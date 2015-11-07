#include "telegraph.h"
const unsigned int BAUD_RATE = 9600; 
const unsigned int SPEAKER_OUTPUT_PIN = 12; 
const unsigned int LED_OUTPUT_PIN = 10; 
const unsigned int DIT_LENGTH = 75;

#define SPEAKER_NOTE  1397

void led_output_symbol(const int length) {
    digitalWrite(LED_OUTPUT_PIN, HIGH);
    delay(length);
    digitalWrite(LED_OUTPUT_PIN, LOW);
}

void speaker_output_symbol(const int length) {
    tone(SPEAKER_OUTPUT_PIN, SPEAKER_NOTE, length*1);
    delay(length*1);
    noTone(SPEAKER_OUTPUT_PIN);
}

Telegraph telegraph(DIT_LENGTH);

void setup() { 
    Serial.begin(BAUD_RATE);
    telegraph.subscribe_output(speaker_output_symbol);
    telegraph.subscribe_output(led_output_symbol);
}

void loop() {
    telegraph.send_message("Hello, world!");
    delay(5000);
}