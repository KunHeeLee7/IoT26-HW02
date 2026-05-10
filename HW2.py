# HW2

from gpiozero import Button, LED
from signal import pause

# GPIO setup
led = LED(14)
button = Button(4)

# Turn on LED when button is pressed
button.when_pressed = led.on

# Turn off LED when button is released
button.when_released = led.off

# Keep program running
pause()
