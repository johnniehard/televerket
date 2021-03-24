from gpiozero import Button
import requests

def button_pressed():
    print("PRESSED!")

button = Button(21)
button.when_pressed = button_pressed

while True:
   button.wait_for_press() 
