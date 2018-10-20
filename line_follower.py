from robot_behaviour_thread import RobotBehaviourThread
import time

class LineFollower(RobotBehaviourThread):
    turning = 0
    started_turning = time.time()

    def __init__(self, callback=None):
        super().__init__(callback)

    def run(self):
        print("Starting line follower...")
        while not self.stopped():
            if self.line_found():
                self.move(0, 60)
                self.set_turning_to(0)
            elif self.turning == 1 and (time.time() - self.started_turning) >= 4:
                self.move(-90, 60)
                self.set_turning_to(1)
            else:
                self.move(90, 60)
                self.set_turning_to(-1)
        self.callback("Forest Crawler")

    def set_turning_to(self, turn):
        if self.turning != turn:
            self.turning = turn
            self.started_turning = time.time()
