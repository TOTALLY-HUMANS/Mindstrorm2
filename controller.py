import rpyc
from pynput import keyboard

class Controller():
    conn = None
    doing = None

    def __init__(self):
        while conn is None:
            try:
                self.conn = rpyc.connect('ev3dev', port=18812)
                print("Connected")
            except ConnectionRefusedError:
                pass

    def start(self):
        self.listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release
        )
        self.listener.start()
        self.listener.join()

    def on_press(self, key):
        if doing and not doing.ready:
            return

        try:
            char = key.char
            print("Pressed " + char)
            if char == '1':
                doing = rpyc.asyn(self.conn.root.line_follower())
                print("Started line follower")
        except AttributeError:
            # key is special key
            pass

    def on_release(self, key):
        #
        pass

if __name__ == '__main__':
    c = Controller()
    c.start()
