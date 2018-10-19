import rpyc
from rpyc.utils.server import ThreadedServer

class RobotService(rpyc.Service):
    def exposed_print_msg(self, msg):
        print(msg)

if __name__ == '__main__':
    s = ThreadedServer(RobotService, port=18812)
    s.start()
