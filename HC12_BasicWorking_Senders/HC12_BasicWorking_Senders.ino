#include <SoftwareSerial.h>

int distance;


SoftwareSerial HC12(10, 11); // HC-12 TX Pin, HC-12 RX Pin

void setup() {
   Serial.begin(9600); 
   HC12.begin(9600);               // Serial port to HC12
}

void loop() {
  distance = "i";
  HC12.write(distance);
  HC12.print(distance);
}
