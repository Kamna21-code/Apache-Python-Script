#!/usr/bin/python3

import cgi
import cgitb
import requests
import json
cgitb.enable()

print('Content-type: text/html\n\n')
req = requests.get("http://www.bom.gov.au/fwo/IDN60701/IDN60701.94592.json")

a = req.json()
pressure = []
temperature = []
for values in a['observations']['data']:
	pressure.append(values['press'])
for values in a['observations']['data']:
	temperature.append(values['air_temp'])

def avg(lis):
    return sum(lis)/len(lis)

print ("<h4>Maximum Pressure is {}</h4>".format(max(pressure)))
print ("<h4>Minimum Pressure is {}</h4>".format(min(pressure)))
print ("<h4>Average Pressure is{}</h4>".format(avg(pressure)))
print ("<h4>Maximum Pressure is {}</h4>".format(max(temperature)))
print ("<h4>Minimum Pressure is {}</h4>".format(min(temperature)))
print ("<h4>Average Pressure is{}</h4>".format(avg(temperature)))