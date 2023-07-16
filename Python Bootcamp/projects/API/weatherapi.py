import requests

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

data=requests.get(url="https://api.openweathermap.org/data/2.5/onecall?lat={18.520430}&lon={73.856743}&exclude={part}&appid={52b82b31607377ec42413106692f30e1}")
weather=data.json()
print(weather)