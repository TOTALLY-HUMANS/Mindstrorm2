#!/usr/bin/env python3
import rpyc
import threading
from rpyc.utils.server import ThreadedServer
from line_follower import LineFollower
from pause import Pause
from forest_crawler import ForestCrawler

class RobotService(rpyc.Service):
    mode = None
    thread = None

    def exposed_change_mode(self, mode):
        print("Mode change command: " + mode)
        
        if self.mode == mode:
            return

        self.mode = mode
        if self.thread is not None:
            self.thread.stop()
            self.thread.join()

        self.change_mode(mode)
        

    def change_mode(self, mode):
        self.mode = mode
        print("Changing mode...")
        if self.mode == 'Line Follower':
            print("Creating Line Follower...")
            self.thread = LineFollower(self.change_mode)
            self.thread.start()
        if self.mode == 'Forest Crawler':
            print("Creating Forest Crawler...")
            self.thread = ForestCrawler(self.change_mode)
            self.thread.start()
        if self.mode == 'Pause':
            print("Pausing...")
            self.thread = Pause()
            self.thread.start()
        if self.mode == 'Stop':
            print("Stop")

if __name__ == '__main__':
    s = ThreadedServer(RobotService, port=18812)
    s.start()
    print("Started server")
