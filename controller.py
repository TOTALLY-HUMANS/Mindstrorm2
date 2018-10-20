import rpyc
from pynput import keyboard

class Controller():
    conn = None

    def __init__(self):
        while self.conn is None:
            try:
                self.conn = rpyc.connect('ev3dev', port=18812)
                print("Connected")
            except ConnectionRefusedError:
                print("Retrying...")

    def start(self):
        self.listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release
        )
        self.listener.start()
        self.listener.join()

    def on_press(self, key):
        try:
            char = key.char
            print("Pressed " + char)
            if char == '1':
                print("Starting line follower...")
                rpyc.async_(self.conn.root.change_mode)('Line Follower')
                print("Started line follower")
            elif char == '2':
                print("Starting forest crawler...")
                rpyc.async_(self.conn.root.change_mode)('Forest Crawler')
                print("Started forest crawler")
        except AttributeError as e:
            # key is special key
            print(e)
            pass

    def on_release(self, key):
        #
        print(key)
        pass

if __name__ == '__main__':
    c = Controller()
    c.start()
