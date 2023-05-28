import RPLCD as RPLCD
from RPLCD import CharLCD
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
import time

from gpiozero import Buzzer
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
BUZZER= 17
buzzState = False
GPIO.setup(BUZZER, GPIO.OUT)



TRIG=22
ECHO=27
GPIO.setmode(GPIO.BCM)


GPIO.setmode(GPIO.BCM) 
green = 22
red = 27
motion = 16

while True:

    i=GPIO.input(16)
    
    if i == 1:
       GPIO.output(22, GPIO.HIGH)  #Turn ON GREEN LED
       GPIO.output(27, GPIO.LOW)
       print("System activated")
	
    

    #lcd.text("Distance",1)
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.output(TRIG,False)
    time.sleep(+2)
    GPIO.output(TRIG,True)
    time.sleep(0.00001)
    GPIO.output(TRIG,False)
    
    while GPIO.input(ECHO)==0:
        pulse_start=time.time()
    
    while GPIO.input(ECHO)==1:
        pulse_end=time.time()
        pulse_duration=pulse_end-pulse_start
        distance=pulse_duration*17150
        distance=round(distance,2)
   
   
    
    print("DISTANCE :"+ str(distance)+"cm")
   
    lcd=CharLCD(cols=16, rows=2, pin_rs=26, pin_e=19, pins_data=[21, 20, 16, 12, 13, 6, 5 ,11], numbering_mode=GPIO.BCM)
    lcd.write_string("Distance:"+ str(distance) +"  cm ")
    
    if distance > 15:
        buzzState = False 
        GPIO.output(BUZZER, GPIO.LOW)
        print("You Good")
        lcd.write_string("Distance is adequate")
    else:
        buzzState = True
        #beep1         
        GPIO.output(BUZZER, GPIO.HIGH)
        sleep(0.5)
        GPIO.output(BUZZER, GPIO.LOW)
        sleep(0.5)
        
        #beep2         
        GPIO.output(BUZZER, GPIO.HIGH)
        sleep(0.5)
        GPIO.output(BUZZER, GPIO.LOW)
        sleep(0.5)
        
        #beep3         
        GPIO.output(BUZZER, GPIO.HIGH)
        sleep(0.5)
        GPIO.output(BUZZER, GPIO.LOW)
        sleep(0.5)
        
        #beep4         
        GPIO.output(BUZZER, GPIO.HIGH)
        sleep(0.5)
        GPIO.output(BUZZER, GPIO.LOW)
        sleep(0.5)
        
        #beep5         
        GPIO.output(BUZZER, GPIO.HIGH)
        sleep(0.5)
        GPIO.output(BUZZER, GPIO.LOW)
        sleep(0.5)
        
        print("Too Close")
        lcd.write_string("Too close keep one meter distance")
        buzzState = False
    
  elif i==0: 
       GPIO.output(22, GPIO.LOW)  #Turn ON GREEN LED
       GPIO.output(27, GPIO.HIGH)
       print("System is off")
	
