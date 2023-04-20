/*
  US-100 Ultrasonic Sensor - Triggrt_Echo Mode
  modified on 26 Sep 2020
  by Mohammad Reza Akbari @ Electropeak
  Home

*/

const int pingPin = 6; // Trigger Pin of Ultrasonic Sensor
const int echoPin = 5; // Echo Pin of Ultrasonic Sensor

long duration;

void setup() {
  pinMode(pingPin, OUTPUT);
  pinMode(echoPin, INPUT);
  digitalWrite(pingPin, LOW);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(pingPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(pingPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  Serial.print(duration);
  Serial.println(" cm");
  delay(300);
}
