import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from datetime import datetime
from tkcalendar import DateEntry  # Import DateEntry from tkcalendar


def on_closing():
    print('closing....')
    # if messagebox.askokcancel("Quit", "Do you want to quit?"):
    # root.destroy()  # for production build
    exit() # for dev use.

def plot_chart(data_points):
    plt.clf()  # Clear the previous plot

    # Extract data from data_points
    dates_str = [entry[3] for entry in data_points]
    open_prices = [entry[0] for entry in data_points]
    close_prices = [entry[1] for entry in data_points]
    volumes = [entry[2] for entry in data_points]

    # Convert date strings to datetime objects
    dates = [datetime.strptime(date, '%d-%m-%y') for date in dates_str]

    # Plot the chart
    plt.plot(dates, open_prices, marker='o', linestyle='-', color='b', label='Open Price')
    plt.plot(dates, close_prices, marker='o', linestyle='-', color='g', label='Close Price')
    plt.plot(dates, volumes, marker='o', linestyle='-', color='r', label='Volume')

    plt.title('Stock Data Chart')
    plt.xlabel('Day')
    plt.ylabel('Values')
    plt.legend()
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    canvas.draw()

def update_chart():
    try:
        open_price = float(entry_open.get())
        close_price = float(entry_close.get())
        volume = float(entry_volume.get())
        
        # Get date from DateEntry widget
        date = entry_date.get_date()

        # Update the data_points list
        data_points.append([open_price, close_price, volume, date.strftime('%d-%m-%y')])

        # Plot the chart
        plot_chart(data_points)

        # Update the table
        update_table()

        # Clear entry widgets
        entry_open.delete(0, tk.END)
        entry_close.delete(0, tk.END)
        entry_volume.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values.")

def update_table():
    # Clear existing items in the table
    for item in table.get_children():
        table.delete(item)

    # Insert new data into the table
    for row in data_points:
        table.insert("", "end", values=row)

# Create the main window
root = tk.Tk()
root.title("Stock Data Chart")

# Create entry widgets for data points
entry_open_label = ttk.Label(root, text="Open Price:")
entry_open_label.grid(row=0, column=0, padx=10, pady=5)
entry_open = ttk.Entry(root)
entry_open.grid(row=0, column=1, padx=10, pady=5)

entry_close_label = ttk.Label(root, text="Close Price:")
entry_close_label.grid(row=1, column=0, padx=10, pady=5)
entry_close = ttk.Entry(root)
entry_close.grid(row=1, column=1, padx=10, pady=5)

entry_volume_label = ttk.Label(root, text="Volume:")
entry_volume_label.grid(row=2, column=0, padx=10, pady=5)
entry_volume = ttk.Entry(root)
entry_volume.grid(row=2, column=1, padx=10, pady=5)

# Create a DateEntry widget for the "day" data point
entry_date_label = ttk.Label(root, text="Day:")
entry_date_label.grid(row=3, column=0, padx=10, pady=5)
entry_date = DateEntry(root, format="%d-%m-%y", locale='en_US')  # Specify date format
entry_date.grid(row=3, column=1, padx=10, pady=5)

# Create a button to update the chart
update_button = ttk.Button(root, text="Update Chart", command=update_chart)
update_button.grid(row=4, column=0, columnspan=2, pady=10)

# Create a Matplotlib figure and canvas
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=5, column=0, columnspan=2)

# Create a table to display the data points
columns = ["Open", "Close", "Volume", "Day"]
table = ttk.Treeview(root, columns=columns, show="headings")

# Set column headings
for col in columns:
    table.heading(col, text=col)

table.grid(row=6, column=0, columnspan=2, pady=10)

# Initialize the data_points list
data_points = []

# Handle window closing event
root.protocol("WM_DELETE_WINDOW", on_closing)

# ... (rest of the code remains the same)

# Run the Tkinter main loop
root.mainloop()