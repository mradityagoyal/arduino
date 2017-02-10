/*
  Example for receiving
  
  https://github.com/sui77/rc-switch/
  
  If you want to visualize a telegram copy the raw data and 
  paste it into http://test.sui.li/oszi/
*/

#include <RCSwitch.h>

RCSwitch mySwitch = RCSwitch();

void setup() {
  Serial.begin(9600);
  mySwitch.enableReceive(0);  // Receiver on interrupt 0 => that is pin #2
}

void loop() {
  if (mySwitch.available()) {
    Serial.print("Value:");
    Serial.println(mySwitch.getReceivedValue());
    Serial.print("BitLength:");
    Serial.println(mySwitch.getReceivedBitlength());
    Serial.print("Delay:");
    Serial.println(mySwitch.getReceivedDelay());
    
    Serial.print("Protocol:");
    Serial.println(mySwitch.getReceivedProtocol());
    mySwitch.resetAvailable();
  }
}
