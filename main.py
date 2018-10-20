#!/usr/bin/env python3
import rpyc
from rpyc.utils.server import ThreadedServer
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank, MoveSteering
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, LightSensor, InfraredSensor, ColorSensor
from ev3dev2.led import Leds

class RobotService(rpyc.Service):
    drive = MoveSteering(OUTPUT_B, OUTPUT_C)
    sensor = ColorSensor(INPUT_4)
    sensor.mode = ColorSensor.MODE_COL_REFLECT
    
    def exposed_line_follower(self):
        self.move(0, 60)
        while True:
            if (self.line_found()):
                self.move(0, 60)
            else:
                self.move(-90, 60)

    def line_found(self):
        return self.sensor.reflected_light_intensity < 50 

    def move(self, angle, speed):
        self.drive.on(angle, SpeedPercent(speed))
            
    def stop(self):
        self.move(0,0)

if __name__ == '__main__':
    s = ThreadedServer(RobotService, port=18812)
    s.start()
