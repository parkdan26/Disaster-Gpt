""" Sends user data to Twilio which will send an SMS to users' phone number."""
import time
import csv
import json
from twilio.rest import Client

from_Number = '+14082170234'
user_data = {}

with open("../server/file.txt", "r") as f:
  nextLine = f.readline()
  while nextLine:
    if nextLine.__contains__(("Location")):
      location = nextLine.strip().split(":")[1]
      location = location[0:len(location) - 1].strip().split("\"")
      location = location[1]
    if nextLine.__contains__(("Phone")):
      phone = nextLine.strip().split(":")[1]
      phone = phone[0:len(phone) - 1].strip().split("\"")
      phone = phone[1]
      phone1 = phone.replace('-', '')
      user_data[location] = phone1
    nextLine = f.readline()

  f2 = open("Prep_info.txt", "r")
  nextline2 = f2.readline()  # ("yes", "Flood", 5) "Oakville"
  disaster_list = []
  while nextline2:
    disaster_list.append(nextline2.strip())
    nextline2 = f2.readline()

while True:
  account_sid = 'ACCOUNT'
  auth_token = 'AUTH TOKEN'
  client = Client(account_sid, auth_token)

  f = open("Result.txt", "r")
  nextline = f.readline()
  while nextline:
    for loca in user_data:
      if loca.lower() == nextline.split("+")[1].strip():
        disaster = nextline.split("+")[0][1]
        message = client.messages.create(
          from_=from_Number,
          body=f"{disaster}WARNING! : Affected cities {loca} \n"
               f"The following message will have preparation advice",
          to=user_data[loca]
        )

        if disaster == "Hurricane":
          message = client.messages.create(
            from_=from_Number,
            body=disaster_list[0],
            to=user_data[loca]
          )
        elif disaster == "Earthquake":
          message = client.messages.create(
            from_=from_Number,
            body=disaster_list[1],
            to=user_data[loca]
          )
        elif disaster == "Flood":
          message = client.messages.create(
            from_=from_Number,
            body=disaster_list[2],
            to=user_data[loca]
          )
        elif disaster == "Wildfire":
          message = client.messages.create(
            from_=from_Number,
            body=disaster_list[3],
            to=user_data[loca]
          )
        elif disaster == "Winter Storm":
          message = client.messages.create(
            from_=from_Number,
            body=disaster_list[4],
            to=user_data[loca]
          )

    nextline = f.readline()
    time.sleep(360*60)
