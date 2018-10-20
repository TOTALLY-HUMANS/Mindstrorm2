#!/usr/bin/env python3
import rpyc
import threading
from rpyc.utils.server import ThreadedServer
from line_follower import LineFollower
from pause import Pause
from forest_crawler import ForestCrawler
from manual_control import ManualControl

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
        elif self.mode == 'Battle Mode':
            print("Created Battle Mode...")
            self.thread = BattleMode(self.change_mode)
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
