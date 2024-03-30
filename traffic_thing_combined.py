import tkinter as tk
import random

class ConsciousnessField:
    def __init__(self):
        self.state = "Undefined"

    def update_state(self, car_actions):
        if "Observed" in car_actions:
            self.state = "Altered"
        else:
            self.state = "Natural"

class Car:
    def __init__(self, name, start_position, color):
        self.name = name
        self.position = start_position
        self.color = color
        self.path = []

    def plan_path(self, destination):
        # Simplified path planning to destination
        self.path = [self.position, destination]

    def move(self):
        if self.path:
            self.position = self.path.pop(0)

class Observer:
    def __init__(self, observation_range):
        self.observation_range = observation_range

    def observe(self, car):
        return "Observed" if abs(car.position[0]) <= self.observation_range and abs(car.position[1]) <= self.observation_range else "Not observed"

class GridVisualization:
    def __init__(self, size, cars, observer, field):
        self.size = size
        self.cars = cars
        self.observer = observer
        self.field = field
        self.root = tk.Tk()
        self.root.title("Traffic Simulation with Consciousness Field")
        self.canvas = tk.Canvas(self.root, width=500, height=550, background='white')
        self.canvas.pack(padx=10, pady=10)
        self.update()

    def draw_grid(self):
        for i in range(self.size):
            for j in range(self.size):
                self.canvas.create_rectangle(50 * i, 50 * j, 50 * (i + 1), 50 * (j + 1), fill='white', outline='gray')

    def place_cars_and_observer(self):
        car_actions = []
        for car in self.cars:
            x, y = car.position
            self.canvas.create_rectangle(50 * x, 50 * y, 50 * (x + 1), 50 * (y + 1), fill=car.color, outline='gray')
            car_actions.append(self.observer.observe(car))

        self.field.update_state(car_actions)

    def display_field_state(self):
        self.canvas.create_text(250, 525, text=f"Consciousness Field State: {self.field.state}", font=('Helvetica', 12))

    def update(self):
        self.canvas.delete("all")
        self.draw_grid()
        self.place_cars_and_observer()
        self.display_field_state()
        for car in self.cars:
            car.move()
        self.root.after(1000, self.update)

# Setup
field = ConsciousnessField()
cars = [Car('A', (0, 0), 'red'), Car('B', (4, 4), 'blue')]
observer = Observer(observation_range=5)
for car in cars:
    car.plan_path((4, 4))

# Visualization
visualization = GridVisualization(10, cars, observer, field)
visualization.root.mainloop()
