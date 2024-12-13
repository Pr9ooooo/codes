void setup() {
  // put your setup code here, to run once:
  pinMode(2,OUTPUT);
  Serial.begin(57600);
}

void loop() {
  // put your main code here, to run repeatedly:
 char ch
 while(Serial.available()>0){
  ch=Serial.read()
  if (ch=="i"){
   Serial.print("LED IS ON NOW");
   digitalWrite(2,HIGH);
  }
  else if (ch=="No"){
   Serial.print("LED IS OFF NOW");
   digitalWrite(2,LOW)
  }
 }
}

