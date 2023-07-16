import requests

# response=requests.get(url="http://api.open-notify.org/iss-now.json")

# response.raise_for_status()
# data=response.json()["iss_position"]
# longitude=data["longitude"]
# latitude=data["latitude"]
# ISS_postion=(longitude,latitude)
# print(ISS_postion)

my_lat=18.520430
my_long=73.856743
position={
    "lat":my_lat,
    "lng":my_long
}
response=requests.get(url="https://api.sunrise-sunset.org/json",params=position)
print(response.json())
