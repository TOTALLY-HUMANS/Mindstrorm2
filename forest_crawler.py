from robot_behaviour_thread import RobotBehaviourThread

class ForestCrawler(RobotBehaviourThread):
    def __init__(self, callback=None):
        super().__init__(callback)

    def run(self):
        print("Starting forest crawler...")

        #while not self.stopped():

        angles, distances = self.scan_room()
        print("DONE SCANNING ROOM...")
        
        angle_to_use = find_longest_open_space(angles, distances)
        print(angle_to_use)
        angle_to_use = self.gyroscope.angle - angle_to_use
        self.stop_movement()
        self.turn_degrees(abs(angle_to_use), angle_to_use)


            
            

    def scan_room(self):
        angles = []
        distances = []

        self.turn_degrees(90, -1)
        initial_angle = self.gyroscope.angle
        self.move(100, 50)

        print("GOGOGOGOGOGOGO")
        print(initial_angle)

        while self.gyroscope.angle < initial_angle + 180 and self.gyroscope.angle > initial_angle - 180:
            angles.append(self.gyroscope.angle)
            distances.append(self.infrared_sensor.distance)

        print("DEBUG POINT 1")
        self.stop_movement()

        return angles, distances

    def find_longest_open_space(self, angles, distances):
        
        distances_copy = distances[:]
        distances_copy.sort()
        long_distance_threshold = distances_copy[int(round(0.5 * len(distances)))]
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
                    print("foo")

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

            
            

        

            
