#include <Servo.h>

Servo myServo;

void setup() {
  myServo.attach(9);  // Assuming the servo is connected to pin 9
  Serial.begin(9600);
  myServo.write(0);
}

void loop() {
  
  if (Serial.available() > 1)
   {
    int roll = Serial.parseInt();
    int c = myServo.read();
    //myServo.write(c);
    delay(1000);

    for (int pos = c; pos <= roll; pos += 1) { 
    delay(1000); // goes from 0 degrees to 180 degrees
    myServo.write(pos);              // tell servo to go to position in variable 'pos' 
  }
    Serial.flush();  // Clear the serial buffer
  }
}
