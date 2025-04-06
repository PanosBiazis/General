//C++
int Red=0;
int Orange=1;
int Green=2;
int Red2=3;
int Orange2=4;
int Green2=5;
void setup() {
  // put your setup code here, to run once:
  pinMode(Red,OUTPUT);
  pinMode(Orange,OUTPUT);
  pinMode(Green,OUTPUT);
  pinMode(Red2,OUTPUT);
  pinMode(Orange2,OUTPUT);
  pinMode(Green2,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(Red,HIGH);
  digitalWrite(Orange,LOW);
  digitalWrite(Green,LOW);
  digitalWrite(Red2,LOW);
  digitalWrite(Orange2,LOW);
  digitalWrite(Green2,HIGH);
  delay(5000);
  digitalWrite(Red,HIGH);
  digitalWrite(Orange,LOW);
  digitalWrite(Green,LOW);
  digitalWrite(Red2,LOW);
  digitalWrite(Orange2,HIGH);
  digitalWrite(Green2,LOW);
  delay(500);
  digitalWrite(Red,HIGH);
  digitalWrite(Orange,LOW);
  digitalWrite(Green,LOW);
  digitalWrite(Red2,HIGH);
  digitalWrite(Orange2,LOW);
  digitalWrite(Green2,LOW);
  delay(500);
  digitalWrite(Red,LOW);
  digitalWrite(Orange,LOW);
  digitalWrite(Green,HIGH);
  digitalWrite(Red2,HIGH);
  digitalWrite(Orange2,LOW);
  digitalWrite(Green2,LOW);
  delay(5000);
  digitalWrite(Red,LOW);
  digitalWrite(Orange,HIGH);
  digitalWrite(Green,LOW);
  digitalWrite(Red2,HIGH);
  digitalWrite(Orange2,LOW);
  digitalWrite(Green2,LOW);
  delay(500);
  digitalWrite(Red,HIGH);
  digitalWrite(Orange,LOW);
  digitalWrite(Green,LOW);
  digitalWrite(Red2,HIGH);
  digitalWrite(Orange2,LOW);
  digitalWrite(Green2,LOW);
  delay(5000);
}