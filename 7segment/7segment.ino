#include <WiFi.h>
#include <PubSubClient.h>


int seg1 = 23; //g
int seg2 = 22; //f
int seg3 = 2;  //a
int seg4 = 13; //b
int seg5 = 21; //e
int seg6 = 19; //d
int seg7 = 18; //c

#define A (1 << 6)
#define B (1 << 5)
#define C (1 << 4)
#define D (1 << 3)
#define E (1 << 2)
#define F (1 << 1)
#define G (1 << 0)

const char* ssid = "Test1";
const char* pw = "12345678";


const uint8_t value[] = {
  0b1111110,
  0b1010000,
  0b1101101,
  0b1111001,
  0b1010011,
  0b0111011,
  0b0111111,
  0b1110000,
  0b1111111,
  0b1111011,
};

WiFiClient wifiClient;
PubSubClient client(wifiClient);

uint8_t number = 0;

void handler(const char* topic, uint8_t* data, unsigned int dataLength){
  number= (*data) - '0';
}

void setup() {
  // put your setup code here, to run once:
  WiFi.begin(ssid,pw);
  while (!WiFi.isConnected()){
    delay(500);
  }
  client.setCallback(handler);
  client.setServer("192.168.43.20", 1883);

  client.connect("LIVERPOOL");

  client.subscribe("pl_winners");

  pinMode(seg1, OUTPUT);
  pinMode(seg2, OUTPUT);
  pinMode(seg3, OUTPUT);
  pinMode(seg4, OUTPUT);
  pinMode(seg5, OUTPUT);
  pinMode(seg6, OUTPUT);
  pinMode(seg7, OUTPUT);

}

void display(uint8_t number) {
  uint8_t bitmap = value[number];
  digitalWrite(seg3, bitmap & A);
  digitalWrite(seg4, bitmap & B);
  digitalWrite(seg7, bitmap & C);
  digitalWrite(seg6, bitmap & D);
  digitalWrite(seg5, bitmap & E);
  digitalWrite(seg2, bitmap & F);
  digitalWrite(seg1, bitmap & G);
}


void loop() {
  // put your main code here, to run repeatedly:
  if(!client.connected()){
    client.connect("LIVERPOOL");
    delay(100);
}
  client.loop();
  display(number);
} 

