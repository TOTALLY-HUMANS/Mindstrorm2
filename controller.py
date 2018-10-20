import rpyc
from pynput import keyboard
from pynput.keyboard import Key

class Controller():
    conn = None
    mode = None
    updown = False
    downdown = False
    leftdown = False
    rightdown = False
    clawlift = False
    clawlower = False

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
            elif char == '3':
                self.change_mode('Cube Carrier')
            elif char == '4':
                self.change_mode('Disc Traveler')
            elif char == '5':
                self.change_mode('Slope Searcher')
            elif char == '6':
                self.change_mode('Battle Mode')
            elif char == 'q':
                self.change_mode('Stop')
                return False
            elif char == 'w':
                self.change_mode('Pause')
            elif char == 'l' and not self.clawlift:
                self.start_manual_control('clawlift')
                self.clawlift = True
            elif char == 'o' and not self.clawlower:
                self.start_manual_control('clawlower')
                self.clawlower = True

        except AttributeError as e:
            if key == Key.up and not self.updown:
                self.start_manual_control('up')
                self.updown = True
            elif key == Key.down and not self.downdown:
                self.start_manual_control('down')
                self.downdown = True
            elif key == Key.left and not self.leftdown:
                self.start_manual_control('left')
                self.leftdown = True
            elif key == Key.right and not self.rightdown:
                self.start_manual_control('right')
                self.rightdown = True

    def on_release(self, key):
        try:
            char = key.char
            if char == 'l':
                self.stop_manual_control('clawlift')
                self.clawlift = False
            elif char == 'o':
                self.stop_manual_control('clawlower')
                self.clawlower = False

        except AttributeError as e:
            if key == Key.up:
                self.stop_manual_control('up')
                self.updown = False
            elif key == Key.down:
                self.stop_manual_control('down')
                self.downdown = False
            elif key == Key.left:
                self.stop_manual_control('left')
                self.leftdown = False
            elif key == Key.right:
                self.stop_manual_control('right')
                self.rightdown = False

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
