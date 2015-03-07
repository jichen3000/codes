const unsigned int LED_BIT_0 = 12;
const unsigned int LED_BIT_1 = 10;
const unsigned int LED_BIT_2 = 8;

void setup() {
    pinMode(LED_BIT_0, OUTPUT);
    pinMode(LED_BIT_1, OUTPUT);
    pinMode(LED_BIT_2, OUTPUT);

    randomSeed(analogRead(A0));
    long result = random(1, 7);
    output_result(result);
}

void loop() {

}

void output_result(const long result){
    digitalWrite(LED_BIT_0, result & B001);
    digitalWrite(LED_BIT_1, result & B010);
    digitalWrite(LED_BIT_2, result & B100);
}