import requests
from requests.structures import CaseInsensitiveDict

# GET requests from API
url = "https://weatherstationapi.azurewebsites.net/api/TemperatureSensor/GetData"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoiaG9lZnNkYXZpZDk3MDFAZ21haWwuY29tIiwiaHR0cDovL3NjaGVtYXMueG1sc29hcC5vcmcvd3MvMjAwNS8wNS9pZGVudGl0eS9jbGFpbXMvbmFtZWlkZW50aWZpZXIiOiI1MTM2ZmUxZS1mNmQ2LTQ4NGEtYTlkNC03ZTIyZWRhMzIwMzIiLCJuYmYiOiIxNjAyMjY5MTg3IiwiZXhwIjoiMTYwNDg2MTE4NyJ9.6RDXO-I_YInttDCQBqw9RXNwCZkcefiiyQZ8lmCZoSU"


resp = requests.get(url, headers=headers)

data = resp.json()
print(data)

#---------------------------------------------------------------------------------------------------
#POST requests to API
postURL = "https://weatherstationapi.azurewebsites.net/api/TemperatureSensor/InsertSet"
dataToSend = [{"temperature" : 85,"humidity":0.20,"timeCaptured" : "2020-10-19T12:00:00"},
              {"temperature" : 85,"humidity":0.20,"timeCaptured" : "2020-10-19T12:05:00"},
              {"temperature" : 87,"humidity":0.20,"timeCaptured" : "2020-10-19T12:10:00"}]

req = requests.post(url = postURL,json = dataToSend,headers = headers)
print(req.json())

