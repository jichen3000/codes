#include <SPI.h> // needed in Arduino 0019 or later
#include <Ethernet.h>
#include <Twitter.h>

// The includion of EthernetDNS is not needed in Arduino IDE 1.0 or later.
// Please uncomment below in Arduino IDE 0022 or earlier.
//#include <EthernetDNS.h>

byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
IPAddress my_ip(10, 160, 34, 161);
// Insert IP address of your domain name system below: 
IPAddress my_dns(4, 2, 2, 1);
// Insert IP address of your cable or DSL router below:
IPAddress my_gateway(10, 160, 34, 1);


// Your Token to Tweet (get it from http://arduino-tweet.appspot.com/)
Twitter twitter("");

// Message to post
char msg[] = "Hello, World! I'm Arduino!";

void setup()
{
  delay(1000);
  Ethernet.begin(mac, my_ip, my_dns, my_gateway); 
  // Ethernet.begin(mac, ip);
  // or you can use DHCP for autoomatic IP address configuration.
  // Ethernet.begin(mac);
  Serial.begin(9600);
  
  Serial.println("connecting ...");
  if (twitter.post(msg)) {
    // Specify &Serial to output received response to Serial.
    // If no output is required, you can just omit the argument, e.g.
    // int status = twitter.wait();
    int status = twitter.wait(&Serial);
    if (status == 200) {
      Serial.println("OK.");
    } else {
      Serial.print("failed : code ");
      Serial.println(status);
    }
  } else {
    Serial.println("connection failed.");
  }
}

void loop()
{
}
