import tkinter as tk
import matplotlib.pyplot as plt

# Define the data for the x and y axes
x_data = [1, 2, 3, 4, 5]
y_data = [2, 4, 6, 8, 10]

# Create a new tkinter window
root = tk.Tk()
root.title("Map")

# Set the size of the window
canvas_width = 500
canvas_height = 500
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

# Create a list to store the coordinates
coordinates = []

def update_plot():
    # Clear the canvas
    canvas.delete("all")

    # Plot the points on the canvas
    for coord in coordinates:
        x, y = coord
        canvas.create_oval(x-2, y-2, x+2, y+2, fill="black")

    # Draw lines between the points
    for i in range(len(coordinates)-1):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[i+1]
        canvas.create_line(x1, y1, x2, y2)

    # Update the plot every 100ms
    root.after(100, update_plot)

def on_click(event):
    # Get the x and y coordinates of the mouse click
    x = event.x
    y = event.y

    # Append the coordinates to the list
    coordinates.append((x, y))

# Bind the left mouse click event to the on_click function
canvas.bind("<Button-1>", on_click)

# Start the plot update loop
root.after(100, update_plot)

# Start the tkinter event loop
root.mainloop()