import requests
import datetime
import json

URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=560078&date=01-08-2021"
response = requests.get(URL)
resp_json = response.json()
# print(resp_json)

print(len(resp_json["centers"]))
print(json.dumps(resp_json, indent = 1))



# for i in range (0,len(resp_json['centers'])):
# 	if 
# 	print(json.dumps(resp_json['centers'][i], indent = 1))

# if len(resp_json["centers"]) == 0:
# 	error = "No centers available in this pincode"
# 	print(error)



# URL = "https://cdn-api.co-vin.in/api/v2/admin/location/states"
# response = requests.get(URL)
# print(response)
# json_data = response.json()
# print(json_data)




# URL = "https://cdn-api.co-vin.in/api/v2/admin/location/districts/1"
# response = requests.get(URL)
# print(response)
# json_data = response.json()
# print(json_data)
