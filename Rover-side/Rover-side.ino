#include <SoftwareSerial.h>
#include <Servo.h>

int DELAY = 180;
Servo bulldozer;
Servo Steer

SoftwareSerial HC12(11, 10);  // RX, TX pins for SoftwareSerial, connect these to the corresponding TX, RX pins on Raspberry Pi Pico
SoftwareSerial ToFromPico(11, 10); 

void setup() {
  Serial.begin(9600);  // Initialize Serial Monitor
  HC12.begin(9600);  // Initialize SoftwareSerial with baudrate 9600
  Serial.begin(9600);
  bulldozer.attach(9);  // attaches the servo on pin 9 to the servo object
  bulldozer.write(180);
  steer.attach(9);  // attaches the servo on pin 9 to the servo object
  steer.write(180);
  while (!Serial.available());
  Serial.read();
}

void loop() {
  // for reciving HC12
   while (HC12.available() or ToFromPico.available()) {  // Check if data is available from Raspberry Pi Pico
    byte picodata = ToFromPico.read()
    byte HC12data = HC12.read()
    //String tata = data ; // Read data from SoftwareSerial until newline character
    Serial.println("Received data: " + (String)HC12data);  // Print received data to Serial Monitor

    if (String(char(String(HC12data))) == 'w'){
      // Write to both BLDC to increase trush by +10 pwm seconds
          ToFromPico.write("Front");
    }

    if (String(char(String(HC12data))) == 's'){
      // Write to two BLDC to decrease trush by +10 pwm seconds
      //giving pico the direction 
      byte dataRead = Serial.read();
      ToFromPico.write("Back");
    }

    if (String(char(String(HC12data))) == 'd'){
      // Write to left BLDC to increase trush by +10 pwm seconds
      //giving pico the direction 
      byte dataRead = Serial.read();
      ToFromPico.write("Left");
    }

    if (String(char(String(HC12data))) == 's'){
      // Write to right  BLDC to increase trush by +10 pwm seconds and reduce left pwm seconds
      //giving pico the direction 
      byte dataRead = Serial.read();
      ToFromPico.write("Right");
    }

    if (String(char(String(HC12data))) == 'o'){
      // change HC12 to send
      while (HC12.available()) {
          byte dataRead = Serial.read();
          HC12.write(dataRead);
  }
    }
  }

  for (int DELAY1 = 180; delay > 90; i--){
    myservo.write(DELAY1);
  }

  for (int DELAY2 = 180; delay > 90; i--){
    steer.write(DELAY);
}

