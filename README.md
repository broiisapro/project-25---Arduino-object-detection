---

# **Arduino and Python Distance Display Project**

This project uses an ultrasonic sensor connected to an Arduino to measure distances and visualize them in a Python-based GUI. If the measured distance is below a threshold, the GUI indicates the proximity, and an LED on the Arduino flashes.

---

## **Features**
- Measure distances using an ultrasonic sensor.
- Display distance visually in a Python GUI.
- Flash an LED on the Arduino when an object is detected within a set threshold distance.

---

## **Hardware Requirements**
1. Arduino board (e.g., Arduino Uno).
2. Ultrasonic sensor (e.g., HC-SR04).
3. LED.
4. Resistor (220Ω).
5. Jumper wires.
6. Breadboard.

---

## **Circuit Connections**

### **Ultrasonic Sensor**
| Sensor Pin | Arduino Pin   |
|------------|---------------|
| `VCC`      | `5V`          |
| `GND`      | `GND`         |
| `TRIG`     | Digital Pin 9 |
| `ECHO`     | Digital Pin 10|

### **LED**
| LED Pin   | Arduino Pin   |
|-----------|---------------|
| Anode (+) | Digital Pin 8 |
| Cathode (-) | `GND` (via 220Ω resistor) |

---


---

## **Setup and Usage**

### **1. Upload the Arduino Code**
1. Open the Arduino IDE.
2. Copy the provided Arduino sketch into the IDE.
3. Connect the Arduino to your computer via USB.
4. Select the correct board and port in the Arduino IDE.
5. Upload the sketch to the Arduino.

### **2. Connect the Circuit**
Refer to the "Circuit Connections" section to set up the components.

### **3. Run the Python Script**
1. Note the COM port of the Arduino (e.g., `COM3` on Windows).
2. Update the `SERIAL_PORT` variable in the Python script to match your Arduino's COM port.
3. Run the Python script:
   ```bash
   python distance_display.py
   ```

---

## **Customization**
- **Threshold Distance**:
  - Modify the `THRESHOLD_DISTANCE` variable in the Python script and the `thresholdDistance` constant in the Arduino sketch.

---
