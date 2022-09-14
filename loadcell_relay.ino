#include <HX711_ADC.h> // https://github.com/olkal/HX711_ADC
#include <Wire.h>
#include <LiquidCrystal_I2C.h> // LiquidCrystal_I2C library

HX711_ADC LoadCell(4, 5); // parameters: dt pin, sck pin<span data-mce-type="bookmark" style="display: inline-block; width: 0px; overflow: hidden; line-height: 0;" class="mce_SELRES_start"></span>
LiquidCrystal_I2C lcd(0x27, 16, 2); // 0x27 is the i2c address of the LCM1602 IIC v1 module (might differ)

int Relay = 9;
int val;

void setup()
{
  LoadCell.begin(); // start connection to HX711
  LoadCell.start(2000); // load cells gets 2000ms of time to stabilize
  LoadCell.setCalFactor(968.303); // calibration factor for load cell => strongly dependent on your individual setup
  lcd.init();//begin(); // begins connection to the LCD module
  lcd.backlight(); // turns on the backlight
  pinMode(13, OUTPUT);
  pinMode(Relay, OUTPUT);   // it was missing in your sketch
}
void loop()
{
  LoadCell.update(); // retrieves data from the load cell
  float i = LoadCell.getData(); // get output value ; 
  int wt = (int)i;
  lcd.setCursor(0, 0); // set cursor to first row
  lcd.print("Weight[g]:"); // print out to LCD
  lcd.setCursor(0, 1); // set cursor to secon row
  lcd.print(i); // print out the retrieved value to the second row
  //---------------------------------------
  if (wt < 100)
  {
    digitalWrite(Relay, HIGH);
  }

  if (wt > 100 && wt < 500)
  {
    digitalWrite(Relay, HIGH);
    delay(15000);
    digitalWrite(Relay, LOW);
  }

  if (wt > 500)
  {
    digitalWrite(Relay, HIGH);
    delay(30000);
    digitalWrite(Relay, LOW);
  }
}
