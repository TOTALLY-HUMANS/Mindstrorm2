import rpyc
from pynput import keyboard
from pynput.keyboard import Key

class Controller():
    conn = None
    mode = None

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
                self.change_mode('Line Follower')
            elif char == '2':
                self.change_mode('Forest Crawler')
            elif char == 'q':
                self.change_mode('Stop')
                return False
            elif char == 'w':
                self.change_mode('Pause')

        except AttributeError as e:
            print(key)
            if key == Key.up:
                self.start_manual_control('up')
            elif key == Key.down:
                self.start_manual_control('down')
            elif key == Key.left:
                self.start_manual_control('left')
            elif key == Key.right:
                self.start_manual_control('right')

    def on_release(self, key):
        print(key)
        if key == Key.up:
            self.stop_manual_control('up')
        elif key == Key.down:
            self.stop_manual_control('down')
        elif key == Key.left:
            self.stop_manual_control('left')
        elif key == Key.right:
            self.stop_manual_control('right')

    def change_mode(self, mode, args=None):
        self.mode = mode
        print("Starting: " + mode)
        rpyc.async_(self.conn.root.change_mode)(mode, args)
        print("Started: " + mode)

    def start_manual_control(self, direction):
        if self.mode != 'Manual Control':
            self.change_mode('Manual Control', direction)
        else:
            rpyc.async_(self.conn.root.start_direction)(direction)

    def stop_manual_control(self, direction):
        rpyc.async_(self.conn.root.stop_direction)(direction)


if __name__ == '__main__':
    c = Controller()
    c.start()
