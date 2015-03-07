import processing.serial.*;

final float MAX_WORKING_TEMP = 20.0;
final int LINE_FEED = 10;
final int BAUD_RATE = 9600;
final int FONT_SIZE = 32;
final int WIDTH = 320;
final int HEIGHT = 240;
final String API_KEY = "";
final String API_SECRET = "";
final String ACCESS_TOKEN = "";
final String ACCESS_TOKEN_SECRET = "";

Serial _arduinoPort;
float _temperature;
boolean _isCelsius;
PFont _font;

void setup() {
  size(WIDTH, HEIGHT);
  _font = createFont("Arial", FONT_SIZE, true);
  println(Serial.list());
  _arduinoPort = new Serial(this, Serial.list()[0], BAUD_RATE);
  _arduinoPort.clear();
  _arduinoPort.bufferUntil(LINE_FEED);
  _arduinoPort.readStringUntil(LINE_FEED);
}

void draw() {
  background(255);
  fill(0);
  textFont(_font, FONT_SIZE);
  textAlign(CENTER, CENTER);
  if (_isCelsius)
    text(_temperature + " \u2103", WIDTH / 2, HEIGHT / 2);
  else 
    text(_temperature + " \u2109", WIDTH / 2, HEIGHT / 2);
} 


Arduino: 1.6.0 (Mac OS X), Board: "Arduino Uno"

Build options changed, rebuilding all
TweetTemperature.pde:4:18: error: variable or field 'serialEvent' declared void
TweetTemperature.pde:4:25: error: expected ')' before 'port'
TweetTemperature.pde:1:1: error: 'import' does not name a type
TweetTemperature.pde:3:1: error: 'final' does not name a type
TweetTemperature.pde:4:1: error: 'final' does not name a type
TweetTemperature.pde:5:1: error: 'final' does not name a type
TweetTemperature.pde:6:1: error: 'final' does not name a type
TweetTemperature.pde:7:1: error: 'final' does not name a type
TweetTemperature.pde:8:1: error: 'final' does not name a type
TweetTemperature.pde:9:1: error: 'final' does not name a type
TweetTemperature.pde:10:1: error: 'final' does not name a type
TweetTemperature.pde:11:1: error: 'final' does not name a type
TweetTemperature.pde:12:1: error: 'final' does not name a type
TweetTemperature.pde:14:1: error: 'Serial' does not name a type
TweetTemperature.pde:17:1: error: 'PFont' does not name a type
TweetTemperature.pde: In function 'void setup()':
TweetTemperature.pde:20:8: error: 'WIDTH' was not declared in this scope
TweetTemperature.pde:20:15: error: 'HEIGHT' was not declared in this scope
TweetTemperature.pde:20:21: error: 'size' was not declared in this scope
TweetTemperature.pde:21:3: error: '_font' was not declared in this scope
TweetTemperature.pde:21:31: error: 'FONT_SIZE' was not declared in this scope
TweetTemperature.pde:21:46: error: 'createFont' was not declared in this scope
TweetTemperature.pde:22:18: error: 'class HardwareSerial' has no member named 'list'
TweetTemperature.pde:22:24: error: 'println' was not declared in this scope
TweetTemperature.pde:23:3: error: '_arduinoPort' was not declared in this scope
TweetTemperature.pde:23:22: error: expected type-specifier before 'Serial'
TweetTemperature.pde:23:22: error: expected ';' before 'Serial'
TweetTemperature.pde:25:28: error: 'LINE_FEED' was not declared in this scope
TweetTemperature.pde: In function 'void draw()':
TweetTemperature.pde:30:17: error: 'background' was not declared in this scope
TweetTemperature.pde:31:9: error: 'fill' was not declared in this scope
TweetTemperature.pde:32:12: error: '_font' was not declared in this scope
TweetTemperature.pde:32:19: error: 'FONT_SIZE' was not declared in this scope
TweetTemperature.pde:32:28: error: 'textFont' was not declared in this scope
TweetTemperature.pde:33:13: error: 'CENTER' was not declared in this scope
TweetTemperature.pde:33:27: error: 'textAlign' was not declared in this scope
TweetTemperature.pde:35:25: error: invalid operands of types 'float' and 'const char [5]' to binary 'operator+'
TweetTemperature.pde:35:36: error: 'WIDTH' was not declared in this scope
TweetTemperature.pde:35:47: error: 'HEIGHT' was not declared in this scope
TweetTemperature.pde:35:57: error: 'text' was not declared in this scope
TweetTemperature.pde:37:25: error: invalid operands of types 'float' and 'const char [5]' to binary 'operator+'
TweetTemperature.pde:37:36: error: 'WIDTH' was not declared in this scope
TweetTemperature.pde:37:47: error: 'HEIGHT' was not declared in this scope
TweetTemperature.pde:37:57: error: 'text' was not declared in this scope
TweetTemperature.pde: At global scope:
TweetTemperature.pde:40:18: error: variable or field 'serialEvent' declared void
TweetTemperature.pde:40:25: error: expected ')' before 'port'
Error compiling.

  This report would have more information with
  "Show verbose output during compilation"
  enabled in File > Preferences.
