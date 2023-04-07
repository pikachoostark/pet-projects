void setup() {
  Serial.begin(9600);
}

void loop() {
  while (Serial.available() == 0);
  int x = Serial.parseInt();

  delay(1000);

  Serial.print(x, BIN);
  Serial.print(" ");
  Serial.print(x, OCT);
  Serial.print(" ");
  Serial.println(x, HEX);
}
