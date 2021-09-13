import RPi.GPIO as GPIO
import time
import os

os.system('raspi-gpio set 19 ip')
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.OUT)

def start_network():
    os.system('rfkill unblock wifi')
    os.system('rfkill unblock bluetooth')


def stop_network():
    os.system('rfkill block wifi')
    os.system('rfkill block bluetooth')


def turn_on_screen():
    os.system('raspi-gpio set 19 op a5')
    GPIO.output(18, GPIO.LOW)


def turn_off_screen():
    os.system('raspi-gpio set 19 ip')
    GPIO.output(18, GPIO.HIGH)


turn_off_screen()
screen_on = False


while (True):
    # If you are having and issue with the button doing the opposite of what you want
    # i.e. it turns on when it should be off, change this line to:
    input = GPIO.input(26)
    # input = not GPIO.input(26)
    if input != screen_on:
        screen_on = input
        if screen_on:
            turn_on_screen()
            start_network()
        else:
            turn_off_screen()
            stop_network()
    time.sleep(0.3)