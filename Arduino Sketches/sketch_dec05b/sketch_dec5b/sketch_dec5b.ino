int firstButtonState = 1;
int secondButtonState = 1;
const int ledPin = 13;
const int firstButtonPin = 14;
const int secondButtonPin = 16;

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
  pinMode(firstButtonPin, INPUT_PULLUP);
  pinMode(secondButtonPin, INPUT_PULLUP);
}

void loop() {
  if (firstButtonState != digitalRead(firstButtonPin)) {
    // firstButtonState = digitalRead(firstButtonPin);
    digitalWrite(ledPin, HIGH);
    Serial.println(firstButtonPin);
  } else if (secondButtonState != digitalRead(secondButtonPin)) {
    // secondButtonState = digitalRead(secondButtonPin);
    digitalWrite(ledPin, HIGH);
    Serial.println(secondButtonPin);
  } else {
    digitalWrite(ledPin, LOW);
  }

  firstButtonState = digitalRead(firstButtonPin);
  secondButtonState = digitalRead(secondButtonPin);
}
