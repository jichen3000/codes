#include <SPI.h>
#include <Ethernet.h>
#include "smtp_service.h"

const unsigned int SMTP_PORT = 2525;
const unsigned int BAUD_RATE = 9600;
const String       USERNAME  = "amljaGVuMzAwMEBnbWFpbC5jb20="; // Encoded in Base64.
const String       PASSWORD  = "amljaGVuNzgwNjAy"; // Encoded in Base64.

byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
IPAddress my_ip(10, 160, 34, 161);
// IPAddress time_server(192, 43, 244, 18); // time.nist.gov
IPAddress my_dns(4, 2, 2, 1);
// Insert IP address of your cable or DSL router below:
IPAddress my_gateway(10, 160, 34, 1);

 // Insert IP address of your SMTP server below!
IPAddress smtp_server(216, 22, 15, 248);

SmtpService smtp_service(smtp_server, SMTP_PORT, USERNAME, PASSWORD);

void setup() {
  // Ethernet.begin(mac, my_ip);
  Ethernet.begin(mac, my_ip, my_dns, my_gateway); 
  Serial.begin(BAUD_RATE);
  delay(1000);
  Email email( 
    "arduino@example.com",
    "jichen3000@gmail.com",
    "For arduino test",
    "just a test email."
  );
  smtp_service.send_email(email);
}

void loop() {}
