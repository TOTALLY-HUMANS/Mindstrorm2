#!/usr/bin/env python3
import rpyc
from rpyc.utils.server import ThreadedServer
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds

class RobotService(rpyc.Service):
    def exposed_line_follower(self):
        tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)

        # drive in a turn for 5 rotations of the outer motor
        # the first two parameters can be unit classes or percentages.
        tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(75), 10)

        # drive in a different turn for 3 seconds
        tank_drive.on_for_seconds(SpeedPercent(60), SpeedPercent(30), 3)

if __name__ == '__main__':
    s = ThreadedServer(RobotService, port=18812)
    s.start()
