#include <SoftwareSerial.h>
#include <Wire.h>


SoftwareSerial HC12(2, 3); // HC-12 TX Pin, HC-12 RX Pin

void setup() {
   Serial.begin(9600); 
   Wire.begin();
   //mpu.initialize();// Serial port to computer
   HC12.begin(9600);               // Serial port to HC12

}

void loop() {

      HC12.write(12);
      Serial.print(12);

     }   

