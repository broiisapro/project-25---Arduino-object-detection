// Define pins for the ultrasonic sensor and LED
const int trigPin = 9;
const int echoPin = 10;
const int ledPin = 8;

// Define a threshold distance in centimeters
const int thresholdDistance = 10;

void setup() {
  // Initialize the serial monitor
  Serial.begin(9600);

  // Set pin modes
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // Send a 10-microsecond pulse to the TRIG pin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Read the ECHO pin and calculate the distance
  long duration = pulseIn(echoPin, HIGH);
  int distance = duration * 0.034 / 2; // Convert to centimeters

  // Print the distance to the serial monitor
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  // Check if the distance is below the threshold
  if (distance > 0 && distance <= thresholdDistance) {
    // Flash the LED
    digitalWrite(ledPin, HIGH);
    delay(200);
    digitalWrite(ledPin, LOW);
    delay(200);
  } else {
    // Turn off the LED
    digitalWrite(ledPin, LOW);
  }

  // Small delay before the next measurement
  delay(100);
}
