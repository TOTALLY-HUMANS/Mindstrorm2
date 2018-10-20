from robot_behaviour_thread import RobotBehaviourThread
import time

class DiscTraveler(RobotBehaviourThread):
    def __init__(self, callback=None):
        super().__init__(callback)

    def run(self):
        print("Starting disc traveler...")
        
        self.move(0, 60)
        time.sleep(1)
        self.stop_movement()
        self.turn_degrees(70, -1)

        initial_angle = self.gyroscope.angle

        while not self.stopped():

            if not self.ultrasonic_sensor.distance_centimeters < 5:
                angle = self.gyroscope.angle
                delta = abs(initial_angle) - abs(angle) if initial_angle > angle else abs(angle) - abs(initial_angle)
                align = 1 if initial_angle > angle else -1

                self.move(align * delta, 33)


                
