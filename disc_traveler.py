from robot_behaviour_thread import RobotBehaviourThread
import time

class DiscTraveler(RobotBehaviourThread):
    def __init__(self, callback=None):
        super().__init__(callback)

    def run(self):
        print("Starting disc traveler...")
        initial_angle = self.gyroscope.angle
        self.move(0, 60)
        time.sleep(0.5)

        while not self.stopped():
            angle = self.gyroscope.angle
            self.move(-(initial_angle - angle), 20)
