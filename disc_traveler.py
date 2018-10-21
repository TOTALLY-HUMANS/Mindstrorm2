from robot_behaviour_thread import RobotBehaviourThread
import time

class DiscTraveler(RobotBehaviourThread):
    def __init__(self, callback=None):
        super().__init__(callback)

    def run(self):
        print("Starting disc traveler...")
        print(self.ultrasonic_sensor.distance_centimeters)
        print("foo")

        initial_angle = self.gyroscope.angle

        while not self.stopped():

            if (not self.ultrasonic_sensor.distance_centimeters < 5) and (not self.touch_sensor.is_pressed):
                angle = self.gyroscope.angle
                delta = (initial_angle - angle) % 360

                self.move(-1 * (delta / 3.6), 60)
            else:
                self.stop_movement()


                
