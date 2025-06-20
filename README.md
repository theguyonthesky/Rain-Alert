# Rain Alert ☔️
A Python script that uses OpenWeatherMap to check the weather forecast for your location and sends you a WhatsApp alert via Twilio if rain is expected soon.

# Features
- Fetches weather forecast data from `OpenWeatherMap` API

- Detects rain in upcoming hours based on weather condition codes

- Sends WhatsApp notifications via `Twilio` if rain is predicted

- Authorization is done using environment variables for API keys and secure credentials

# How It Works
1. The script queries the `OpenWeatherMap` forecast API for the next few hours at a fixed location <br>*(Note: the coordinates (latitude & longitude) are set to Baku, Azerbaijan as a sample — you can replace them with your own location.)*

2. It scans the forecasted weather conditions for any sign of rain (weather condition codes below 700).

3. If rain is detected, the script uses `Twilio’s` WhatsApp API to send a reminder message to your phone. <br>*(Note: You’ll need to create a Twilio account and activate the WhatsApp Sandbox to enable messaging.)*

4. You get a timely notification saying: *“It’s going to rain today. Remember to take an ☔️”*

# Tools and Modules Used
- Python – main programming language
- `requests` – to make HTTP requests to the weather API (Install it with: pip install requests)
- `twilio` – to send WhatsApp messages through Twilio API (Install it with: pip install twilio)
- Environment variables for API keys (`OWM_API_KEY`, `TWILIO_SID`, `AUTH_TOKEN`) for security

# Files
`main.py`: Main script for weather check and alert

# How to Run
1. Make sure Python is installed on your system

2. Clone or download this repository.

3. Create an `OpenWeatherMap` account to get your API key

4. Create a `Twilio` account to get your `Account SID` and `Auth Token`, and activate the WhatsApp Sandbox to enable messaging

5. Run the app using one of the following methods:
    - Terminal (macOS/Linux): 'python3 main.py'
    - Windows (or IDEs like VS Code, PyCharm): 'python main.py' or use the Run button

6. *(Optional)* Create a `PythonAnywhere` account to run your script automatically. Since your script will be hosted online, it’s highly recommended to use environment variables to securely store your `OpenWeatherMap API key`, Twilio Account SID, and Auth Token.

# License
This project is licensed under the MIT License. Feel free to use or modify it for personal use or learning.
<br> **Don't forget your ☔️ 😊**
