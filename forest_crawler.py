from robot_behaviour_thread import RobotBehaviourThread

class ForestCrawler(RobotBehaviourThread):
    def __init__(self, callback=None):
        super().__init__(callback)

    def run(self):
        print("Starting forest crawler...")

        #while not self.stopped():

        angles, distances = self.scan_room()
        print(angles)
        print(distances)
            
            

    def scan_room(self):
        angles = []
        distances = []
        print("turning 90...")
        self.turn_degrees(90)
        print("turned 90")
        initial_angle = self.gyroscope.angle
        self.move(100, 50)

        while self.gyroscope.angle < initial_angle + 180 and self.gyroscope.angle > initial_angle - 180:
            print(initial_angle)
            print(self.gyroscope.angle)
            print("--")
            angles.append(self.gyroscope.angle)
            distances.append(self.infrared_sensor.distance)

        return angles, distances
            

        

            
