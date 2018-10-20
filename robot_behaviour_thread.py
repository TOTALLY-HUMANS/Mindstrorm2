import threading
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank, MoveSteering
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, LightSensor, InfraredSensor, ColorSensor
from ev3dev2.led import Leds

class RobotBehaviourThread(threading.Thread):
    move_steering = MoveSteering(OUTPUT_B, OUTPUT_C)
    color_sensor = ColorSensor(INPUT_4)
    color_sensor.mode = ColorSensor.MODE_COL_REFLECT
    gyroscope = GyroSensor()


    def __init__(self, callback=None):
        super().__init__()
        print("Initializing thread")
        self._stop_event = threading.Event()
        self.callback = callback

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()
    
    def line_found(self):
        return self.color_sensor.reflected_light_intensity < 50 

    def move(self, angle, speed):
        self.move_steering.on(angle, SpeedPercent(speed))

    def turn_degrees(self, degrees):
        direction = degrees <= 0 ? -100 : 100
        self.move(direction, 50)
        gyroscope.wait_until_angle_changed_by(degrees)
        self.stop_movement()

    def stop_movement(self):
        self.move_steering.off(brake=True)