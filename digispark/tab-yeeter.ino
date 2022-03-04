#include <DigiKeyboard.h>

void setup() {
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.sendKeyStroke(MOD_CONTROL_LEFT, KEY_W);
}

void loop() {
  DigiKeyboard.sendKeyStroke(MOD_CONTROL_LEFT, KEY_W);
  DigiKeyboard.delay(100);
}
