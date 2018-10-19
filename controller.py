import rpyc
from pynput import keyboard

class Controller():
    def __init__(self):
        self.conn = rpyc.connect('192.168.2.2', port=18812)

    def start(self):
        self.listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release
        )
        self.listener.start()
        self.listener.join()

    def stop(self):
        self.listener.stop()

    def on_press(self, key):
        self.stop()
        try:
            self.conn.root.line_follower()
        except AttributeError:
            # key is special key
            pass
        self.start()

    def on_release(self, key):
        #
        pass

if __name__ == '__main__':
    c = Controller()
    c.start()
