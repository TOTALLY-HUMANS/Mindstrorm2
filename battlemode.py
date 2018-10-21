from robot_behaviour_thread import RobotBehaviourThread
from ev3dev2.led import Leds
from time import sleep


class BattleMode(RobotBehaviourThread):

    leds = Leds()

    def __init__(self, callback=None):
        super().__init__(callback)
        print("INIT")

    def run(self):
        enemy_in_range = False
        print("Engaging battlemode...")
        self.change_color()
        print("Battlemode engaged...")

        self.enter_thunderdome()
        self.move(100, 30)
        sleep(1)
        self.move(-80, 60)

        while not self.stopped():
            edge_detected = self.edge_detected()
            touch_sensor_status = self.check_touch_sensor_status()

            # Drive circles until enemy contact
            if touch_sensor_status and not enemy_in_range and not edge_detected:
                print("Enemy in range")
                self.move(0, 99)
                enemy_in_range = True

            if enemy_in_range and not edge_detected:
                if not touch_sensor_status:
                    print("ENEMY ELIMINATED")
                    self.stop_movement()
                    self.move(0, -30)
                    sleep(2)
                    self.stop_movement()
                    enemy_in_range = False

            if edge_detected:
                print("EDGE DETECTED")
                self.stop_movement()
                self.move(0, -45)
                sleep(1)
                self.turn_degrees(135, 1)

            if not enemy_in_range and not edge_detected:
                self.move(-80, 60)
                
                

            

    def enter_thunderdome(self):
        # Enter battle positions
        print("Entering Thunderdome")
        self.move(0, 45)
        sleep(7)
        self.stop_movement()
        print("In position")

    def check_touch_sensor_status(self):
        return self.touch_sensor.is_pressed

    def edge_detected(self):
        # Track the edges of the platform
        # get_color(self):
        # self.color_sensor.mode = 'COL-REFLECT'
        # return self.color_sensor.reflected_light_intensity < 5

        self.color_sensor.mode = 'COL-COLOR'
        for j in range(3):
            edge_color = self.get_color()
            if (edge_color == 0):
                return True
            
        return False


    def print_reflect(self):
        self.color_sensor.mode = 'COL-REFLECT'
        print("REFLECT: " + str(self.color_sensor.reflected_light_intensity))

    def change_color(self):
        # Change LED to colors suitable for battle

        # Turn all LEDs off
        self.leds.all_off()
        sleep(1)

        # Set both pairs of LEDs to red (as for blood of the enemies)
        self.leds.set_color('LEFT', 'RED')
        self.leds.set_color('RIGHT', 'RED')

    
