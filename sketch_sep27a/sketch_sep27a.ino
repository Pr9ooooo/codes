void setup() {
  // put your setup code here, to run once:
  pinMode(13,OUTPUT);
  pinMode(15,OUTPUT);
  pinMode(18, OUTPUT);
  pinMode(14,INPUT); //button is an input device
  digitalWrite(15,LOW); //creating a virtual GND

}

void loop() {
  // put your main code here, to run repeatedly:
  if ((digitalRead(14))==HIGH){
   digitalWrite(18,HIGH); 
   digitalWrite(13,LOW);
  }
  else if ((digitalRead(14))==LOW){
    digitalWrite(13,HIGH);
    digitalWrite(18,LOW);
  }

}
//Digital Read: It reads the pin's active or non-activeness, this can be used to compare and make a wire act as a switch
