import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

# openweather api
API_KEY = os.getenv("OPEN_WEATHER_API_KEY")
LAT = "32.101620"
LONG = "-88.322580"
API_ENDPOINT = f"https://api.openweathermap.org/data/2.5/forecast?lat={LAT}&lon={LONG}&appid={API_KEY}&exclude=current,daily,minutely"

# twilio api
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")

response = requests.get(url=API_ENDPOINT)
response.raise_for_status()
weather_data = response.json()

twelve_hour_forecast = [weather["weather"][0] for weather in weather_data["list"][:13]]


def send_message():
    client = Client(account_sid, auth_token)
    message = client.messages \
            .create(
                body="It's going to rain, grab an ☔️",
                from_= os.getenv("TWILIO_FROM"),
                to=os.getenv("TWILIO_TO")
        )

    print(message.status)


for hour in twelve_hour_forecast:
    hour["id"] < 700 and send_message()

