import requests
import json

response_data = requests.get('https://www.iplocation.net/go/ipinfo').text
try:
   response_json_data = json.loads(response_data)
   print("response_json_data=",json.dumps(response_json_data,indent=4))
   location = response_json_data["loc"].split(",")
   print ("Latitude: %s" % location[0])
   print ("Longitude: %s" % location[1])
except ValueError:
   print ("Exception happened while loading data")
