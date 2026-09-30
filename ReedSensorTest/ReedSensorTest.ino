const int reed = 6;
int val = LOW;
void setup() {
  // put your setup code here, to run once:
  pinMode(reed, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println(digitalRead(reed));
}
