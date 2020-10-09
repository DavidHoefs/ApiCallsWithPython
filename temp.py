from gpiozero import CPUTemperature
import http.client
import datetime
import json
import ssl
import pprint

cpu = CPUTemperature()
conn = http.client.HTTPSConnection('192.168.0.110:45458',context = ssl._create_unverified_context())

headers = {'Content-type': 'application/json'}
for i in range(150):
    
    foo = {'temperature': i,'humidity':20,'timeCaptured': '2020-09-20T00:00:00'}
    json_data = json.dumps(foo,default=str)

    conn.request('POST', '/api/TemperatureSensor/PostData', json_data, headers)

    response = conn.getresponse()
    print(response.read().decode())
    print(cpu.temperature)
##connection = http.client.HTTPSConnection("192.168.0.110:45458",context = ssl._create_unverified_context())
##connection.request("GET", "/api/TemperatureSensor/GetData")
##response = connection.getresponse()
##print("Status: {} and reason: {}".format(response.status, response.reason))
##headers = response.getheaders()
##pp = pprint.PrettyPrinter(indent=4)
##pp.pprint("Headers: {}".format(headers))

conn.close()