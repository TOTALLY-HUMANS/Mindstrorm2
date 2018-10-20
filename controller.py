import rpyc
from pynput import keyboard

class Controller():
    conn = None
    doing = None

    def __init__(self):
        while conn is None:
            try:
                self.conn = rpyc.connect('192.168.2.2', port=18812)
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
            doing = rpyc.asyn(self.conn.root.line_follower())
        except AttributeError:
            # key is special key
            pass

    def on_release(self, key):
        #
        pass

if __name__ == '__main__':
    c = Controller()
    c.start()
