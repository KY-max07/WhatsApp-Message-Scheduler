from twilio.rest import Client
from datetime import datetime, timedelta
import time

# Twilio account info

account_sid = "account_sid"
auth_token="auth_token"
client = Client(account_sid, auth_token)




def send_message(recipient_number, message):
    try:
        message = client.messages.create(
            from_= "whatsapp:+14155238886",
            body = message,
            to = f"whatsapp:+91{recipient_number}"
            
        )
        print(f"message sent successfully!")
    except Exception as e:
        print('an error occurred ', e)
        
        

name = input('Enter your name : ') 
recipient_number = input('enter the recipient WhatsApp number with Country code (+91):')
message = input(f"enter the message : ")   


date_str = input('enter the date to send the message (YYYY-MM-DD) : ')
time_str = input( "Enter the time to send the message (HH:MM) : ")


Schedule_datetime = datetime.strptime(f'{date_str} {time_str}','%Y-%m-%d %H:%M')
current_datetime = datetime.now()



time_difference = Schedule_datetime-current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds <= 0:
    print('PAST!!!!! Please enter Future Date and Time : ')
else:
    print(f"Message scheduled to {name} at {Schedule_datetime} ")
    
    
    time.sleep(delay_seconds)
    
    
     
    send_message(recipient_number, message)
    
    
