""" Sends user data to Twilio which will send an SMS to users' phone number."""
import time
import csv
import json
from twilio.rest import Client

from_Number = '+14082170234'
user_Number = 'Something'
user_data = {}

with open("../server/file.txt", "r") as f:


while True:
  account_sid = 'ACCOUNT'
  auth_token = 'AUTH TOKEN'
  client = Client(account_sid, auth_token)

  for row in user_data:
    if location in row.values():
      message = client.messages.create(
        from_=from_Number,
        body=f"WARNING! : Natural Disaster Incoming! ",
        to=row[location]
      )
  #time.sleep(360*60)
