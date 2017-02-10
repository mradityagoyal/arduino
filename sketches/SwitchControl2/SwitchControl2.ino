#include <Firmata.h>

byte analogPin;

void stringCallback(char *myString)
{
  for(byte i=0;i<50;i++){
    digitalWrite(13, HIGH);
    delay(50);
    digitalWrite(12, LOW);
    delay(50);
  }
  Firmata.sendString(myString);
}


void sysexCallback(byte command, byte argc, byte*argv)
{
    digitalWrite(13, HIGH);
    Serial.print((unsigned char)START_SYSEX);
    Serial.print((unsigned char)command);
    for (byte i=0; i<argc; i++) {
        Serial.print((unsigned char)argv[i]);
    }
    Serial.print((unsigned char)END_SYSEX);
    delay(100);
    digitalWrite(12, LOW);
}

void setup()
{
    pinMode(13, OUTPUT);
    Firmata.setFirmwareVersion(FIRMATA_FIRMWARE_MAJOR_VERSION, FIRMATA_FIRMWARE_MINOR_VERSION);
    Firmata.attach(STRING_DATA, stringCallback);
    Firmata.attach(START_SYSEX, sysexCallback);
    Firmata.begin(57600);
}

void loop()
{
    while(Firmata.available()) {
        Firmata.processInput();
    }
}
