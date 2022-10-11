import RPi.GPIO as GPIO 
import time 
  
def on(pin,tim): 
         GPIO.output(pin,1) 
         time.sleep(tim) 
def off(pin,tim): 
         GPIO.output(pin,0) 
         time.sleep(tim) 
         return  
  
GPIO.setmode(GPIO.BOARD) 
  
GPIO.setup(10,GPIO.OUT) 
GPIO.setup(12,GPIO.OUT) 
GPIO.setup(13,GPIO.OUT) 
  
for i in range(0,2): 
         on(10,2) 
         off(10,1) 
         on(12,2) 
         off(12,1) 
         on(13,2) 
         off(13,1) 
print('Done') 
GPIO.cleanup()
