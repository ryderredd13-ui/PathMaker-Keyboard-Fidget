int BUT1 = D0;

  int BUT2 = D1;

  int BUT3 = D2;

  int BUT4 = D10;


  int LED1 = D3;

  int LED2 = D4;

  int LED3 = D5;

  int LED4 = D9;
void setup() {
  

  pinMode(BUT1, INPUT_PULLUP);

  pinMode(BUT2, INPUT_PULLUP);

  pinMode(BUT3, INPUT_PULLUP);

  pinMode(BUT4, INPUT_PULLUP);


  pinMode(LED1, OUTPUT);

  pinMode(LED2, OUTPUT);

  pinMode(LED3, OUTPUT);

  pinMode(LED4, OUTPUT);

  long startTime = millis();



}

void loop() {
  long but1time;
  long but2time;
  long but3time;
  long but4time = 0;  

if (digitalRead(BUT1) == HIGH) {

but1time = millis(); digitalWrite(LED1, HIGH);
} else {

digitalWrite(LED1, LOW);
}

if (digitalRead(BUT2) == HIGH) {

but2time = millis(); digitalWrite(LED2, HIGH);
} else {

digitalWrite(LED2, LOW);
}
if (digitalRead(BUT3) == HIGH) {

but3time = millis(); digitalWrite(LED3, HIGH);
} else {

digitalWrite(LED3, LOW);
}
if (digitalRead(BUT4) == HIGH) {

but4time = millis(); digitalWrite(LED4, HIGH);
} else {

digitalWrite(LED4, LOW);
}



}