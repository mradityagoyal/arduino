/*
  Example for different sending methods
  
  https://github.com/sui77/rc-switch/
  
*/

#include <RCSwitch.h>

RCSwitch mySwitch = RCSwitch();

void setup() {

  Serial.begin(9600);
  
  // Transmitter is connected to Arduino Pin #12  
  mySwitch.enableTransmit(12);

  pinMode(LED_BUILTIN, OUTPUT);

  // Optional set pulse length.
   mySwitch.setPulseLength(170);
  
  // Optional set protocol (default is 1, will work for most outlets)
  // mySwitch.setProtocol(2);
  
  // Optional set number of transmission repetitions.
//   mySwitch.setRepeatTransmit(2);
  
}

void loop() {
  /* Same switch as above, but using decimal code */
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);
  mySwitch.switchOff("11111", "00010");
  mySwitch.send(12047364, 24);
  digitalWrite(LED_BUILTIN, HIGH);
  delay(3000);  
   mySwitch.switchOff("11111", "00010");
  mySwitch.send(12047372, 24);
   delay(3000);
  
 
}
