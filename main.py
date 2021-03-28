from gpiozero import Button
import requests
import os

git_rev = None
with open('git_rev', 'r') as f:
    git_rev = f.read()

state = 'IDLE'

auth = (os.environ['CALL_API_USERNAME'], os.environ['CALL_API_PASSWORD'])

fields = {
        'from': os.environ['CALLER_NUMBER'],
        'to': os.environ['TARGET_NUMBER'],
        'voice_start': '{}'
    }

def send_sms(message):
    sms = {
        'from': os.environ['CALLER_NUMBER'],
        'to': os.environ['TARGET_NUMBER'],
        'message': message,
    }

    response = requests.post("https://api.46elks.com/a1/sms", data=sms, auth=auth)
    print("SENT SMS:", response.content)

print('Started')
print(git_rev)
send_sms(f'Televerket: {git_rev}')

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
