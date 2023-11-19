#include <MeMCore.h>
#include <Arduino.h>

MeDCMotor motor1(M1);
MeDCMotor motor2(M2);

MePort port(PORT_1);
Servo servo1;  // create servo object to control a servo 
int16_t servo1Pin =  port.pin1();//attaches the servo on PORT_3 SLOT1 to the servo object



char input;

uint8_t motorSpeed = 120;

void setup() {
  Serial.begin(115200);
  servo1.attach(servo1Pin); // attaches the servo on port 1 pin 2 to the servo object
  servo1.write(165);
}

void loop() {
  // Serial.println(millis());
  
  if(Serial.available()) {
    char charArr[20];
    size_t serialIn = Serial.readBytes(charArr, 20);
    
    char inputChar = charArr[0]; //convert to string so that it compares to stuff correctly cuz char datatype != string datatype

    Serial.print("inputChar: \"");
    Serial.print(inputChar);
    Serial.println("\"");

    if (inputChar == 'w') {
      Serial.println("forward");
      motor1.run(-motorSpeed);
      motor2.run(motorSpeed);
    }
    else if (inputChar == 'e') {
      while (Serial.available() == 0) {
        Serial.println("wiggle");
        motor1.run(-motorSpeed/2);
        motor2.run(motorSpeed);
        delay(250);
        motor1.run(-motorSpeed);
        motor2.run(motorSpeed);
        delay(200);
        motor1.run(-motorSpeed);
        motor2.run(motorSpeed/2);
        delay(200);
        motor1.run(-motorSpeed);
        motor2.run(motorSpeed);
        delay(200);
      }
      motor1.stop();
      motor2.stop();
    }
    else if (inputChar == 's') {
      Serial.println("backward");
      motor1.run(motorSpeed);
      motor2.run(-motorSpeed);
    }
    else if (inputChar == 'a') {
      Serial.println("turn left");
      motor1.run(motorSpeed);
      motor2.run(motorSpeed);
    }
    else if (inputChar == 'd') {
      Serial.println("turn right");
      motor1.run(-motorSpeed);
      motor2.run(-motorSpeed);
    }
    else if (inputChar == 'q') {
      Serial.println("stop");
      motor1.stop();
      motor2.stop();
    }
    else if (inputChar == 'r') {
      Serial.println("slight forward");
      motor1.run(-motorSpeed);
      motor2.run(motorSpeed);
      delay(300);
      motor1.stop();
      motor2.stop();
    }
    // difference of 45 between each value
    else if (inputChar == '0') {
      Serial.println("servo back 0");
      servo1.write(0);
    }
    else if (inputChar == '1') {
      Serial.println("servo back 45");
      servo1.write(45);
    }
    else if (inputChar == '2') {
      Serial.println("servo high 100");
      servo1.write(100);
    }
    else if (inputChar == '3') {
      Serial.println("servo front 135");
      servo1.write(135);
    }
    else if (inputChar == '4') {
      Serial.println("servo front 165");
      servo1.write(165);
    }
    else if (inputChar == '5') {
      Serial.println("servo front 180");
      servo1.write(180);
    }
    else {
      Serial.println("invalid input");
    }
    
  }
}

