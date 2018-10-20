from robot_behaviour_thread import RobotBehaviourThread
from ev3dev2.led import Leds
from time import sleep


class BattleMode(RobotBehaviourThread):

    leds = Leds()
    enemy_in_range = False

    def __init__(self, callback=None):
        super().__init__(callback)

    def run(self):
        print("Engaging battlemode...")
        self.change_color()
        print("Battlemode engaged...")

        self.enter_thunderdome()
        self.move(30, 60)

        while not self.stopped():
            # Drive circles until enemy contact
            if self.check_touch_sensor_status() and not enemy_in_range:
                self.move(0, 99)
                enemy_in_range = True

            if enemy_in_range:
                if not self.check_touch_sensor_status():
                    self.stop_movement()
                    self.move(0, -30)
                    sleep(1)
                    self.stop_movement()
                    enemy_in_range = False
                    self.move(30, 60)

            if self.edge_detected():
                self.stop_movement()

                for i in range(3):
                    self.turn_degrees(90, 1)
                    if not self.edge_detected():
                        break
                
                

            
            
    def enter_thunderdome(self):
        # Enter battle positions
        print("Entering Thunderdome")
        self.move(0, 30)
        sleep(5)
        self.stop_movement():
        print("In position")

    def check_touch_sensor_status(self):
        return self.infrared_sensor.proximity < 5

    def edge_detected(self):
        # Track the edges of the platform
        self.color_sensor.mode = 'COL-REFLECT'
        return self.color_sensor.reflected_light_intensity < 5
        

    def change_color(self):
        # Change LED to colors suitable for battle

        # Turn all LEDs off
        leds.all_off()
        sleep(1)

        # Set both pairs of LEDs to red (as for blood of the enemies)
        leds.set_color('LEFT', 'RED')
        leds.set_color('RIGHT', 'RED')

    
