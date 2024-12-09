#include <WiFi.h>
#include <WiFiUdp.h>

#define LIGHT_SENSOR_PIN 36 // ESP32 pin GPIO36 (ADC0)

// WiFi credentials
const char* ssid = "pi";
const char* password = "123123123";

// Raspberry Pi UDP server details
const char* serverIP = "192.168.137.209";  // Replace with your Raspberry Pi IP address
const int serverPort = 8888;

// Device-specific configurations
const int deviceID = 1; // Change to 2 for the second device
WiFiUDP udp;

unsigned long previousMillis = 0; // Stores the last time data was sent
const long interval = 5000; // Interval to send data (5 seconds)
bool handshakeComplete = false; // Handshake status

void setup() {
  // Initialize serial communication for debugging
  Serial.begin(9600);

  // Initialize the ADC attenuation (up to ~3.3V input)
  analogSetAttenuation(ADC_11db);

  // Connect to WiFi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");

  // Start UDP
  udp.begin(8888);
}

void loop() {
  // Handshake: Wait for "hi" from Raspberry Pi
  if (!handshakeComplete && udp.parsePacket()) {
    String incomingMessage = udp.readString();
    incomingMessage.trim();

    if (incomingMessage == "hi") {
      // Respond to handshake
      char handshakeResponse[50];
      snprintf(handshakeResponse, sizeof(handshakeResponse), "esp_%d, 9999", deviceID);
      udp.beginPacket(serverIP, serverPort);
      udp.print(handshakeResponse);
      udp.endPacket();

      Serial.println("Handshake completed. Sending data...");
      handshakeComplete = true; // Handshake is done
    }
    return; // Wait for handshake before sending sensor data
  }

  // Regular data transmission
  if (handshakeComplete) {
    unsigned long currentMillis = millis(); // Get the current time

    // Check if interval has passed
    if (currentMillis - previousMillis >= interval) {
      previousMillis = currentMillis;  // Save the current time

      // Read the input from the light sensor
      int lightReading = analogRead(LIGHT_SENSOR_PIN);

      // Format the message
      char message[50];
      snprintf(message, sizeof(message), "esp_%d, %d", deviceID, lightReading);

      // Send the message to the Raspberry Pi
      udp.beginPacket(serverIP, serverPort);
      udp.print(message);
      udp.endPacket();

      // Debugging output
      Serial.print("Sent: ");
      Serial.println(message);
    }

    // Check for reset command from Pi
    if (udp.parsePacket()) {
      String resetCommand = udp.readString();
      resetCommand.trim();

      if (resetCommand == "reset") {
        // Reset the timer or any other necessary state
        previousMillis = 0;
        Serial.println("Timer reset by Pi");
      }
    }
  }
}