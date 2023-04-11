#include <HX711.h>

// Initialize the HX711 library with the DT and SCK pin numbers
HX711 hx711(A0, A1);

// Initialize the relay module pin numbers
int relay1 = 2;
int relay2 = 3;
int relay3 = 4;
int relay4 = 5;

// Initialize the weight threshold and the counter
float threshold = 50; // in grams
int count = 0;

void setup() {
  // Set the relay module pins as outputs
  pinMode(relay1, OUTPUT);
  pinMode(relay2, OUTPUT);
  pinMode(relay3, OUTPUT);
  pinMode(relay4, OUTPUT);

  // Start the HX711 library and set the gain to 128
  hx711.begin();
  hx711.set_gain(128);
}

void loop() {
  // Read the weight from the HX711
  float weight = hx711.get_units();

  // If the weight is above the threshold, turn on the relays and increment the counter
  if (weight > threshold) {
    digitalWrite(relay1, HIGH);
    digitalWrite(relay2, HIGH);
    digitalWrite(relay3, HIGH);
    digitalWrite(relay4, HIGH);
    count++;
  }
  // Otherwise, turn off the relays
  else {
    digitalWrite(relay1, LOW);
    digitalWrite(relay2, LOW);
    digitalWrite(relay3, LOW);
    digitalWrite(relay4, LOW);
  }

  // Print the weight and the counter to the serial monitor
  Serial.print("Weight: ");
  Serial.print(weight);
  Serial.print(" g, Count: ");
  Serial.println(count);

  // Wait for 500 milliseconds before taking the next measurement
  delay(500);
}

