#include <Servo.h>

Servo myservo;

String msg = "";
String msgCurr = "";
int val[] = {0, 0, 0, 0, 0, 0};
int lastVal[] = {0, 0, 0, 0, 0, 0};

void setup() {
  Serial.begin(9600);
  myservo.attach(11); 
}

void loop() {
  if (Serial.available()) {
    char chrIn = Serial.read();
    msg += chrIn;
  }
  if(msg.indexOf(";") > 0){
    msgCurr = msg.substring(0, msg.indexOf(";"));
    //Serial.println(msgCurr);
    msg = msg.substring(msg.indexOf(";") + 3);
  }
  if(msgCurr != ""){
    int i = 0;
    while(msgCurr.indexOf(",") != -1){
//      Serial.print("Motor ");
//      Serial.print(i);
      val[i++] = msgCurr.substring(0, msgCurr.indexOf(",")).toInt();
//      Serial.println(" " + msgCurr.substring(0, msgCurr.indexOf(",")));
      msgCurr = msgCurr.substring(msgCurr.indexOf(",") + 1);
    }
//    Serial.print("Motor ");
//    Serial.print(i);
      val[i++] = msgCurr.substring(0, msgCurr.indexOf(";")).toInt();
//    Serial.println(" " + msgCurr.substring(0, msgCurr.indexOf(";")));
    msgCurr = "";
  }
  if(lastVal[0] != val[0]){
    myservo.write(val[0]);
    lastVal[0] = val[0];
    Serial.println(val[0]);
  }
}
