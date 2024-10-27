"""This file runs the collected data through chatGPT to recognize trends and patterns"""
import google.generativeai as genai
import csv

API_KEY = 'API KEY'
genai.configure(api_key=API_KEY)

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
)

chat_session = model.start_chat(
  history=[
  ]
)

api_keys = []
preparation_list = []
location = []
disasters = ["Hurricane", "Earthquake", "Flood", "Wildfire", "Winter Storm"]

for disaster in disasters:
    response1 = chat_session.send_message(f"Please output a list of things that a person should do to prepare "
                                          f"for the following natural disaster: {disaster}, keep in mind this text "
                                          f"will be displayed on a phone SMS so the format should match. Not too long "
                                          f"but enough information for the user to be properly informed and must be "
                                          f"readable.")
    response2 = chat_session.send_message(f"Please output a list of things that a person should do to prepare "
                                          f"for the following natural disaster if it is considered more severe or "
                                          f"higher risk: {disaster}, keep in mind this text "
                                          f"will be displayed on a phone SMS so the format should match. Not too long "
                                          f"but enough information for the user to be properly informed and must be "
                                          f"readable.")
    preparation_list.append((response1.text.strip(), response2.text.strip()))
#

filename = "Prep_info"

with open(filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerows(preparation_list)
