#include <Arduino.h>

String InBytes;

void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
} 

void loop() {
  if (Serial.available() > 0) {
    InBytes = Serial.readStringUntil("\n");

    if (InBytes == "on") {
      digitalWrite(LED_BUILTIN, HIGH);
      Serial.write("LED ON");
    } else if (InBytes == "off") {
      digitalWrite(LED_BUILTIN, LOW);
      Serial.write("LED OFF");
    } else {
      Serial.write("Invalid");
      Serial.println(InBytes);
    }
  }
}
