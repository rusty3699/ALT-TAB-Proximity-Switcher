#define trigPin 9
#define echoPin 10
#define ledPin 13  // Onboard LED pin

void setup() {
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(ledPin, OUTPUT);  // Set LED pin as output
}

void loop() {
  long duration, distance;
  
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  duration = pulseIn(echoPin, HIGH);
  distance = (duration / 2) / 29.1;

  Serial.println(distance);

  // Adjust the threshold distance based on your preference
  if (distance < 50) {
    digitalWrite(ledPin, HIGH);  // Turn on LED if someone is near
  } else {
    digitalWrite(ledPin, LOW);   // Turn off LED if no one is near
  }

  delay(500);  // Adjust the delay as needed
}
