import requests
from twilio.rest import Client

link = "https://api.openweathermap.org/data/2.5/onecall"
key = "fdbd7a2f5f7c2058c4b39eedfb11a5bd"
account_sid = "AC0e6e5d2dc75213bceeebff67247c0db7"
auth_token = "f6d4630424820b66d0b3cc818c5c8e27"

parameters = {
    "lat": 28.676790,
    "lon": 77.262001,
    "appid": key,
    "exclude": "current,minutely,daily"
}

response = requests.get(link, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_check = weather_data['hourly'][:12]

rain = False
for h in weather_check:
    condition = h['weather'][0]['id']
    if int(condition) < 700:
        rain = True
if rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's raining outside. Bring your umbrella dear.",
        from_='__from number__',
        to='--to_number__'
    )
    print(message.status)
