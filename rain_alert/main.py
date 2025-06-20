import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


api_key = os.environ.get('OWM_API_KEY')
api_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = os.environ.get('TWILIO_SID')
auth_token = os.environ.get('AUTH_TOKEN')




LATITUDE = 40.409261
LONGITUDE = 49.867092


parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url = api_endpoint, params=parameters)
# print(response.status_code)
response.raise_for_status()
weather_data = response.json()
# print(weather_data)

# forecast_list = weather_data['list']
# first_condition_code = forecast_list[0]['weather'][0]['id']
# second_condition_code = forecast_list[1]['weather'][0]['id']
# third_condition_code = forecast_list[2]['weather'][0]['id']
# fourth_condition_code = forecast_list[3]['weather'][0]['id']

will_rain = False
for hour_data in weather_data['list']:
    condition_code = hour_data['weather'][0]['id']
    if condition_code < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client = proxy_client)
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body="It's going to rain today. Remember to take an ☔️",
        to='whatsapp:YOUR_WP_PHONE_NUMBER'
    )
    print(message.status)
