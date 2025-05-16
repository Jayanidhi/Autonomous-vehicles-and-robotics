import numpy as np
import heapq
import time

# A* algorithm implementation
def a_star(grid, start, goal):
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    neighbors = [(0,1),(1,0),(-1,0),(0,-1)]
    close_set = set()
    came_from = {}
    gscore = {start:0}
    fscore = {start:heuristic(start, goal)}
    open_heap = []

    heapq.heappush(open_heap, (fscore[start], start))

    while open_heap:
        _, current = heapq.heappop(open_heap)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        close_set.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j
            tentative_g_score = gscore[current] + 1
            if 0 <= neighbor[0] < grid.shape[0] and 0 <= neighbor[1] < grid.shape[1]:
                if grid[neighbor[0]][neighbor[1]] == 1:
                    continue
            else:
                continue

            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue

            if tentative_g_score < gscore.get(neighbor, float('inf')):
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_heap, (fscore[neighbor], neighbor))
    return []

# Simple PID simulation
class PID:
    def __init__(self, kp, ki, kd):
        self.kp, self.ki, self.kd = kp, ki, kd
        self.integral = 0
        self.prev_error = 0

    def update(self, target, current):
        error = target - current
        self.integral += error
        derivative = error - self.prev_error
        output = self.kp*error + self.ki*self.integral + self.kd*derivative
        self.prev_error = error
        return output

# Simulated robot controller
def simulate_robot(grid, start, goal):
    path = a_star(grid, start, goal)
    pid = PID(1.0, 0.1, 0.05)
    current_pos = list(start)

    print("Navigating from", start, "to", goal)
    for step in path[1:]:
        control_signal = pid.update(step[0], current_pos[0])  # Simulated x-axis movement control
        current_pos[0] += np.sign(control_signal)
        current_pos[1] = step[1]
        print(f"Moving to {tuple(current_pos)}, Control Signal: {control_signal:.2f}")
        time.sleep(0.5)  # Simulate delay

# Define map grid (0 = free space, 1 = obstacle)
grid = np.zeros((10, 10))
grid[3][3:7] = 1
grid[6][2:5] = 1

start = (0, 0)
goal = (9, 9)

simulate_robot(grid, start, goal)
