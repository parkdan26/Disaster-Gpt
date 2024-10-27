import requests
from Apikey import Key

class Weather:
    url = f"https://api.tomorrow.io/v4/timelines?apikey={Key.weather_k}"
    location: list
    startDate: str
    endDate: str

    def set(self, location: list, startDate: str, endDate: str):
        self.location = location
        self.startDate = startDate
        self.endDate = endDate

    def execute(self):
        params = {
            "location": f"{float(self.location[0])}, {float(self.location[1])}",
            "fields": ["temperature", "humidity", "windSpeed", "precipitationIntensity", "pressureSurfaceLevel",
                       "pressureSeaLevel", "cloudCover", "visibility"],
            "units": "metric",
            "timesteps": ["1d"],
            "startTime": self.startDate,
            "endTime": self.endDate
        }
        headers = {
            "accept": "application/json",
            "Accept-Encoding": "gzip",
            "content-type": "application/json"
        }

        response = requests.post(self.url, json=params, headers=headers)
        data = response.json()

        intervals = data['data']['timelines'][0]['intervals']
        interval = intervals[len(intervals) - 1]["values"]
        temp = interval["temperature"]
        humidity = interval["humidity"]
        wind_speed = interval["windSpeed"]
        precip_intensity = interval["precipitationIntensity"]
        pressure_surface = interval["pressureSurfaceLevel"]
        pressure_sea = interval["pressureSeaLevel"]
        cloud_cover = interval["cloudCover"]
        visibility = interval["visibility"]

        return [temp, humidity, wind_speed, precip_intensity,
                pressure_surface, pressure_sea, cloud_cover, visibility]