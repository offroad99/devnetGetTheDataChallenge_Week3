import json
import ipaddress
import os

#get python file path to open the json file
mypath = os.path.abspath(os.path.dirname(__file__))

try:
    with open(f'{mypath}/JSONdata') as f:
        jdata = json.load(f)
except:
    print("Cannot open JSONdata file")

for appliance in jdata:
    try: 
        bool(ipaddress.ip_address(appliance.get('lanIp')))
        print(f'{appliance.get("lanIp")} is a Valid IP Address for Serial #{appliance.get("serial")}') 
    except ValueError: 
        print(f'{appliance.get("lanIp")} is NOT a Valid IP Address for Serial #{appliance.get("serial")}') 




