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

        turnTimer = 1.7
        turnSpeed = 20
        moveSpeed = 60

        first_turn = left

        while not self.stopped():
            color = self.get_color()
            if color == 6:
                if self.turning == left:
                    first_turn = left
                elif self.turning == right:
                    first_turn = right
                self.move(straight, moveSpeed)
                self.set_turning_to(straight)
            elif color == 4:
                # self.move(first_turn, turnSpeed)
                # time.sleep(turnTimer * 1.3)
                self.move(straight, moveSpeed)
                time.sleep(0.3)
                self.move(0, -moveSpeed)
                time.sleep(1.5)
                self.stop_movement()
                time.sleep(5)
                first_turn = left
                self.move(first_turn, turnSpeed)
                time.sleep(0.5)
                self.set_turning_to(first_turn)
            elif (not self.turning == -first_turn) and (self.turning == straight or (time.time() - self.started_turning) <= turnTimer):
                self.move(first_turn, turnSpeed)
                self.set_turning_to(first_turn)
            elif self.turning != -first_turn or (time.time() - self.started_turning) <= (2.2 * turnTimer):
                self.move(-first_turn, turnSpeed)
                self.set_turning_to(-first_turn)

        #self.callback("Forest Crawler")

    def set_turning_to(self, turn):
        if self.turning != turn:
            self.turning = turn
            self.started_turning = time.time()

    def line_found(self):
        self.color_sensor.mode = 'COL-REFLECT'
        return self.color_sensor.reflected_light_intensity > 30

    def yellow_found(self):
        self.color_sensor.mode = 'COL-COLOR'
        return self.color_sensor.value() == 4

    def red_found(self):
        self.color_sensor.mode = 'COL-COLOR'
        return self.color_sensor.value() == 5

    def print_reflect(self):
        self.color_sensor.mode = 'COL-REFLECT'
        print("REFLECT: " + str(self.color_sensor.reflected_light_intensity))

        # Lattia 1 (joskus 2)
        # Viiva 6
        # Oranssi 6
        # Tumma oranssi 5
        # Keltainen 4
