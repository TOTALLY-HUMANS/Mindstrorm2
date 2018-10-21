from robot_behaviour_thread import RobotBehaviourThread
import time

class ForestCrawler(RobotBehaviourThread):
    def __init__(self, callback=None):
        super().__init__(callback)

    def run(self):
        print("Starting forest crawler...")
        scan_surroundings = True

        while not self.stopped():
            if scan_surroundings:
                angles, distances = self.scan_room()
                print("DONE SCANNING ROOM...")

                angle_to_use = self.find_longest_open_space(angles, distances)
                print("FOOFOOFOO")
                print(angle_to_use)
                if angle_to_use == 0:
                    angle_to_use = self.gyroscope.angle
                    print("ANGLE WAS 0")

                angle_to_use = angle_to_use - self.gyroscope.angle
                print(abs(angle_to_use))
                self.turn_degrees(abs(angle_to_use), -1)
                scan_surroundings = False
                print(scan_surroundings)

            if self.wall_near():
                print("WALL NEAR!")
                self.stop_movement()
                self.move(0, -20)
                time.sleep(1)
                self.stop_movement()
                scan_surroundings = True

            if not scan_surroundings:
                print("moving")
                self.move(0, 30)

            

    def scan_room(self):
        angles = []
        distances = []

        self.turn_degrees(80, -1)
        initial_angle = self.gyroscope.angle
        self.move(100, 15)

        while self.gyroscope.angle < initial_angle + 180 and self.gyroscope.angle > (initial_angle - 180):
            angles.append(self.gyroscope.angle)
            distances.append(self.ultrasonic_sensor.distance_centimeters)

        self.stop_movement()

        return angles, distances


    def wall_near(self):
        return self.ultrasonic_sensor.distance_centimeters < 5 or self.touch_sensor.is_pressed


    def find_longest_open_space(self, angles, distances):
        
        distances_copy = distances[:]
        distances_copy.sort()
        long_distance_threshold = distances_copy[int(round(0.75 * len(distances)))]
        longest_distance_angle_start = 0
        longest_distance = 0
        longest_distance_index = 0
        current_longest_distance = 0
        start_of_current_longest_distance = 0
        long_distance_hole = False

        print(long_distance_threshold)

        for index, distance in enumerate(distances):

            if distance >= long_distance_threshold:
                if not long_distance_hole:
                    start_of_current_longest_distance = index

                long_distance_hole = True
                current_longest_distance += 1
            else:
                if current_longest_distance > longest_distance:
                    longest_distance = current_longest_distance
                    longest_distance_index = start_of_current_longest_distance

                long_distance_hole = False
                current_longest_distance = 0
                start_of_current_longest_distance = 0

        return angles[int(round((0.5 * longest_distance) + longest_distance_index))]

            
            

        

            
