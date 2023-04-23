#include <SoftwareSerial.h>

SoftwareSerial mySerial(11, 10);  // RX, TX pins for SoftwareSerial, connect these to the corresponding TX, RX pins on Raspberry Pi Pico

void setup() {
  Serial.begin(9600);  // Initialize Serial Monitor
  mySerial.begin(9600);  // Initialize SoftwareSerial with baudrate 9600
}

void loop() {
   while (mySerial.available()) {  // Check if data is available from Raspberry Pi Pico
    byte data = mySerial.read();
    //String tata = data ; // Read data from SoftwareSerial until newline character
    Serial.println("Received data: " + (String)data);  // Print received data to Serial Monitor
  }
    while (Serial.available()) {
    byte dataRead = Serial.read();
    mySerial.write(dataRead);
  }
}

