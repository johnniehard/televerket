from gpiozero import Button
import requests
import os

state = 'IDLE'

auth = (os.environ['CALL_API_USERNAME'], os.environ['CALL_API_PASSWORD'])

fields = {
        'from': os.environ['CALLER_NUMBER'],
        'to': os.environ['TARGET_NUMBER'],
        'voice_start': '{}'
    }

print('Started')
print(os.environ['GIT_REV'])

def button_pressed():
    print('PRESSED')
    state = 'CALLING'
    response = requests.post("https://api.46elks.com/a1/calls", data=fields, auth=auth)
    print(response.content)
    state = 'IDLE'


button = Button(21)
button.when_pressed = button_pressed

while True:
   if state == 'IDLE':
       button.wait_for_press() 
