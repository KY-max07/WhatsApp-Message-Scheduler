# Installing Required libraries

from twilio.rest import Client
from datetime import datetime, timedelta
import time

# Twilio account info

account_sid = "AC5fc83b943474c062684a73d75a706896"
auth_token="78b52cbebf12c879c23f3e83a34bbb85"
client = Client(account_sid, auth_token)


# message function

def send_message(recipient_number, message):
    try:
        message = client.messages.create(
            from_= "whatsapp:+14155238886",
            body = message,
            to = f"WhatsApp:{recipient_number}"
            
        )
        print(f"message sent successfully!")
    except Exception as e:
        print('an error occurred ', e)
        
        
#user input
name = input('Enter your name : ') 
recipient_number = input('enter the recipient WhatsApp number with Country code (+91) : ')
message = input(f"enter the message : ")   

# Parse date and time & calculate the delay

date_str = input('enter the date to send the message (YYYY-MM-DD) : ')
time_str = input( "Enter the time to send the message (HH:MM) : ")

# datetime

Schedule_datetime = datetime.strptime(f'{date_str} {time_str}','%Y-%m-%d %H:%M')
current_datetime = datetime.now()


# current delay
time_difference = Schedule_datetime-current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds <= 0:
    print('PAST!!!!! Please enter Future Date and Time : ')
else:
    print(f"Message scheduled to {name} at {Schedule_datetime} ")
    
    # wait until the scheduled time 
    time.sleep(delay_seconds)
    
    
    #Send the message 
    send_message(recipient_number, message)
    
    
