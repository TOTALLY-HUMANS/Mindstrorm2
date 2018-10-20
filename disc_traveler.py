from robot_behaviour_thread import RobotBehaviourThread
import time

class DiscTraveler(RobotBehaviourThread):
    def __init__(self, callback=None):
        super().__init__(callback)

    def run(self):
        print("Starting disc traveler...")
        initial_angle = self.gyroscope.angle
        while not self.stopped():
            angle = self.gyroscope.angle
            self.move(-(initial_angle - angle), 20)
        
