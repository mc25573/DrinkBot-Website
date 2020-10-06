// Pump pump0(0, 100); // pin number, on time
// Pump pump1(1, 350);

// pump0.Run();
// pump0 = pin 0

class Pump
{
    // Class Member Variables
    // These are initialized at startup
    int pinNum;      // the number of the pin
    unsigned short OnTime;     // milliseconds of on-time
   
    // These maintain the current state
    int pinState;                 // ledState used to set the pin
    unsigned long previousMillis; // will store last time pin was updated
    bool done;
   
    // Constructor - creates a Pump 
    // and initializes the member variables and state
    public:
    Pump(int pin)
    {
      pinNum = 2 * pin + 2; // +2 to avoid rx/tx pins
      pinMode(pinNum, OUTPUT);   
      pinMode(pinNum + 1, OUTPUT); // 2 pins required for motor driver
      pinState = LOW; 
      previousMillis = 0;
    }
    void Start(unsigned short on, int direct)
    {
      done = false;
      OnTime = on;
      pinState = direct; 
      digitalWrite(pinNum, pinState);  // Turn on
      digitalWrite(pinNum + 1, !pinState);
      previousMillis = millis();
    }
    bool Run()
    {
      // check to see if it's time to turn off the pin
      unsigned long currentMillis = millis(); 
      if((currentMillis - previousMillis >= OnTime))
      {
        // maybe should turn off using the stdby pin
        pinState = LOW;  // Turn it off
        digitalWrite(pinNum, pinState);  // Update pin
        digitalWrite(pinNum + 1, pinState);
        done = true;
      }
      return done;
    }
};

const byte numChars = 72;
const byte numPumps = 10;
// first value is motor direction
float dataFromPi[numPumps * 2 + 1] = {-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1};
char receivedChars[numChars];
char tempChars[numChars];    // temporary array for use when parsing
bool newData = false;
bool all_pumps_done = false;
Pump *all_pumps[numPumps];

void setup() {
  Serial.begin(115200);
  // pins 52 and 53 will be pwm and stdby, respectively
  // or use 5 V pin? for pwm at least
  for (int i = 0; i < numPumps; i++){
    all_pumps[i] = new Pump(i);
  }
}

void loop() {
  
  recvWithStartEndMarkers();
  
  if (newData == true) {
    strcpy(tempChars, receivedChars);
    // debugging
    Serial.println(receivedChars);
    parseData();
    newData = false;
    
    // start specified pumps
    for (int i = 1; i <= numPumps*2; i+=2){
      if (dataFromPi[i] != -1){ 
        all_pumps[(int)dataFromPi[i]]->Start(dataFromPi[i+1] * 3760,(int)dataFromPi[0]); // 1 = 3.76s of on time       
      }else{
        break;
      }
    }
    // exits while loop when all pumps finish running
    while (all_pumps_done == false){       
      all_pumps_done = true;
             
      for (int i = 1; i < numPumps*2; i+=2){   
                
        if (dataFromPi[i] != -1){
          all_pumps_done = all_pumps_done && all_pumps[(int)dataFromPi[i]]->Run(); // check all pumps
          
        }else{
          break;
        }       
      }
      // can do (quick) operations here
      // debugging
      for (int i = 2;i <= numPumps*2+1; i++){
        Serial.print(digitalRead(i));
        Serial.print(" ");
      }
      Serial.println("");
      delay(200);
    }
    all_pumps_done = false;
    
    // Reset Input Data
    for (int i = 0; i <= numPumps*2; i+=1){ 
      dataFromPi[i] = -1;
    }
    // debugging
    Serial.println("Waiting for new data");
  }
}


void recvWithStartEndMarkers() {
    static boolean recvInProgress = false;
    static byte ndx = 0;
    char startMarker = '<';
    char endMarker = '>';

    while (Serial.available() > 0 && newData == false) {
        char rc = Serial.read();

        if (recvInProgress == true) {
            if (rc != endMarker) {
                receivedChars[ndx] = rc;
                ndx++;
                if (ndx >= numChars) {
                    ndx = numChars - 1;
                }
            }
            else {
                receivedChars[ndx] = '\0'; // terminate the string
                recvInProgress = false;
                ndx = 0;
                newData = true;
            }
        }

        else if (rc == startMarker) {
            recvInProgress = true;
        }
    }
}

void parseData() {      // split the data into its parts
 
    int i = 0;
    char *p = strtok(tempChars, ",");

    while (p != NULL)
    {
        dataFromPi[i++] = atof(p);
        p = strtok(NULL, ",");
    }   // convert this part to an integer

}

 
