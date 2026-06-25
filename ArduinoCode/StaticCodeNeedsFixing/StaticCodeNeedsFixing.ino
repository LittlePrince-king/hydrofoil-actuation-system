#include <Servo.h>

Servo myservo;

// --- EDIT THIS ---
int targetAngle = 180;   // where you want it to go
float speedDegPerStep = 1.0; // how fast it moves (deg per update)
// ------------------

float currentAngle = 0; // tracked continuously

void setup() {
  myservo.attach(9);
  currentAngle = myservo.read(); // initialize from servo
}

void loop() {

  // Move toward target
  if (currentAngle < targetAngle) {
    currentAngle += speedDegPerStep;
    if (currentAngle > targetAngle) currentAngle = targetAngle;
  }
  else if (currentAngle > targetAngle) {
    currentAngle -= speedDegPerStep;
    if (currentAngle < targetAngle) currentAngle = targetAngle;
  }

  myservo.write(currentAngle);

  delay(10); // smooth update
}
