import RPi.GPIO as GPIO
import time
import os


os.system('raspi-gpio set 13 ip')
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
os.system('amixer sset "PCM" 0%')


def turnOnScreen():
    os.system('raspi-gpio set 13 op a0')
# power on screen
    os.system('sudo echo 0 | sudo tee /sys/class/backlight/rpi_backlight/bl_power')
# change volume to 90%
    os.system('amixer sset "PCM" 90%')


def turnOffScreen():
    os.system('raspi-gpio set 13 ip')
# power off screen
    os.system('sudo echo 1 | sudo tee /sys/class/backlight/rpi_backlight/bl_power')
# change volume to 0%
    os.system('amixer sset "PCM" 0%')


turnOffScreen()
screen_on = False

while (True):
    # If you are having and issue with the button doing the opposite of what you want
    # IE Turns on when it should be off, change this line to:
    # input = not GPIO.input(26)
    input = GPIO.input(26)
    if input != screen_on:
        screen_on = input
        if screen_on:
            turnOnScreen()
        else:
            turnOffScreen()
    time.sleep(0.3)
