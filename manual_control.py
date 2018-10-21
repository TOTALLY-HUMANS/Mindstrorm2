from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, MoveSteering, SpeedPercent, ServoMotor, Motor, MediumMotor

class ManualControl():
    claw_movement = MediumMotor(OUTPUT_D)
    move_steering = MoveSteering(OUTPUT_B, OUTPUT_C)
    direction = None

    def __init__(self, direction):
        print(direction)
        self.start_direction(direction)

    def start_direction(self, direction):
        self.stop_direction(self.direction)
        self.direction = direction
        if self.direction == 'up':
            self.move(0, 70)
        elif self.direction == 'down':
            self.move(0, -70)
        elif self.direction == 'left':
            self.move(-90, 70)
        elif self.direction == 'right':
            self.move(90, 70)
        elif self.direction == 'clawlift':
            print("clawlift")
            self.claw_control(-20)
        elif self.direction == 'clawlower':
            print("clawlower")
            self.claw_control(20)

    def stop_direction(self, direction):
        if direction and self.direction == direction:
            if direction == 'clawlift' or direction == 'clawlower':
                self.stop_claw()
            else:
                self.stop_movement()
            self.direction = None

    def move(self, angle, speed):
        print(angle)
        print(speed)
        self.move_steering.on(angle, SpeedPercent(speed))

    def stop_movement(self):
        self.move_steering.off(brake=True)

    def claw_control(self, speed):
        print("Claw control " + str(speed))
        self.claw_movement.on(speed)

    def stop_claw(self):
        self.claw_movement.off(brake=True)
