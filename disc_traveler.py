from robot_behaviour_thread import RobotBehaviourThread
import time

class DiscTraveler(RobotBehaviourThread):
    def __init__(self, callback=None):
        super().__init__(callback)

    def run(self):
        print("Starting disc traveler...")
        self.move(-20, 20)
        