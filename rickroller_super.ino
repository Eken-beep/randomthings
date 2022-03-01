#include <DigiKeyboard.h>

void setup() {
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.sendKeyStroke(MOD_CONTROL_LEFT, KEY_T);
  DigiKeyboard.delay(50);
  DigiKeyboard.println("https://www.youtube.com/watch?v=dQw4w9WgXcQ");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
}   

void loop() {
  
}
