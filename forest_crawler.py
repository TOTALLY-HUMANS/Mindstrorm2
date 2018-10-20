from robot_behaviour_thread import RobotBehaviourThread

class ForestCrawler(RobotBehaviourThread):
    def __init__(self, callback=None):
        super().__init__(callback)

    def run(self):
        print("Starting forest crawler...")

        #while not self.stopped():

        angles, distances = scan_room()
        print(angles)
        print(distances)
            
            

    def scan_room():
        angles = []
        distances = []
        print("1")
        self.turn_degrees(-90)
        print("2")
        initial_angle = self.gyroscope.angle
        self.move(100, 50)

        while self.gyroscope.angle < initial_angle + 180 and self.gyroscope.angle > initial_angle - 180:
            angles.append(self.gyroscope.angle)
            distances.append(self.ultrasonic_sensor.distance_centimeters)
            print(self.gyroscope.angle)
            print(initial_angle)
            print("---")

        return angles, distances
            

        

            
