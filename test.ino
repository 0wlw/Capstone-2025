// Include the Arduino Stepper Library
#include <Stepper.h>

// Number of steps per output rotation
const int stepsPerRevolution = 200;
int received = 0;
float multiplier = 0;


// Create Instance of Stepper library
Stepper StepperF(stepsPerRevolution, 2, 3, 4, 5); // 11 12 13

void setup()
{
	// set the speed at 60 rpm: == 1 rps
	StepperF.setSpeed(60);
	// initialize the serial port:
	Serial.begin(9600);
}

void loop() 
{
  multiplier = 0;
  received = 0;

  if (Serial.available()) {
    received = Serial.readString().toInt();
    Serial.println(received);
  }
  if (received != 0) {
    Serial.println(received);
    
    if (received == 11) {
      multiplier = 0.25;
    } else if (received == 12) {
      multiplier = 0.5;
    } else if (received == 13) {
      multiplier = 0.75;
    }

    StepperF.step(stepsPerRevolution * multiplier);
  }

  delay(1000);
}
