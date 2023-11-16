import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def plot_chart(data_points):
    plt.clf()  # Clear the previous plot
    plt.plot(data_points, marker='o', linestyle='-', color='b')
    plt.title('Data Points Chart')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    canvas.draw()

def update_chart():
    # Get data points from entry widgets
    data_point1 = float(entry1.get())
    data_point2 = float(entry2.get())
    data_point3 = float(entry3.get())

    # Update the data_points list
    data_points = [data_point1, data_point2, data_point3]

    # Plot the chart
    plot_chart(data_points)

# Create the main window
root = tk.Tk()
root.title("Data Points Chart")

# Create entry widgets for data points
entry1_label = ttk.Label(root, text="Data Point 1:")
entry1_label.grid(row=0, column=0, padx=10, pady=5)
entry1 = ttk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=5)

entry2_label = ttk.Label(root, text="Data Point 2:")
entry2_label.grid(row=1, column=0, padx=10, pady=5)
entry2 = ttk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=5)

entry3_label = ttk.Label(root, text="Data Point 3:")
entry3_label.grid(row=2, column=0, padx=10, pady=5)
entry3 = ttk.Entry(root)
entry3.grid(row=2, column=1, padx=10, pady=5)

# Create a button to update the chart
update_button = ttk.Button(root, text="Update Chart", command=update_chart)
update_button.grid(row=3, column=0, columnspan=2, pady=10)

# Create a Matplotlib figure and canvas
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=4, column=0, columnspan=2)

# Run the Tkinter main loop
root.mainloop()
