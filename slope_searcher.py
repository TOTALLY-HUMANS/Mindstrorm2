from robot_behaviour_thread import RobotBehaviourThread
import time

class SlopeSearcher(RobotBehaviourThread):
    def __init__(self, callback=None):
        super().__init__(callback)

    def run(self):
        print("Starting disc traveler...")

        while not self.stopped():
            pass