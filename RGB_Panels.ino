// NeoPixel Ring simple sketch (c) 2013 Shae Erisson
// released under the GPLv3 license to match the rest of the AdaFruit NeoPixel library

#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
#include <avr/power.h>
#endif

// Which pin on the Arduino is connected to the NeoPixels?
// On a Trinket or Gemma we suggest changing this to 1
#define PIN            6

// How many NeoPixels are attached to the Arduino?
#define NUMPIXELS      60

// When we setup the NeoPixel library, we tell it how many pixels, and which pin to use to send signals.
// Note that for older NeoPixel strips you might need to change the third parameter--see the strandtest
// example for more information on possible values.
Adafruit_NeoPixel pixels = Adafruit_NeoPixel(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

int data;

void setup() { 
  Serial.begin(9600); //initialize serial COM at 9600 baudrate
  pinMode(LED_BUILTIN, OUTPUT); //make the LED pin (13) as output
  digitalWrite (LED_BUILTIN, LOW);
  
  pixels.begin(); // This initializes the NeoPixel library.

  // Starts at stick.  First four for Star Citizen Logo
  
  pixels.setPixelColor(0, pixels.Color(150,150,150));
  pixels.setPixelColor(1, pixels.Color(150,150,150));
  pixels.setPixelColor(2, pixels.Color(150,150,150));
  pixels.setPixelColor(3, pixels.Color(150,150,150));

  // Scanning title
  pixels.setPixelColor(4, pixels.Color(50,50,50));
  pixels.setPixelColor(5, pixels.Color(50,50,50));
  pixels.setPixelColor(6, pixels.Color(50,50,50));
  pixels.setPixelColor(7, pixels.Color(50,50,50));
  
  // Scan Mode
  pixels.setPixelColor(8, pixels.Color(255,0,0));
  
  //Scan
  pixels.setPixelColor(9, pixels.Color(255,0,0));

  // Weapon Title
  pixels.setPixelColor(10, pixels.Color(0,50,0));
  pixels.setPixelColor(11, pixels.Color(0,50,0));
  pixels.setPixelColor(12, pixels.Color(0,50,0));
  pixels.setPixelColor(13, pixels.Color(0,50,0));
  
  // Guns
  pixels.setPixelColor(14, pixels.Color(0,200,0));

  // Missile 
  pixels.setPixelColor(15, pixels.Color(0,255,0));

  //Exterior Title
  pixels.setPixelColor(16, pixels.Color(50,0,0));
  pixels.setPixelColor(17, pixels.Color(50,0,0));
  pixels.setPixelColor(18, pixels.Color(50,0,0));
  pixels.setPixelColor(19, pixels.Color(50,0,0));
  
  // Landing Gear
  pixels.setPixelColor(20, pixels.Color(50,0,0));

  // Door Lock
  pixels.setPixelColor(21, pixels.Color(0,50,0));
  pixels.setPixelColor(22, pixels.Color(0,50,0));
  
  //Cargo Ramp
  pixels.setPixelColor(23, pixels.Color(255,0,0));

  //Self Destruct
  pixels.setPixelColor(24, pixels.Color(255,0,0));
  pixels.setPixelColor(25, pixels.Color(255,0,0));
  pixels.setPixelColor(26, pixels.Color(255,0,0));
  
  //ESP
  pixels.setPixelColor(27, pixels.Color(255,0,0));

  
  
  
  
  
  pixels.show();
}
 
void loop() {

  
    if (Serial.available()) {
        char serialListener = Serial.read();
        if (serialListener == 'L') {
            pixels.setPixelColor(59, pixels.Color(0,100,0));
            pixels.show();
        }
        else if (serialListener == 'H') {
            pixels.setPixelColor(59, pixels.Color(100,0,0));
            pixels.show();
        }
    }
}
