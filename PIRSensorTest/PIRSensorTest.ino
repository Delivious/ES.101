
#include <SPI.h>
#include <WiFiNINA.h>
#include <ArduinoHttpClient.h>
#include <ArduinoJson.h>


const int sensor = 4;
const int led = 2;
char ssid[] = "BPstudent"; 
char pass[] = "studentuse"; 

int status = WL_IDLE_STATUS;

int val = LOW;
const int capacity = JSON_OBJECT_SIZE(1);
StaticJsonDocument<capacity> doc;
WiFiClient wifi;
HttpClient client = HttpClient(wifi, "10.30.1.18", 5000);

void setup() {
  Serial.begin(9600);
  doc["motion"] = 0;
  String json;
  serializeJson(doc, json);
  WiFiClient wifi;
  HttpClient client = HttpClient(wifi, "10.30.1.18", 5000);
  pinMode(led, OUTPUT);
  pinMode(sensor, INPUT);
  Serial.println("Connecting to WiFi...");
  while(status != WL_CONNECTED){
    Serial.println(".");
    status = WiFi.begin(ssid, pass);
    delay(10000);
  }
  Serial.println("Successfully connected to network!");
  Serial.println("Configuring Sensors...");
  delay(60000);
  Serial.println("Configured.");
}

void loop() {
  // put your main code here, to run repeatedly:
  val = digitalRead(sensor);
  if (val==HIGH){

    client.beginRequest();
    Serial.println("Motion");
    digitalWrite(led, HIGH);
    
    Serial.println();
    client.post("/api/logs");
    client.beginBody();
    client.endRequest();
    int statusCode = client.responseStatusCode();
    Serial.println("Sent Signal!");
    delay(1000);
  }
  else{
    digitalWrite(led, LOW);
  }
  
  
}
