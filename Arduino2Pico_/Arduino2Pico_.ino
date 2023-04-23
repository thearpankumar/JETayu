#include <SoftwareSerial.h>

SoftwareSerial mySerial(11, 10);  // RX, TX pins for SoftwareSerial, connect these to the corresponding TX, RX pins on Raspberry Pi Pico

void setup() {
  Serial.begin(9600);  // Initialize Serial Monitor
  mySerial.begin(9600);  // Initialize SoftwareSerial with baudrate 9600
}

void loop() {
  // put your main code here, to run repeatedly:
  while (Serial.available()) {
    byte dataRead = Serial.read();
    mySerial.write(dataRead);
  }
}
