#include <SoftwareSerial.h>
SoftwareSerial HC12(10, 11); // HC-12 TX Pin, HC-12 RX Pin
void setup() {
  Serial.begin(9600);             
  HC12.begin(9600);               
}
void loop() {
  while (HC12.available()) {           
    int data=HC12.read(); 
    Serial.println(data);
    
  }
      
  
}