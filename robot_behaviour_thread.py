import threading
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank, MoveSteering
from ev3dev2.sensor.lego import TouchSensor, LightSensor, UltrasonicSensor, ColorSensor, GyroSensor
from ev3dev2.led import Leds

class RobotBehaviourThread(threading.Thread):
    move_steering = MoveSteering(OUTPUT_B, OUTPUT_C)
    color_sensor = ColorSensor()
    color_sensor.mode = ColorSensor.MODE_COL_REFLECT
    ultrasonic_sensor = UltrasonicSensor()
    gyroscope = GyroSensor()
    touch_sensor = TouchSensor()

    def __init__(self, callback=None):
        super().__init__()
        print("Initializing thread")
        self._stop_event = threading.Event()
        self.callback = callback

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    def move(self, angle, speed):
        self.move_steering.on(angle, SpeedPercent(speed))

    def turn_degrees(self, degrees, direction):
        initial_angle = self.gyroscope.angle

        direction_actual = -100 if direction <= 0 else 100        
        self.move(direction_actual, 25)

        print("rotating")
        print(initial_angle)
        while self.gyroscope.angle < initial_angle + degrees and self.gyroscope.angle > initial_angle - degrees:
            pass

        print("done rotating")
        self.stop_movement()

    def stop_movement(self):
        self.move_steering.off(brake=True)

    def get_color(self):
        self.color_sensor.mode = 'COL-COLOR'
        #print(self.color_sensor.value())
        return self.color_sensor.value()
