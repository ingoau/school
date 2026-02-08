const int delayTime = 50;

void setup() {
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);
}

void loop() {
  for (int x = 8; x < 14; x++) {
    digitalWrite(x, HIGH);
    delay(delayTime);
    digitalWrite(x, LOW);
    delay(delayTime);
  }
  for (int x = 13; x > 7; x--) {
    digitalWrite(x, HIGH);
    delay(delayTime);
    digitalWrite(x, LOW);
    delay(delayTime);
  }
}
