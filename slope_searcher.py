from robot_behaviour_thread import RobotBehaviourThread
import time

class SlopeSearcher(RobotBehaviourThread):
    foundRed = False
    foundYellow = False
    foundBlue = False
    foundGreen = False
    foundAll = False

    foundTarget = 0
    foundSecondTime = False

    turning = 0
    started_turning = time.time()

    white = 6
    red = 5
    yellow = 4
    blue = 2
    green = 3

    def __init__(self, callback=None):
        super().__init__(callback)

    def update_found_colors(self, color):
        if color == self.red:
            self.foundRed = True
        elif color == self.yellow:
            self.foundYellow = True
        elif color == self.blue:
            self.foundBlue = True
        elif color == self.green:
            self.foundGreen = True

        self.foundAll = (self.foundRed and self.foundYellow and self.foundBlue and self.foundGreen)

    def run(self):
        print("Starting line follower...")
        straight = 0
        left = -90
        right = 90

        turnTimer = 1.7
        turnSpeed = 20
        moveSpeed = 40

        first_turn = left
        first_turn_always_left = False

        while not self.stopped():
            color = self.get_color()
            #print(color)
            if not self.foundAll:
                self.update_found_colors(color)
                if self.foundAll:
                    self.move(straight, moveSpeed)
                    self.set_turning_to(straight)
                    time.sleep(1)
                    continue
            elif (self.foundTarget == 0) and (color == self.red or color == self.yellow or color == self.blue or color == self.green):
                self.foundTarget = color
                self.set_turning_to(straight)
                self.turn_degrees(180, 1)
                continue
            elif (self.foundTarget != 0) and color == self.foundTarget:
                self.foundSecondTime = True
                continue

            if (self.foundSecondTime and color == self.foundTarget) or ((not self.foundSecondTime) and (color == self.white or color == self.red or color == self.yellow or color == self.blue or color == self.green)):
                if self.turning == left or first_turn_always_left:
                    first_turn = left
                    if first_turn_always_left and (time.time() - self.started_turning) > 1.4:
                        first_turn_always_left = False
                elif self.turning == right:
                    first_turn = right
                self.move(straight, moveSpeed)
                self.set_turning_to(straight)
            elif (not self.turning == -first_turn) and (self.turning == straight or (time.time() - self.started_turning) <= turnTimer):
                self.move(first_turn, turnSpeed)
                self.set_turning_to(first_turn)
            elif self.turning != -first_turn or (time.time() - self.started_turning) <= (2.2 * turnTimer):
                self.move(-first_turn, turnSpeed)
                self.set_turning_to(-first_turn)

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
