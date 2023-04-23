/*
  Ultrasonic Sensor HC-SR04 and Arduino Tutorial
  by Dejan Nedelkovski,
  www.HowToMechatronics.com
*/
// defines pins numbers
const int trigPin = 13;
const int echoPin = 12;

#define SENSOR_PIN 8
#define LED_2 2
#define LED_3 3
#define LED_4 4
#define LED_5 5
#define LED_6 6
#define LED_7 7
#define LED_10 10

// defines variables
long duration;
int distance;

void setup() {
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT); // Sets the echoPin as an Input

  // PIR
  pinMode(SENSOR_PIN, INPUT);

  // LED
  pinMode(LED_2, OUTPUT);
  pinMode(LED_3, OUTPUT);
  pinMode(LED_4, OUTPUT);
  pinMode(LED_5, OUTPUT);
  pinMode(LED_6, OUTPUT);
  pinMode(LED_7, OUTPUT);
  pinMode(LED_10, OUTPUT);
  digitalWrite(LED_2, HIGH);
  digitalWrite(LED_3, HIGH);
  digitalWrite(LED_4, HIGH);
  digitalWrite(LED_5, HIGH);
  digitalWrite(LED_6, HIGH);
  digitalWrite(LED_7, HIGH);
  digitalWrite(LED_10, HIGH);

  Serial.begin(9600); // Starts the serial communication
}


void loop() {
   // if sensorValue == 1 (HIGH) if detect motion
  int sensorValue = digitalRead(SENSOR_PIN);
  
  // Clears the trigPin
  digitalWrite(trigPin, LOW);
  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trigPin, HIGH);
  digitalWrite(trigPin, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);
  // Calculating the distance
  distance = duration * 0.034 / 2;

  // reads (whetherDetectMotion, distance)
  Serial.print(sensorValue);
  Serial.print("|");
  Serial.println(distance);

  if (sensorValue == 1 && distance < 100)
  {
    digitalWrite(LED_10, LOW);
    digitalWrite(LED_2, HIGH);
    digitalWrite(LED_3, HIGH);
    digitalWrite(LED_4, HIGH);
    digitalWrite(LED_5, HIGH);
    digitalWrite(LED_6, HIGH);
    digitalWrite(LED_7, HIGH);
    delay(150);
    digitalWrite(LED_2, LOW);
    delay(50);
    digitalWrite(LED_3, LOW);
    delay(50);
    digitalWrite(LED_4, LOW);
    delay(50);
    digitalWrite(LED_5, LOW);
    delay(50);
    digitalWrite(LED_6, LOW);
    delay(50);
    digitalWrite(LED_7, LOW);
    delay(50);
    digitalWrite(LED_2, HIGH);
    delay(50);
    digitalWrite(LED_3, HIGH);
    delay(50);
    digitalWrite(LED_4, HIGH);
    delay(50);
    digitalWrite(LED_5, HIGH);
    delay(50);
    digitalWrite(LED_6, HIGH);
    delay(50);
    digitalWrite(LED_7, HIGH);
    delay(150);
  } 
  else if (sensorValue == 1) 
  {
    digitalWrite(LED_10, LOW);
    digitalWrite(LED_2, LOW);
    digitalWrite(LED_3, LOW);
    digitalWrite(LED_4, LOW);
    digitalWrite(LED_5, LOW);
    digitalWrite(LED_6, LOW);
    digitalWrite(LED_7, LOW);
    delay(150);
    digitalWrite(LED_2, HIGH);
    digitalWrite(LED_3, HIGH);
    digitalWrite(LED_4, HIGH);
    digitalWrite(LED_5, HIGH);
    digitalWrite(LED_6, HIGH);
    digitalWrite(LED_7, HIGH);
  }
  else 
  {
    digitalWrite(LED_10, HIGH);
    digitalWrite(LED_2, LOW);
    digitalWrite(LED_3, LOW);
    digitalWrite(LED_4, LOW);
    digitalWrite(LED_5, LOW);
    digitalWrite(LED_6, LOW);
    digitalWrite(LED_7, LOW);
  }
  
  delay(200);
}
