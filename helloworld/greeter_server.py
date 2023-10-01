from concurrent import futures
import logging
import time
import grpc
import attack_pb2
import attack_pb2_grpc
import random

class Greeter(attack_pb2_grpc.GreeterServicer):

    no_soldiers = None
    battelfeild_size = None
    total_time_of_war = None
    interval_time = None
    count = 0
    result_val = False
    
    ##TEST
    def SayHello(self, request, context):
        return attack_pb2.HelloReply(message=f"SO,{request.name}!")

############################################################################
#   TAKING USER INPUT AND SETTING THE CLASS GLOBAL VARIABLE FOR FURTHER USE
############################################################################

    @classmethod
    def set_inputs_from_client(cls,M,N,T,t):
        # store inputs which client has sent
        # After storing, call core functionality
        cls.no_soldiers, cls.battelfeild_size, cls.total_time_of_war, cls.interval_time = M,N,T,t
        #cls.op()
        
        #creating obj for calling an instance method
        s1 = cls()
        s1.module()
      
############################################################################
#   CHOOSING A COMMANDER
############################################################################

    def choose_commander(self,soldier_matrix):
        return random.choice(list(soldier_matrix.keys()))

############################################################################
#   CREATING OUTPUT PATTERN FOR SOLDIERS
############################################################################

    def printLayout(self,soldier_matrix, battelfield_size, cols, commander):
        for i in range(battelfield_size):
            for j in range(cols):
                for soldier, data in soldier_matrix.items():
                    if data["coordinates"] == (i, j):
                        if soldier == commander:
                            print(f"C{soldier.split()[-1]} ", end="")
                        else:
                            print(f"{soldier.split()[-1]} ", end="")
                        break
                else:
                    print(". ", end="")
            print()

        if soldier_matrix:
            print("\nCoordinates and Speed:")
            for soldier, data in soldier_matrix.items():
                if soldier == commander:
                    print(f"{soldier}: {data['coordinates']} (Speed {data['speed']}) [Commander]")
                else:
                    print(f"{soldier}: {data['coordinates']} (Speed {data['speed']})")

############################################################################
#   SOLDIERS WHO ESCAPED OR HIT
############################################################################

    def was_hit(self,soldierID):
        print("\nSoldiers who Escaped:")
        for soldier in soldierID:
            print(soldier)

############################################################################
#   MAIN MODULE OF WAR
############################################################################

    def module(self):
        num_soldiers = self.no_soldiers
        num_soldiers2 = self.no_soldiers
        t = self.interval_time
        num_of_attack = int(self.total_time_of_war/self.interval_time)

        rows, cols = self.battelfeild_size, self.battelfeild_size  # You can adjust the size of the matrix as needed.
        soldier_matrix = self.status(rows, cols, num_soldiers)
        commander = self.choose_commander(soldier_matrix)

        while self.count!=num_of_attack:
            print(f"\nIteration with Commander: {commander}\n")

            print("Initial Positions of Soldiers:")
            self.printLayout(soldier_matrix, rows, cols, commander)

            missile_type, missile_target, red_zone_coordinates, died_soldiers, escaped_soldiers = self.missile_approaching(
                soldier_matrix)

            print("\nMissile Fired:")
            print(f"Missile Type: {missile_type}")
            print(f"Target Coordinate: {missile_target}")
            print(f"RED Zone Coordinates: {red_zone_coordinates}")

            if died_soldiers:
                print("\nThe following soldiers died:")
                for soldier in died_soldiers:
                    print(soldier)
            else:
                print("\nNo soldiers were killed.")

            self.was_hit(escaped_soldiers)

            # Update the soldier matrix for the next iteration
            soldier_matrix = {k: v for k, v in soldier_matrix.items() if k in escaped_soldiers}

            # Check if the commander is dead, and select a new commander if needed
            if commander not in soldier_matrix:
                print("\nCommander was killed! Selecting a new commander.")
                commander = self.choose_commander(soldier_matrix)

            if self.count==(num_of_attack-1):
                break

            print(f"\nNext missile-attack in {t} seconds...")
            self.count+=1
            time.sleep(t)
        
        #PRINTTING THE RESULT:
        survived_soldiers=len(escaped_soldiers)
        print("\nno of soldires left",survived_soldiers)
        print("no of soldires were",num_soldiers)

        if survived_soldiers <=  int(num_soldiers/2):
            print("\nWe lose the war...")   
        else:
            self.result_val = True
            print("\nwe won the war...")  

############################################################################
#   SOLDIER'S CURRENT STATUS
############################################################################

    def status(self,rows, cols,num_soldiers):
        total_elements = rows * cols

        if total_elements < 9:
            print("Error: Not enough elements in the matrix to place 9 soldiers.")
            return None

        coordinates = random.sample([(x, y) for x in range(rows) for y in range(cols)], num_soldiers)
        soldiers = {f"Soldier {i + 1}": {"coordinates": (x, y), "speed": random.randint(0, 4)} for i, (x, y) in
                    enumerate(coordinates)}
        return soldiers

############################################################################
#   MISSILE ATTACK IN "T" TIME AT "t" INTERVAL
############################################################################

    def missile_approaching(self,soldier_matrix):
        missile_x, missile_y = random.choice(list(soldier_matrix.values()))["coordinates"]
        missile_type = random.randint(1, 4)
        red_zone_radius = missile_type - 1

        print(f"Missile Type {missile_type} targeted ({missile_x}, {missile_y})")

        red_zone_coordinates = [(x, y) for x in range(missile_x - red_zone_radius, missile_x + red_zone_radius + 1)
                                for y in range(missile_y - red_zone_radius, missile_y + red_zone_radius + 1)]

        died_soldiers = []
        escaped_soldiers = []

        for soldier, data in soldier_matrix.items():
            x, y, speed = data["coordinates"][0], data["coordinates"][1], data["speed"]

            if ((x, y) in red_zone_coordinates) and (speed == 0):
                died_soldiers.append(soldier)
            elif ((missile_x, missile_y) == (x, y)) and (speed < missile_type):
                died_soldiers.append(soldier)
            elif ((x, y) in red_zone_coordinates) and ((missile_type - abs(missile_x - x)) > speed):
                died_soldiers.append(soldier)
            elif ((x, y) in red_zone_coordinates) and (missile_x == x) and ((missile_type - abs(missile_y - y)) > speed):
                died_soldiers.append(soldier)
            else:
                escaped_soldiers.append(soldier)

        for soldier in died_soldiers:
            del soldier_matrix[soldier]

        return missile_type, (missile_x, missile_y), red_zone_coordinates, died_soldiers, escaped_soldiers


        missile_x, missile_y = random.choice(list(soldier_matrix.values()))["coordinates"]
        missile_type = random.randint(1, 2)
        red_zone_radius = missile_type - 1

        print(f"Missile Type {missile_type} targeted ({missile_x}, {missile_y})")

        red_zone_coordinates = [(x, y) for x in range(missile_x - red_zone_radius, missile_x + red_zone_radius + 1)
                                for y in range(missile_y - red_zone_radius, missile_y + red_zone_radius + 1)]

        died_soldiers = []
        escaped_soldiers = []

        for soldier, data in soldier_matrix.items():
            x, y, speed = data["coordinates"][0], data["coordinates"][1], data["speed"]

            if (x, y) in red_zone_coordinates and speed < red_zone_radius:
                died_soldiers.append(soldier)
            else:
                escaped_soldiers.append(soldier)

        return missile_type, (missile_x, missile_y), red_zone_coordinates, died_soldiers, escaped_soldiers

ob1 = Greeter()

def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    commander = Greeter()
    attack_pb2_grpc.add_GreeterServicer_to_server(commander, server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()

if __name__ == "__main__":
    logging.basicConfig()
    serve()

