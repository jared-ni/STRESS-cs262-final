/*
  Ultrasonic Sensor HC-SR04 and Arduino Tutorial

  by Dejan Nedelkovski,
  www.HowToMechatronics.com

*/
// defines pins numbers
const int trigPin = 9;
const int echoPin = 10;

#define SENSOR_PIN 2

// defines variables
long duration;
int distance;

void setup() {
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT); // Sets the echoPin as an Input

  // PIR
  pinMode(SENSOR_PIN, INPUT);

  Serial.begin(9600); // Starts the serial communication
}


void loop() {
   // if sensorValue == 1 (HIGH) if detect motion
  int sensorValue = digitalRead(SENSOR_PIN);
//  Serial.print("PIR: ");
//  Serial.println(sensorValue);

  
  // Clears the trigPin
  digitalWrite(trigPin, LOW);
  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trigPin, HIGH);
  digitalWrite(trigPin, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);
  // Calculating the distance
  distance = duration * 0.034 / 2;
  // Prints the distance on the Serial Monitor
//  Serial.print("Distance: ");
//  Serial.print(distance);
//  Serial.println(" cm");

  // reads (whetherDetectMotion, distance)
  Serial.print(sensorValue);
  Serial.print(" ");
  Serial.println(distance);
  delay(200);
}
