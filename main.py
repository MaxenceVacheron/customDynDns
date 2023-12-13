#!/usr/bin/env python3
# Credits to qupfer who posted this script on https://github.com/ovh/manager/issues/3919

# API DynDNS

# create token for GET and PUT (or more) https://www.ovh.com/auth/api/createToken
# prefilled url: https://api.ovh.com/createToken/index.cgi?GET=/*&PUT=/*&POST=/*&DELETE=/*

# get access

# AK number1
# AS number2
# CK number3

# pip install ovh
# pip install requests

#########################################

import ovh
import json
import os
from dotenv import load_dotenv

import requests

load_dotenv()

application_key = os.getenv('application_key')
application_secret = os.getenv('application_secret')
consumer_key = os.getenv('consumer_key')

zoneName="maxencevacheron.fr"
subDomain=""
interface="eth0"

newIP4=requests.get("https://api4.ipify.org").content.decode()
newIP6=requests.get("https://api6.ipify.org").content.decode()
print(f'{newIP4}\n{newIP6}')

client = ovh.Client(
    endpoint='ovh-eu',               # Endpoint of API OVH Europe (List of available endpoints)
    application_key=application_key,    # Application Key
    application_secret=application_secret, # Application Secret
    consumer_key=consumer_key,       # Consumer Key
)

result = client.get(f'/domain/zone/{zoneName}/record', fieldType='A',subDomain=subDomain)
recordID=result[0]
client.put(f'/domain/zone/{zoneName}/record/{recordID}',subDomain=subDomain,target=newIP4,ttl=0)

result = client.get(f'/domain/zone/{zoneName}/record', fieldType='AAAA',subDomain=subDomain)
recordID=result[0]
client.put(f'/domain/zone/{zoneName}/record/{recordID}',subDomain=subDomain,target=newIP6,ttl=0)


client.post(f'/domain/zone/{zoneName}/refresh')