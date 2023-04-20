
#include <SoftwareSerial.h>

// RX (Pin 0 of Arduino digital IO) to Echo
// TX (Pin 1 of Arduino digital IO) to Trig 
unsigned int HighLen = 0;
unsigned int LowLen  = 0;
unsigned int Len_mm  = 0;


void setup() 
{   
    Serial.begin(9600);                         
}

void loop() 
{
    Serial.flush();                               
    Serial.write(0X55);                           // trig US-100 begin to measure the distance
    delay(500);                                   
    if(Serial.available() >= 2)                   // receive 2 bytes 
    {
        HighLen = Serial.read();                   // High byte of distance
        LowLen  = Serial.read();                   // Low byte of distance
        Len_mm  = HighLen*256 + LowLen;            // Calculate the distance
        if((Len_mm > 1) && (Len_mm < 10000))       // normal distance should between 1mm and 10000mm (1mm, 10m)
        {
            Serial.print("Present Length is: ");   
            Serial.print(Len_mm, DEC);             
            Serial.println("mm");                  
        }
    }
    delay(500);                                   
}
