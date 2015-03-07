#include <SPI.h>
#include <Ethernet.h>
const unsigned int BAUD_RATE = 9600;
const unsigned int DAYTIME_PORT = 13;

byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
IPAddress my_ip(10, 160, 34, 161);
// IPAddress time_server(192, 43, 244, 18); // time.nist.gov
IPAddress time_server(24, 56, 178, 140); // time.nist.gov
// Insert IP address of your domain name system below: 
IPAddress my_dns(4, 2, 2, 1);
// Insert IP address of your cable or DSL router below:
IPAddress my_gateway(10, 160, 34, 1);
EthernetClient client; 

void setup() {
  Serial.begin(BAUD_RATE);
  Ethernet.begin(mac, my_ip, my_dns, my_gateway); 
}

void loop() {
  delay(1000);
  Serial.print("Connecting...");
  
  if (client.connect(time_server, DAYTIME_PORT) <= 0) { 
    Serial.println("connection failed.");
  } else {
    Serial.println("connected.");
    delay(1000);
    while (client.available()) {
      char c = client.read();
      Serial.print(c);
    }
    
    Serial.println("Disconnecting.");
    client.stop();
  }
}

