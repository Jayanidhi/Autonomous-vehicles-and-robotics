import random

class AutonomousVehicle:
    def __init__(self):
        self.speed = 0
        self.direction = "straight"

    def accelerate(self):
        self.speed += 10
        print(f"Accelerating to {self.speed} km/h")

    def brake(self):
        self.speed -= 10
        if self.speed < 0:
            self.speed = 0
        print(f"Braking to {self.speed} km/h")

    def turn(self, direction):
        self.direction = direction
        print(f"Turning {direction}")

    def detect_obstacle(self):
        obstacle_distance = random.randint(1, 100)
        if obstacle_distance < 20:
            print("Obstacle detected! Braking...")
            self.brake()
        else:
            print("No obstacle detected. Accelerating...")
            self.accelerate()

    def navigate(self):
        self.detect_obstacle()
        if self.speed > 0:
            self.turn(random.choice(["left", "right", "straight"]))

vehicle = AutonomousVehicle()
for _ in range(10):
    vehicle.navigate()
