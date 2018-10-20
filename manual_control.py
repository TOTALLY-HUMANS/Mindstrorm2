from ev3dev2.motor import OUTPUT_B, OUTPUT_C, MoveSteering, SpeedPercent

class ManualControl():
    move_steering = MoveSteering(OUTPUT_B, OUTPUT_C)
    direction = None

    def __init__(self, direction):
        print(direction)
        self.start_direction(direction)

    def start_direction(self, direction):
        self.direction = direction
        if self.direction == 'up':
            self.move(0, 60)
        elif self.direction == 'down':
            self.move(0, -60)
        elif self.direction == 'left':
            self.move(-90, 60)
        elif self.direction == 'right':
            self.move(90, 60)

    def stop_direction(self, direction):
        if direction and self.direction == direction:
            self.stop_movement()
            self.direction = None

    def move(self, angle, speed):
        print(angle)
        print(speed)
        self.move_steering.on(angle, SpeedPercent(speed))

    def stop_movement(self):
        self.move_steering.off(brake=True)