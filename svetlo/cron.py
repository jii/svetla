import RPi.GPIO as GPIO
P0 = 12 # LED pin
P1 = 13 # LED pin
P2 = 11 # LED pin
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(P0, GPIO.OUT)
GPIO.setup(P1, GPIO.OUT)
GPIO.setup(P2, GPIO.OUT)

def Klikni():
	GPIO.output(P0, not GPIO.LOW)
	pass
def my_scheduled_job():
	GPIO.output(P0, not GPIO.LOW)
	pass