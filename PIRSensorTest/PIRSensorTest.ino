const int sensor = 4;
const int led = 2;

int val = LOW;


void setup() {
  // put your setup code here, to run once:
  pinMode(led, OUTPUT);
  pinMode(sensor, INPUT);
  Serial.begin(9600);
  Serial.println("Configuring Sensors...");
  delay(60000);
  
}

void loop() {
  // put your main code here, to run repeatedly:
  val = digitalRead(sensor);
  if (val==HIGH){
    Serial.println("Motion");
    digitalWrite(led, HIGH);
  }
  else{
    Serial.println("None");
    digitalWrite(led, LOW);
  }
  
  
}
