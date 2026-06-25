#include <Servo.h>
#include <math.h>

Servo myservo;

// --- EDIT THESE VALUES ---
int minAngle = 20;        // DO NOT USE 0°
int maxAngle = 40;       // DO NOT USE 180°
float timeBetween = 1000; // ms from min → max (half cycle)
// -------------------------

void setup() {
  myservo.attach(9);
}

void loop() {
  unsigned long t = millis();

  float mid = (minAngle + maxAngle) * 0.5;
  float amp = (maxAngle - minAngle) * 0.5;

  float period = 2.0 * timeBetween;
  float theta = (2.0 * PI * t) / period;

  float angle = mid + amp * sin(theta);

  myservo.write(angle);
}
