---

## **Ultrasonic Sensor Visualization with Servo and Radar Display**

### **Overview**
This project demonstrates the use of an ultrasonic sensor mounted on a servo motor to create a radar-like scanning system. Data is visualized in real-time using a Python-based graphical interface.

### **Features**
- **Arduino**:
  - Uses an ultrasonic sensor to measure distances.
  - Servo motor sweeps the sensor across a range of angles (15° to 165°).
  - Transmits angle and distance data over Serial.
- **Python**:
  - Real-time radar visualization using Pygame.
  - Displays distance as a continuous line mapped to detected objects.
  - Tracks and displays the last 5 positions of objects for continuity.

### **Hardware Requirements**
1. Arduino board (e.g., Uno or Mega).
2. Ultrasonic sensor (e.g., HC-SR04).
3. Servo motor.
4. USB cable for connecting Arduino to the computer.
5. A computer with Python and Pygame installed.

### **Software Requirements**
- **Arduino IDE**: For uploading the Arduino sketch.
- **Python 3.x**: For running the visualization.
  - Libraries: `pygame`, `serial`, `math`, `collections`.

### **Setup Instructions**
1. **Arduino**:
   - Connect the ultrasonic sensor to the Arduino:
     - Trig Pin → Digital Pin 10
     - Echo Pin → Digital Pin 11
   - Connect the servo motor to Pin 12.
   - Upload the provided Arduino sketch.
2. **Python**:
   - Install Python libraries:
     ```bash
     pip install pygame pyserial
     ```
   - Modify `PORT` in the Python script to match your Arduino's COM port.
   - Run the Python script:
     ```bash
     python radar_visualization.py
     ```

### **How It Works**
1. The servo motor sweeps the ultrasonic sensor back and forth.
2. The ultrasonic sensor measures distances and sends the angle and distance to the Python program.
3. Pygame visualizes the data as a radar, plotting objects in real time.

### **Improvements Over the First Version**
- **Dynamic Scanning**: The sensor now sweeps across a range of angles.
- **Enhanced Visualization**: Replaced static Tkinter visualization with a Pygame-based radar display.
- **Real-Time Feedback**: Continuous angle and distance display with object tracking.
- **Modular Design**: The distance calculation and visualization logic are modularized for scalability.

---
