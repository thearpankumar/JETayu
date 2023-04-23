#include <Servo.h>

int DELAY = 180;
Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

void setup() {
  Serial.begin(9600);
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
  myservo.write(180);
  while (!Serial.available());
  Serial.read();
}

void loop() {
  if (Serial.available() > 0)
  {
    int DELAY = Serial.parseInt();
    if (DELAY > 0)
    {
      
      myservo.write(DELAY);
      //Serial.print("\n");
      //Serial.println("Motor speed:"); Serial.print("  "); Serial.print(SPEED); Serial.print("%"); 
    }     
  }
}
