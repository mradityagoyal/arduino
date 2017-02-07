
/**
 *  Circuit and code to control a RGB LED. 
 *  https://circuits.io/circuits/3928830-the-unnamed-circuit/edit#breadboard
 */

#include "Arduino.h"

int RED_PIN = 7;
int BLUE_PIN = 6;
int GREEN_PIN = 5;


void setup() {
  pinMode(RED_PIN, OUTPUT);
  pinMode(BLUE_PIN, OUTPUT);
  pinMode(GREEN_PIN, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:

  setColor(255,0,0);
  delay(1000);

  setColor(0,255,0);
  delay(1000);

  setColor(0,0,255);
  delay(1000);


}

void setColor(int red, int green, int blue){

  #ifdef COMMON_ANODE
    red = 255 - red;
    green = 255 - green;
    blue = 255 - blue;
  #endif
  analogWrite(RED_PIN, red);
  analogWrite(GREEN_PIN, green);
  analogWrite(BLUE_PIN, blue);  
  
}

