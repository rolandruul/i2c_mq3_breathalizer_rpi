# MQ-3, I2C and Raspberry Pi3 Breathalizer
# @author - Roland Ruul - 2019
# Using digital output from MQ-3 (1 or 0)
# Should use analog output and analog to digital converter for precise reading
import time
import RPi.GPIO as GPIO

# Initialize I2C OLED Display
from display import Display

display = Display()

font = 'Montserrat-Light.ttf'

# GPIO and MQ-3 Configuration
DO_PIN = 4
REFRESH_INTERVAL = 0.5
PREV_STATE = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(DO_PIN, GPIO.IN)

# Breathalizer logic
try:
	while True:
	
		reading = GPIO.input(DO_PIN)
		
		if PREV_STATE != reading:

			# Clear the display
			display.clearImage()

			# Set header
			display.setFont(font, 12)
			display.write(0, 0, 'Alkomeeter  |  Roland')

			display.setFont(font, 14)
			if reading < 1:
				display.write(0, 25, 'Purjus oled!')
			else:
				display.write(0, 25, 'Kaine oled!')

		PREV_STATE = reading

		time.sleep(REFRESH_INTERVAL)

except KeyboardInterrupt:
	
	# Cleanup when CTRL + X
	GPIO.cleanup()
	display.clearImage()
