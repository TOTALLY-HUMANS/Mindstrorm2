from robot_behaviour_thread import RobotBehaviourThread

class ForestCrawler(RobotBehaviourThread):
    def __init__(self, callback=None):
        super().__init__(callback)

    def run(self):
        print("Starting forest crawler...")

        room = {}
        while not self.stopped():
            scan_room()
            

    def scan_room():
        self.turn_degrees(-90)
        initial_angle = self.gyroscope.angle
        self.move(100, 50)
        while self.gyroscope.angle < initial_angle + 180:
            room[self.gyroscope.angle] = self.ultrasonic_sensor.distance_centimeters
            print(self.gyroscope.angle)

        print(room)
            

        

            
