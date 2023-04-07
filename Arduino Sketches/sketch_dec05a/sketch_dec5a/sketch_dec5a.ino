int firstButtonState = 0;
int secondButtonState = 0;
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
  firstButtonState = digitalRead(firstButtonPin);
  secondButtonState = digitalRead(secondButtonPin);
  
  if (firstButtonState == LOW) {
    digitalWrite(ledPin, HIGH);
    Serial.println(firstButtonPin);
  } else if (secondButtonState == LOW) {
    digitalWrite(ledPin, HIGH);
    Serial.println(secondButtonPin);
  } else {
    digitalWrite(ledPin, LOW)
  }
  
}
