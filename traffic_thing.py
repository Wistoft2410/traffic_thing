import random

class Grid:
    def __init__(self, size):
        self.size = size
        self.grid = [['.' for _ in range(size)] for _ in range(size)]

    def display(self):
        for row in self.grid:
            print(' '.join(row))
        print()

class Car:
    def __init__(self, name, start, end):
        self.name = name
        self.position = start
        self.destination = end
        self.path = []

    def plan_path(self, grid):
        # Simplified path planning: move straight to the destination if possible
        x, y = self.position
        dest_x, dest_y = self.destination
        while x != dest_x or y != dest_y:
            if x < dest_x: x += 1
            elif x > dest_x: x -= 1
            if y < dest_y: y += 1
            elif y > dest_y: y -= 1
            self.path.append((x, y))

    def move(self):
        if self.path:
            self.position = self.path.pop(0)

class ConsciousnessField:
    def __init__(self):
        self.state = "Calm"

    def update_state(self, cars):
        # The field's state changes based on the collective movement of cars
        if any(car.path for car in cars):
            self.state = "Dynamic"
        else:
            self.state = "Harmonized"

    def display_state(self):
        print(f"Consciousness Field State: {self.state}\n")

# Simulation setup
grid_size = 5
grid = Grid(grid_size)
field = ConsciousnessField()

# Initialize cars with start and end positions
cars = [Car('A', (0, 0), (4, 4)), Car('B', (4, 0), (0, 4))]

# Plan paths for each car
for car in cars:
    car.plan_path(grid)

# Main simulation loop
for _ in range(grid_size * 2):
    grid.grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
    for car in cars:
        car.move()
        x, y = car.position
        grid.grid[x][y] = car.name
    grid.display()
    field.update_state(cars)
    field.display_state()
