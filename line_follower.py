from robot_behaviour_thread import RobotBehaviourThread

class LineFollower(RobotBehaviourThread):
    def __init__(self, callback=None):
        super().__init__(callback)

    def run(self):
        print("Starting line follower...")
        #self.callback("Forest Crawler")
        while not self.stopped():
            if (self.line_found()):
                self.move(0, 60)
            else:
                self.move(-90, 60)
