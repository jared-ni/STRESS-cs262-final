#define SENSOR_PIN 8


void setup() {
  // put your setup code here, to run once:
  pinMode(SENSOR_PIN, INPUT);
  Serial.begin(9600);

}

void loop() {
  // if sensorValue == 1 (HIGH) if detect motion
  int sensorValue = digitalRead(SENSOR_PIN);
  Serial.println(sensorValue);
  delay(2000);
}
