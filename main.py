import serial
import tkinter as tk

# Serial port configuration
SERIAL_PORT = "COM4"  # Replace with your Arduino's port
BAUD_RATE = 9600

# Threshold distance (in cm)
THRESHOLD_DISTANCE = 25

# Create the Tkinter window
root = tk.Tk()
root.title("Distance Display")
canvas_width = 400
canvas_height = 300
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

# Initialize serial communication
try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
except Exception as e:
    print(f"Error connecting to serial port: {e}")
    exit()

def update_canvas():
    """Update the canvas based on the distance."""
    try:
        # Read distance from Arduino
        if ser.in_waiting > 0:
            distance = ser.readline().decode('utf-8').strip()
            distance = int(float(distance))  # Ensure it's an integer

            # Clear the canvas
            canvas.delete("all")

            # Draw green background
            canvas.create_rectangle(0, 0, canvas_width, canvas_height, fill="green")

            # If object detected, draw a red bar
            if distance <= THRESHOLD_DISTANCE:
                red_height = int((THRESHOLD_DISTANCE - distance) / THRESHOLD_DISTANCE * canvas_height)
                canvas.create_rectangle(0, canvas_height - red_height, canvas_width, canvas_height, fill="red")

    except ValueError:
        # Handle invalid serial data
        pass

    # Schedule the next update
    root.after(5, update_canvas)

# Start the canvas update loop
update_canvas()

# Run the Tkinter main loop
root.mainloop()

# Close the serial port when done
ser.close()