#include <Arduino.h>
#include <Stepper.h>

const int stepsPerRevolution = 200;
Stepper StepperU(stepsPerRevolution, 2, 3, 4, 5);
Stepper StepperF(stepsPerRevolution, 8, 9, 10, 11);
Stepper StepperR(stepsPerRevolution, 22, 23, 24, 25);
Stepper StepperL(stepsPerRevolution, 28, 29, 30, 31);
Stepper StepperB(stepsPerRevolution, 34, 35, 36, 37);
Stepper StepperD(stepsPerRevolution, 40, 41, 42, 43);

String InBytes;

void setup() {
  Serial.begin(9600);
  StepperU.setSpeed(60);
  StepperF.setSpeed(60);
  StepperR.setSpeed(60);
  StepperL.setSpeed(60);
  StepperD.setSpeed(60);
  StepperB.setSpeed(60);
} 

void loop() {
  if (Serial.available() > 0) {
    InBytes = Serial.readStringUntil("\n");

    if (InBytes == "U1") { ///////////////////////////
      StepperU.step(stepsPerRevolution * 0.25);
      Serial.println(InBytes);
    } else if (InBytes == "U2") {
      StepperU.step(stepsPerRevolution * 0.5);
      Serial.println(InBytes);
    } else if (InBytes == "U3") {
      StepperU.step(stepsPerRevolution * 0.75);
      Serial.println(InBytes);
    } else if (InBytes == "F1") { ///////////////////////////
      StepperF.step(stepsPerRevolution * 0.25);
      Serial.println(InBytes);
    } else if (InBytes == "F2") {
      StepperF.step(stepsPerRevolution * 0.5);
      Serial.println(InBytes);
    } else if (InBytes == "F3") {
      StepperF.step(stepsPerRevolution * 0.75);
      Serial.println(InBytes);
    } else if (InBytes == "R1") { ///////////////////////////
      StepperR.step(stepsPerRevolution * 0.25);
      Serial.println(InBytes);
    } else if (InBytes == "R2") {
      StepperR.step(stepsPerRevolution * 0.5);
      Serial.println(InBytes);
    } else if (InBytes == "R3") {
      StepperR.step(stepsPerRevolution * 0.75);
      Serial.println(InBytes);
    } else if (InBytes == "L1") { ///////////////////////////
      StepperL.step(stepsPerRevolution * 0.25);
      Serial.println(InBytes);
    } else if (InBytes == "L2") {
      StepperL.step(stepsPerRevolution * 0.5);
      Serial.println(InBytes);
    } else if (InBytes == "L3") {
      StepperL.step(stepsPerRevolution * 0.75);
      Serial.println(InBytes);
    } else if (InBytes == "B1") { ///////////////////////////
      StepperB.step(stepsPerRevolution * 0.25);
      Serial.println(InBytes);
    } else if (InBytes == "B2") {
      StepperB.step(stepsPerRevolution * 0.5);
      Serial.println(InBytes);
    } else if (InBytes == "B3") {
      StepperB.step(stepsPerRevolution * 0.75);
      Serial.println(InBytes);
    } else if (InBytes == "D1") { ///////////////////////////
      StepperD.step(stepsPerRevolution * 0.25);
      Serial.println(InBytes);
    } else if (InBytes == "D2") {
      StepperD.step(stepsPerRevolution * 0.5);
      Serial.println(InBytes);
    } else if (InBytes == "D3") {
      StepperD.step(stepsPerRevolution * 0.75);
      Serial.println(InBytes);
    }
  }
}
