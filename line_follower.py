from robot_behaviour_thread import RobotBehaviourThread

class LineFollower(RobotBehaviourThread):
    def __init__(self, callback=None):
        super().__init__(callback)

    def run(self):
        turning = 0
        print("Starting line follower...")
        while not self.stopped():
            if self.line_found():
                self.move(0, 60)
            elif turning == 1:
                self.move(-90, 60)
            elif turning == -1:
                pass
            elif turning == 0:
                turning = 1
        self.callback("Forest Crawler")
