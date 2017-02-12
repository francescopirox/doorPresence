import RPi.GPIO as R
import time

def open():
	R.setmode(R.BCM)	
	R.setup(17, R.OUT, initial =0)
	print ("Apertura in corso!")
	R.output(17, 1)
	time.sleep(1)
	R.output(17, 0)
	print ("Porta aperta!")
	R.cleanup
def check():
	R.setmode(R.BCM)
	R.setup(4,R.IN)
	Input = R.input(4)
	i=1
	if Input == i:
        	print "door closed"
	else:
        	print "porta aperta"
	R.cleanup()

