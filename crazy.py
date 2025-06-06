#include <Stepper.h>

const int stepsPerRevolution = 200;

int received = 0;

Stepper stepperU(stepsPerRevolution, 2, 3, 4, 5);
Stepper stepperF(stepsPerRevolution, 8, 9, 10, 11);
Stepper stepperL(stepsPerRevolution, 22, 23, 24, 25);
Stepper stepperR(stepsPerRevolution, 28, 29, 30, 31);
Stepper stepperB(stepsPerRevolution, 34, 35, 36, 37);
Stepper stepperD(stepsPerRevolution, 40, 41, 42, 43);

void setup() {
  Serial.begin(9600);
  stepperU.setSpeed(60);
  stepperF.setSpeed(60);
  stepperL.setSpeed(60);
  stepperR.setSpeed(60);
  stepperB.setSpeed(60);
  stepperD.setSpeed(60);
}

void loop() {
  while (!Serial.available());
  received = Serial.readString().toInt();
  if (received == 11) {
    stepperU.step(0.25 * stepsPerRevolution);
  } else if (received == 21) {
    stepperF.step(0.25 * stepsPerRevolution);
  } else if (received == 31) {
    stepperL.step(0.25 * stepsPerRevolution);
  } else if (received == 41) {
    stepperR.step(0.25 * stepsPerRevolution);
  } else if (received == 51) {
    stepperB.step(0.25 * stepsPerRevolution);
  } else if (received == 61) {
    stepperD.step(0.25 * stepsPerRevolution);
  } else if (received == 12) { /////////////////////////////////////////////
    stepperU.step(0.5 * stepsPerRevolution);
  } else if (received == 22) {
    stepperF.step(0.5 * stepsPerRevolution);
  } else if (received == 32) {
    stepperL.step(0.5 * stepsPerRevolution);
  } else if (received == 42) {
    stepperR.step(0.5 * stepsPerRevolution);
  } else if (received == 52) {
    stepperB.step(0.5 * stepsPerRevolution);
  } else if (received == 62) {
    stepperD.step(0.5 * stepsPerRevolution);
  } else if (received == 13) { ///////////////////////////////////////
    stepperU.step(0.75 * stepsPerRevolution);
  } else if (received == 23) {
    stepperF.step(0.75 * stepsPerRevolution);
  } else if (received == 33) {
    stepperL.step(0.75 * stepsPerRevolution);
  } else if (received == 43) {
    stepperR.step(0.75 * stepsPerRevolution);
  } else if (received == 53) {
    stepperB.step(0.75 * stepsPerRevolution);
  } else if (received == 63) {
    stepperD.step(0.75 * stepsPerRevolution);
  }
  received = 0;
  delay(1000);
}
