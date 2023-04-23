#include <SoftwareSerial.h>

SoftwareSerial hc12Serial(1, 0); // RX, TX pins of HC-12

void setup() {
  Serial.begin(9600);
  hc12Serial.begin(9600);
}

void loop() {
  String data = "q"; // Data to send
  hc12Serial.println(data); // Send data via HC-12
  Serial.println("Sent: " + data);
  delay(1000);
}
