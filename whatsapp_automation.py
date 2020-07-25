#use twilio sandbox for whatsapp
#first create twillio account in twilio 
#step 1 --> pip install twilio

#create a file whatsaap.py


import os
import twilio
from twilio.rest import Client

account_sid = 'ACa7b8462ee514fd9be3ea986517e681d5'
auth_token = '7376c7f4bb0d6bcac631b4490fcf7605'
client = Client(account_sid, auth_token)


from_whatsapp_number='whatsapp:+91 9304290368'
to_whatsapp_number='whatsapp:+919708549289'

client.messages.create(body='hello world!',
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)
