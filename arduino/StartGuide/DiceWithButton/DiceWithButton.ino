const unsigned int LED_BIT_0 = 12;
const unsigned int LED_BIT_1 = 10;
const unsigned int LED_BIT_2 = 8;
const unsigned int BUTTON_PIN = 7;

void setup() {
    pinMode(LED_BIT_0, OUTPUT);
    pinMode(LED_BIT_1, OUTPUT);
    pinMode(LED_BIT_2, OUTPUT);
    pinMode(BUTTON_PIN, INPUT);

    randomSeed(analogRead(A0));
    // long result = random(1, 7);
    // output_result(result);
}

int current_value = 0;
int old_value = 0;
void loop() {
    current_value = digitalRead(BUTTON_PIN);
    if (current_value != old_value 
            && current_value == HIGH){
        output_result(random(1, 7));
        delay(50);
    }
    old_value = current_value;

}

void output_result(const long result){
    digitalWrite(LED_BIT_0, result & B001);
    digitalWrite(LED_BIT_1, result & B010);
    digitalWrite(LED_BIT_2, result & B100);
}