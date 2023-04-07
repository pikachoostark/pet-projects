String my_str;

void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    my_str = Serial.readString();
    Serial.println(my_str);
  }
}
