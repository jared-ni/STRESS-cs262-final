/*
  CS262 STRESS final project
  Jared Ni, Gary Wu, Jessica Chen, Bryan Han
  Arduino Uno - US-100 Ultrasonic Sensor connection
*/

#include <SoftwareSerial.h>


SoftwareSerial us100(3, 2);

unsigned int high_byte = 0;
unsigned int low_byte  = 0;
unsigned int distance  = 0;

void setup() {
  
  Serial.begin(9600);
  us100.begin(9600);
}

void loop() {
  us100.flush();
  // trigs distance measurement on the US-100 to begin
  us100.write(0X55);
  delay(200);  
  
  // check receive 2 bytes correctly                       
  if (us100.available() >= 2) 
  {
    high_byte = us100.read();
    low_byte  = us100.read();
    
    // distance calculation
    distance  = high_byte * 256 + low_byte;
    Serial.print("Distance: ");
    Serial.print(distance, DEC);          
    Serial.println("mm");        
  }                                     
} 
