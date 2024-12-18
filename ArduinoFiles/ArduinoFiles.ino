/* 
-------------------------------------------------------------------------------------------------------------------------------------------
Author: Marin Dedvukaj <marin.dedvukaj2005@gmail.com>
Date: 15/12/2024
License: Apache 2.0

Description: 
This code is meant for a arduino uno connected to 3 sensors. 1 DHT 22 , 1 light intensity sensor and one microphone.
These sensors will read 4 parameters and display them through serial port. 
The parameters are "humidity/temperature/lightlevel/soundlevel"
the data will be retuned in the format as writen above.
-------------------------------------------------------------------------------------------------------------------------------------------
*/




//Libraries needed for code to run
// "DHT sensor library" by Adafruit
//"BH1750" by Christopher Laws
#include <Wire.h>
#include <BH1750.h>
#include <Adafruit_Sensor.h>
#include <DHT.h>
#include <DHT_U.h>


//Pin definition for DHT
#define DHTPIN 7
#define DHTTYPE DHT22 

// pin definition for microphone
int soundPin = A0;

//dht initialization
DHT dht(DHTPIN, DHTTYPE);

// Initialize BH1750 sensor
BH1750 lightMeter;

//Temperature reading using DHT 22 sensor
float tempReader(){
  // Reading temperature
  float temperature = dht.readTemperature();
  // check if values were read correctly
  if (isnan(temperature)) {
    Serial.println("Failed to read from DHT sensor!");
    return NAN;
  }
  return temperature;
}

//humidity reading using DHT 22 sensor
float humidityReader(){
  // Reading  humidity
  float humidity = dht.readHumidity();
  // check if values were read correctly
  if (isnan(humidity)) {
    Serial.println("Failed to read from DHT sensor!");
    return NAN;
  }
  return humidity;
}


// Light reading using BH1750 sensor
float lightReader() {
  // Get value for light level
  float lux = lightMeter.readLightLevel();
  //cheack if light level was read properly
  if (lux < 0) {
    Serial.println("Failed to read from BH1750 sensor!");
    return NAN;
  }
  return lux;
}

//code for sound level
int soundReader(){
  int soundLevel = analogRead(soundPin);
  soundLevel -= 480;
  if (soundLevel < 0){
    soundLevel *= -1;
  }
  return soundLevel;
}
// Code ran on startup

void setup() {
  // Begin serial communication 
  Serial.begin(9600);
  
  // Initialize DHT sensor
  dht.begin();
  
  // Initialize BH1750 sensor
  Wire.begin();
  if (lightMeter.begin(BH1750::CONTINUOUS_HIGH_RES_MODE)) {
  } else {
    Serial.println("Error initializing BH1750.");
  }
}

void loop() {
  //print in the format humidity/temperature/lightlevel/soundlevel
  Serial.print(humidityReader());
  Serial.print("/");
  Serial.print(tempReader());
  Serial.print("/");
  Serial.print(lightReader());
  Serial.print("/");
  Serial.println(soundReader());
  delay(1000);
}
