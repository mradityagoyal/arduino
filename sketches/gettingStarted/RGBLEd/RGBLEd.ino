
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

  int flag = 0;
  while(true){
    analogWrite(RED_PIN, 255);
    analogWrite(GREEN_PIN, 0);
    analogWrite(BLUE_PIN, 0);
    delay(1000);
    if(flag <= 0){
      analogWrite(GREEN_PIN, 255);
      delay(1000);
      flag++;
    }
    else{
      analogWrite(BLUE_PIN, 255);
      delay(1000);
      flag--;
    }
  }
  


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

