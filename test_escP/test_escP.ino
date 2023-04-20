#include <Servo.h> //Arduino Servo Library 

Servo ESC1;  // ESC1 için bir obje tanımlanıyor. 
Servo ESC2;  // ESC2 için bir obje tanımlanıyor. 
Servo ESC3;  // ESC3 için bir obje tanımlanıyor. 
Servo ESC4;  // ESC4 için bir obje tanımlanıyor. 

float value;    // Analog pin A1 den veri okuma için değişken tanımlaması. 

void setup()
{
  Serial.begin(9600);
  
  ESC1.attach(4);  // Pin 4 den PWM sinyal çıkışı.
  ESC2.attach(5);  // Pin 5 den PWM sinyal çıkışı.
  ESC3.attach(6);  // Pin 6 den PWM sinyal çıkışı.
  ESC4.attach(7);  // Pin 7 den PWM sinyal çıkışı.
}

void loop() {  
     
  // Analog girişten okunan değerin ESC nin anlayacağı değerlere çevrilmesi. 
  ESC1.write(100);  // ESC1 için hız değeri ayarlanıyor.
  ESC2.write(100);  // ESC2 için hız değeri ayarlanıyor.
  ESC3.write(100);  // ESC3 için hız değeri ayarlanıyor.
  ESC4.write(100);  // ESC4 için hız değeri ayarlanıyor.
  
  Serial.print("Değer= ");
  //Serial.println(value);
}  
