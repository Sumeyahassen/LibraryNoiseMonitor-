import tkinter as tk  # For GUI window
import numpy as np# For generating fake noise data
import matplotlib.pyplot as plt# For graph plotting
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg# For embedding Matplotlib in Tkinter

# Sound level thresholds
LOW_THRESHOLD = 20 # If sound level is below 20 → "Quiet"
HIGH_THRESHOLD = 50 # If sound level is above 50 → "Too Loud" 

# Create main application window
root = tk.Tk() # Create the main window
root.title("Noise Detection System")  # Window title
root.geometry("500x400") # Set window size

# Label to display noise status
status_label = tk.Label(root, text="Waiting for noise data...", font=("Times New Roman", 20))
status_label.pack(pady=10)

# Create a Matplotlib figure for real-time noise level visualization
fig, ax = plt.subplots(figsize=(5, 2))
x_data = list(range(10))  # Last 10 sound readings
y_data = [0] * 10
line, = ax.plot(x_data, y_data, "g-")  # Green line for low noise

ax.set_ylim(0, 100)
ax.set_xlim(0, 9)
ax.set_xlabel("Time")
ax.set_ylabel("Sound Level")

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Function to update fake sound data
def update_noise_level():
    global y_data

    # Generate fake sound level (random number between 0 and 100)
    sound_level = np.random.randint(0, 100)

    # Update GUI based on sound level
    if sound_level < LOW_THRESHOLD:
        status_label.config(text="✅ Quiet! You can enter the library.", fg="green")
        line.set_color("g")
    elif sound_level > HIGH_THRESHOLD:
        status_label.config(text="🔇 Too loud! Please keep quiet.", fg="red")
        line.set_color("r")
    else:
        status_label.config(text="⚠️ Moderate noise level.", fg="orange")
        line.set_color("orange")

    # Update graph data
    y_data.append(sound_level)
    y_data.pop(0)  # Remove oldest value
    line.set_ydata(y_data)
    
    # Redraw graph
    canvas.draw()

    # Schedule the next update
    root.after(1000, update_noise_level)  # Update every second

# Start the simulation
# 
update_noise_level()

# Run the Tkinter GUI loop
root.mainloop()
