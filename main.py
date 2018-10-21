#!/usr/bin/env python3
import rpyc
import threading
from rpyc.utils.server import ThreadedServer
from line_follower import LineFollower
from pause import Pause
from forest_crawler import ForestCrawler
from cube_carrier import CubeCarrier
from disc_traveler import DiscTraveler
from slope_searcher import SlopeSearcher
from manual_control import ManualControl
from battlemode import BattleMode
import sys
sys.stdout = sys.__stdout__

class RobotService(rpyc.Service):
    mode = None
    thread = None

    def exposed_change_mode(self, mode, args=None):
        print("Mode change command: " + mode)

        if self.mode == mode:
            return

        if self.thread is not None:
            if self.mode != 'Manual Control':
                self.mode = mode
                self.thread.stop()
                self.thread.join()
            else:
                self.thread.stop_direction(self.thread.direction)

        self.change_mode(mode, args)

    def exposed_start_direction(self, direction):
        if self.mode == 'Manual Control':
            print(direction)
            self.thread.start_direction(direction)

    def exposed_stop_direction(self, direction):
        if self.mode == 'Manual Control':
            self.thread.stop_direction(direction)

    def change_mode(self, mode, args=None):
        self.mode = mode
        print("Changing mode...")
        if self.mode == 'Line Follower':
            print("Creating Line Follower...")
            self.thread = LineFollower(self.change_mode)
            self.thread.start()
        elif self.mode == 'Manual Control':
            print("Starting manual control...")
            self.thread = ManualControl(args)
            print("Manual control started")
        elif self.mode == 'Forest Crawler':
            print("Creating Forest Crawler...")
            self.thread = ForestCrawler(self.change_mode)
            self.thread.start()
        elif self.mode == 'Cube Carrier':
            print("Creating Cube Carrier...")
            self.thread = CubeCarrier(self.change_mode)
            self.thread.start()
        elif self.mode == 'Disc Traveler':
            print("Creating Disc Traveler...")
            self.thread = DiscTraveler(self.change_mode)
            self.thread.start()
        elif self.mode == 'Slope Searcher':
            print("Creating Slope Searcher...")
            self.thread = SlopeSearcher(self.change_mode)
            self.thread.start()
        elif self.mode == 'Battle Mode':
            print("Creating Battle Mode...")
            self.thread = BattleMode(self.change_mode)
            print("FOOBAR")
            self.thread.start()
        elif self.mode == 'Pause':
            print("Pausing...")
            self.thread = Pause()
            self.thread.start()
        elif self.mode == 'Stop':
            print("Stop")

if __name__ == '__main__':
    s = ThreadedServer(RobotService, port=18812)
    s.start()
    print("Started server")
