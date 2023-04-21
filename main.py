import requests
from datetime import datetime
#response=requests.get(url="http://api.open-notify.org/iss-now.json")
#response.raise_for_status()
#data=response.json()
#Longitude=data["iss_position"]["longitude"]
#Latitude=data["iss_position"]["latitude"]
#print(Latitude)
#print(Longitude)
My_lat=9.033140
My_lng=38.750080
parameters={
    'lat':My_lat,
    'lng':My_lng,
    "formatted": 0,
}
response=requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data=response.json()
sunrise=data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset=data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)
date=datetime.now().hour
print(date)