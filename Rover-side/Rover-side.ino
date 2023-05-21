#include <SoftwareSerial.h>
#include <Servo.h>

int DELAY = 180;
Servo bulldozer;
Servo Steer;

const int triggerPin = 6;
const int echo = 5;

// vcc to 5v ultrasonic gnd to gnd Arduino
long duration;
int distance;

// Motor A
int enA = 9;
int in1 = 8;
int in2 = 7;

// Motor B
int enB = 3;
int in3 = 5;
int in4 = 4;

SoftwareSerial HC12(11, 10);  // RX, TX pins for SoftwareSerial, connect these to the corresponding TX, RX pins on Raspberry Pi Pico
SoftwareSerial ToFromPico(11, 10); 

void setup() {
  Serial.begin(9600);  // Initialize Serial Monitor
  HC12.begin(9600);  // Initialize SoftwareSerial with baudrate 9600
  Serial.begin(9600);
  bulldozer.attach(9);  // attaches the servo on pin 9 to the servo object
  bulldozer.write(180);
  Steer.attach(9);  // attaches the servo on pin 9 to the servo object
  Steer.write(90);

  // Set all the motor control pins to outputs
  pinMode(enA, OUTPUT);
  pinMode(enB, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);

  // Start with motors disabled and direction forward

  // Motor A

  digitalWrite(enA, LOW);
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);

  // Motor B

  digitalWrite(enB, LOW);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);

  Serial.begin(9600);

  while (!Serial.available());
  Serial.read();
}

void loop() {
  // for reciving HC12
   while (HC12.available() or ToFromPico.available()) {  // Check if data is available from Raspberry Pi Pico
    byte picodata = ToFromPico.read();
    byte HC12data = HC12.read();
    //String tata = data ; // Read data from SoftwareSerial until newline character
    Serial.println("Received data: " + HC12data);  // Print received data to Serial Monitor

    if (HC12data == 'w'){
      // Write to both BLDC to increase trush by +10 pwm seconds
      ToFromPico.write("LEFT");
      digitalWrite(in1, HIGH);
      digitalWrite(in2, LOW);
      analogWrite(enA, 255);
      //servo.write(90);
    }

    if (HC12data == 'a') {
    // Write to two BLDC to decrease thrust by +10 PWM seconds
    // giving pico the direction
    ToFromPico.write("RIGHT");
    byte dataRead = ToFromPico.read();
    Steer.write(135);
    }
    if (HC12data == 'd'){
      // Write to left BLDC to increase trush by +10 pwm seconds
      //giving pico the direction 
      ToFromPico.write("RIGHT");
      byte dataRead = ToFromPico.read();
      Steer.write(45);
    }

    if (HC12data == 's'){
      // Write to right  BLDC to increase trush by +10 pwm seconds and reduce left pwm seconds
      //giving pico the direction 
      ToFromPico.write("BACK");
      byte dataRead = ToFromPico.read();
      digitalWrite(in1, LOW);
      digitalWrite(in2, HIGH);
      analogWrite(enA, 255);
      //servo.write(90);
    }

    if (HC12data == 'x'){
      //giving pico the direction 
      byte dataRead = Serial.read();
      Steer.write(90);
    }

    if (HC12data == 'o'){
      // change HC12 to send
          byte dataRead = ToFromPico.read();
          HC12.write(dataRead);
    }
  
  //sensors_code

  }
}


