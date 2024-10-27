import google.generativeai as genai
from ApiKey import Key
from Weather import Weather

genai.configure(api_key=Key.google_k)

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

def ai() -> tuple:
    response = chat_session.send_message(f"Create a prediction model base on weather information that I give you. "
                                         f"{prediction} gives you information in the order of temp, humidity, "
                                         f"wind_speed, precip_intensity, pressure_surface, "
                                         f"pressure_sea, cloud_cover, visibility. Tell me if a natural disaster is "
                                         f"likely to occur(yes or no). If yes, tell me what natural disaster "
                                         f"and the level of risk (0 to 5). Provide the answer "
                                         f"in a tuple (yes/no, type of natural disaster, risk), risk is 0 "
                                         f"and type is N/A if answer is no. Just give me the answer.")
    return response.text

def to_iso(location: str):
    response = chat_session.send_message(f"{location}, give me latitude and longitude separated by a comma "
                                         f"Just give me the answer.")

    return response.text


f = open("../server/file.txt", "r")
nextline = f.readline()
f2 = open("Result.csv", "w")

while nextline:
    if nextline.__contains__("Location"):
        coor = nextline.strip().split(":")
        iso = to_iso(coor).strip().split(",")
        coor = [float(iso[0]), float(iso[1])]
        weather = Weather()
        weather.set(coor,"now", "nowPlus5d")
        prediction = weather.execute() #temp, humidity, wind_speed, precip_intensity, pressure_surface,
        # pressure_sea, cloud_cover, visibility
        response = ai()
        if response[0].strip().lower() == 'yes':
            filename = "Result.csv"
            f2.write(str(response) + "\n")

    nextline = f.readline()

f2.close()


