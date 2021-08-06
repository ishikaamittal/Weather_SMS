import requests
from twilio.rest import Client

weather_api_link = "weather_api_link"
weather_api_key = "weather_api_key"
account_sid = "sid"
auth_token = "tokencode"

parameters = {
    "lat": 28.676790,
    "lon": 77.262001,
    "appid": weather_api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(weather_api_link, params=parameters)
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
