// I stole some of this code
// It uses buttons to buzz the buzzer or smth

/*
  Button

  Turns on and off a light emitting diode(LED) connected to digital pin 13,
  when pressing a pushbutton attached to pin 2.

  The circuit:
  - LED attached from pin 13 to ground through 220 ohm resistor
  - pushbutton attached to pin 2 from +5V
  - 10K resistor attached to pin 2 from ground

  - Note: on most Arduinos there is already an LED on the board
    attached to pin 13.

  created 2005
  by DojoDave <http://www.0j0.org>
  modified 30 Aug 2011
  by Tom Igoe

  This example code is in the public domain.

  https://docs.arduino.cc/built-in-examples/digital/Button/
*/

// constants won't change. They're used here to set pin numbers:
const int button1Pin = 6;  // the number of the pushbutton pin
const int button2Pin = 7;  // the number of the pushbutton pin
const int ledPin = 8;    // the number of the LED pin
const int buzzer = 3;

// variables will change:
int button1State = 0;  // variable for reading the pushbutton status
int button2State = 0;  // variable for reading the pushbutton status

void setup() {
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
  // initialize the pushbutton pin as an input:
  pinMode(button1Pin, INPUT);
  pinMode(button2Pin, INPUT);
  pinMode(buzzer, OUTPUT);
}

void loop() {
  // read the state of the pushbutton value:
  button1State = digitalRead(button1Pin);
  button2State = digitalRead(button2Pin);

  // check if the pushbutton is pressed. If it is, the buttonState is HIGH:
  if (button1State == HIGH) {
    // turn LED on:
    tone(buzzer, 500);
  } else if (button2State == HIGH) {
    // turn LED on:
    tone(buzzer, 1000);
  } else {
    // turn LED off:
    noTone(buzzer);
  }
}
