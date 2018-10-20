from robot_behaviour_thread import RobotBehaviourThread
import time

class LineFollower(RobotBehaviourThread):
    turning = 0
    started_turning = time.time()

    def __init__(self, callback=None):
        super().__init__(callback)

    def run(self):
        print("Starting line follower...")
        straight = 0
        left = -90
        right = 90
        
        turnTimer = 1
        turnSpeed = 30
        moveSpeed = 60

        first_turn = left

        while not self.stopped():
            if self.line_found():
                if self.turning == left:
                    first_turn = left
                elif self.turning == right
                    first_turn = right

                self.move(straight, moveSpeed)
                self.set_turning_to(straight)
            elif (not self.turning == right) and (self.turning == straight or (time.time() - self.started_turning) <= turnTimer):
                self.move(left, turnSpeed)
                self.set_turning_to(left)
            else:
                self.move(right, turnSpeed)
                self.set_turning_to(right)
        self.callback("Forest Crawler")

    def set_turning_to(self, turn):
        if self.turning != turn:
            self.turning = turn
            self.started_turning = time.time()
    
    def line_found(self):
        return self.color_sensor.reflected_light_intensity > 30
