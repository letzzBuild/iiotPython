import RPi.GPIO as GPIO
import subprocess
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(36,GPIO.OUT)


def checkNetworkConnection():
  while(1):
     sleep(5)    
     result=subprocess.Popen("sudo mii-tool eth0 ",stdout=subprocess.PIPE,shell=True)
     finalResult=result.communicate()
     print(finalResult)
     for i in finalResult[:1]:
        if(b'eth0: no link' in i):
           GPIO.output(36,False)
           print("led off")
        else:
           GPIO.output(36,True)
           print("led on")
     break

