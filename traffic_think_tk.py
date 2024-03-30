import tkinter as tk

class GridVisualization:
    def __init__(self, size, cars, field):
        self.size = size
        self.cars = cars
        self.field = field
        self.root = tk.Tk()
        self.root.title("Traffic Simulation and Consciousness Field")
        self.canvas = tk.Canvas(self.root, width=500, height=550, borderwidth=5, background='white')
        self.canvas.pack()
        self.car_colors = {'A': 'red', 'B': 'blue'}

    def draw_grid(self):
        for i in range(self.size):
            for j in range(self.size):
                self.canvas.create_rectangle(i * 100, j * 100, (i + 1) * 100, (j + 1) * 100, fill='white')

    def place_cars(self):
        for car in self.cars:
            x, y = car.position
            self.canvas.create_rectangle(x * 100, y * 100, (x + 1) * 100, (y + 1) * 100, fill=self.car_colors[car.name])

    def update_field_state(self):
        self.canvas.create_text(250, 525, text=f"Consciousness Field State: {self.field.state}", font=('Helvetica', 12))

    def update(self):
        self.canvas.delete("all")
        self.draw_grid()
        self.place_cars()
        self.update_field_state()
        self.root.after(1000, self.update)  # Update every second

    def run(self):
        self.update()
        self.root.mainloop()

# Initialize the consciousness field and cars as before
field = ConsciousnessField()
cars = [Car('A', (0, 0), (4, 4)), Car('B', (4, 0), (0, 4))]
for car in cars:
    car.plan_path(grid)

# Initialize and run the visualization
grid_visualization = GridVisualization(grid_size, cars, field)
grid_visualization.run()
