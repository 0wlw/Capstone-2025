#include <Arduino.h>
#include <Stepper.h>

const int stepsPerRevolution = 200;
Stepper testStepper(stepsPerRevolution, 2, 3, 4, 5);

String InBytes;

void setup() {
  Serial.begin(9600);
  testStepper.setSpeed(60);
} 

void loop() {
  if (Serial.available() > 0) {
    InBytes = Serial.readStringUntil("\n");

    if (InBytes == "on") {
      Serial.write("LED ON");
      testStepper.step(stepsPerRevolution);
    } else if (InBytes == "off") {
      digitalWrite(LED_BUILTIN, LOW);
      Serial.write("LED OFF");
    } else {
      Serial.write("Invalid");
      Serial.println(InBytes);
    }
  }
}
