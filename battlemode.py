from robot_behaviour_thread import RobotBehaviourThread
from ev3dev2.led import Leds
from time import sleep


class BattleMode(RobotBehaviourThread):

    leds = Leds()
    enemy_contact = False
    touch_sensor_active = False

    def __init__(self, callback=None):
        super().__init__(callback)

    def run(self):
        print("Engaging battlemode...")
        self.change_color()
        print("Battlemode engaged...")

        self.enter_thunderdome()

        # Drive circles until enemy contact
        while not enemy_contact():
            self.move(30, 60)
            self.check_touch_sensor_status()
            if (self.touch_sensor_active):
                self.charge()
            
    def enter_thunderdome(self):
        # Enter battle positions
        print("Entering Thunderdome")
        self.move(0, 30)
        sleep(5)
        self.stop_movement():
        print("In position")


    def charge(self):
        # Charge forward until the motion sensor is no longer active
        self.stop_movement():
        sleep(1)
        while (self.touch_sensor_active)
            self.move(0, 90)

        # Robot must turn so that it faces the edge so that it does not
        # reverse over the edge

        self.move(0, -30)
        sleep(5)
        self.stop_movement():

    def check_touch_sensor_status(self):
        # Check touch sensor values
        if (self.color_sensor.reflected_light_intensity < 50 ):
                self.touch_sensor_active = True
                print("Target accuired")
            else:
                self.touch_sensor_active = False

    def edge_tracker(self):
        # Track the edges of the platform



    def change_color(self):
        # Change LED to colors suitable for battle

        # Turn all LEDs off
        leds.all_off()
        sleep(1)

        # Set both pairs of LEDs to red (as for blood of the enemies)
        leds.set_color('LEFT', 'RED')
        leds.set_color('RIGHT', 'RED')

    
