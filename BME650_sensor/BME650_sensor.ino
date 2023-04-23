#include <math.h>
#include <Wire.h>
#include <SPI.h>
#include <Adafruit_Sensor.h>
#include "Adafruit_BME680.h"

#define SEALEVELPRESSURE_HPA (1013.25)

Adafruit_BME680 bme;

void setup() {
  Serial.begin(9600);
  if (!bme.begin()) {
    Serial.println("Could not find a valid BME680 sensor, check wiring!");
    while (1);
  }
}

void loop() {
  if (! bme.performReading()) {
    Serial.println("Failed to perform reading");
    return;
  }
  float P = bme.pressure;
  float Alt = ((((((10 * log10((P / 100.0) / 1013.25)) / 5.2558797) - 1) / (-6.8755856 * pow(10, -6))) / 1000) * 0.30);
  Serial.print("My Formula: ");
  Serial.println(Alt);
  Serial.print("Adafruit Formula: ");
  Serial.println(bme.readAltitude(SEALEVELPRESSURE_HPA));
  delay(5000);
}