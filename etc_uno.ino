#include <Wire.h>
#include <Adafruit_MCP4725.h>

Adafruit_MCP4725 dac0;
Adafruit_MCP4725 dac1;
char msg[256];

void setup(void) {
  Serial.begin(9600);
  Serial.println("Hello!");
  dac0.begin(0x62);
  dac1.begin(0x63);
  Serial.println("Generating a triangle wave");
}

void set_position_percent(float pos) {
  if (pos > 100.0)
    pos = 100.0;
  if (pos < 0.0)
    pos = 0.0;
  pos = pos / 100.0;
  int dac1val = floor(pos * 4095);
  dac1.setVoltage(dac1val,false);
  dac0.setVoltage(4095-dac1val,false);
}

void loop(void) {
  if (Serial.available()) {
    char etcval = Serial.read();
    set_position_percent(etcval*1.0);
    sprintf(msg,"Setting ETC position to %d\n",etcval);
    Serial.print(msg);
  }
}
