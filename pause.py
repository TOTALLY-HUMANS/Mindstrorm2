from robot_behaviour_thread import RobotBehaviourThread

class Pause(RobotBehaviourThread):
    def __init__(self, callback=None):
        super().__init__(callback)
        
    def run(self):
        print("Pausing...")
        self.stop_movement()
