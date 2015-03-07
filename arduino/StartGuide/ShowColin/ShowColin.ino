const unsigned int LED_PIN = 13; 
const unsigned int ONE_UNIT = 500;
const unsigned int THREE_UNIT = 1500;
const unsigned int SEVEN_UNIT = 3500;

void setup() {
  // put your setup code here, to run once:
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(LED_PIN, HIGH);
  delay(SEVEN_UNIT);
  worldSpace();

  chrC();
  letterSpace();
  chrO();
  letterSpace();
  chrL();
  letterSpace();
  chrI();
  letterSpace();
  chrN();

  worldSpace();

  chrJ();
  letterSpace();
  chrI();
}

void morseDot(){
  digitalWrite(LED_PIN, HIGH);
  delay(ONE_UNIT);
  digitalWrite(LED_PIN, LOW);
  delay(ONE_UNIT);
}

void morseDash(){
  digitalWrite(LED_PIN, HIGH);
  delay(THREE_UNIT);
  digitalWrite(LED_PIN, LOW);
  delay(ONE_UNIT);
}

void letterSpace(){
  digitalWrite(LED_PIN, LOW);
  delay(THREE_UNIT);
}

void worldSpace(){
  digitalWrite(LED_PIN, LOW);
  delay(SEVEN_UNIT);
}

void chrC(){
  for ( int i=0; i<2; i++){
    morseDash();
    morseDot();
  }
}

void chrO(){
  for ( int i=0; i<3; i++){
    morseDash();
  }
}

void chrL(){
  morseDot();
  morseDash();
  morseDot();
  morseDot();
}

void chrI(){
  for ( int i=0; i<2; i++){
    morseDot();
  }
}

void chrN(){
  morseDash();
  morseDot();
}

void chrJ(){
  morseDot();
  for ( int i=0; i<3; i++){
    morseDash();
  }
}
