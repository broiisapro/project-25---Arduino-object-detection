#include <Servo.h>

const int trigPin = 10;
const int echoPin = 11;
Servo servoMotor;  // Create Servo object

long duration;
int distance;
int angle = 15;  // Starting angle for the servo

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);
  servoMotor.attach(12);  // Servo motor connected to pin 9
}

void loop() {
  // Sweep the servo from 15 to 165 degrees and back
  for (angle = 15; angle <= 165; angle++) {
    servoMotor.write(angle);
    delay(30);
    distance = getDistance();  // Get the distance from ultrasonic sensor
    Serial.print(angle);
    Serial.print(",");
    Serial.println(distance);  // Send data to Python
  }
  
  // Sweep back from 165 to 15 degrees
  for (angle = 165; angle >= 15; angle--) {
    servoMotor.write(angle);
    delay(30);
    distance = getDistance();
    Serial.print(angle);
    Serial.print(",");
    Serial.println(distance);
  }
}

long getDistance() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  duration = pulseIn(echoPin, HIGH);
  distance = duration * 0.034 / 2;  // Calculate the distance in cm
  return distance;
}
