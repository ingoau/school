int potPin = A5;
int potVal = 0;

void setup() {
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);
}

void loop() {
  potVal = analogRead(potPin);

  if (potVal < 170) {
    turnOffAll();
    digitalWrite(8, HIGH);
  } else if (potVal < 170 * 2) {
    turnOffAll();
    digitalWrite(9, HIGH);
  } else if (potVal < 170 * 3) {
    turnOffAll();
    digitalWrite(10, HIGH);
  } else if (potVal < 170 * 4) {
    turnOffAll();
    digitalWrite(11, HIGH);
  } else if (potVal < 170 * 5) {
    turnOffAll();
    digitalWrite(12, HIGH);
  } else {
    turnOffAll();
    digitalWrite(13, HIGH);
  }
}

void turnOffAll() {
  digitalWrite(8, LOW);
  digitalWrite(9, LOW);
  digitalWrite(10, LOW);
  digitalWrite(11, LOW);
  digitalWrite(12, LOW);
  digitalWrite(13, LOW);
}
