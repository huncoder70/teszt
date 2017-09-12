##!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
import time
from collections import OrderedDict
from pymodbus3.client.sync import ModbusTcpClient



"""IMI, JSON küldő script!"""

__author__ = "Zsolt Laszlo"
__copyright__ = "Copyright 2017"
__credits__ = ["Zsolt Laszlo"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Zsolt Laszlo"
__email__ = "lzsolti1970@gmail.com"
__status__ = "Development"

class ModbusClient:
    def __init__(self, **kwargs):

        self.host = kwargs['host']
        self.port = kwargs['port']
        self.connection = ModbusTcpClient(self.host, self.port)

    def read_registers(self, **kwargs):

        response = self.connection.read_holding_registers(kwargs['address'], kwargs['count'])
        register = response.registers
        return register

    def read_coils(self, **kwargs):

        response = self.connection.read_coils(kwargs['address'], kwargs['count'])
        coils = response.bits
        return coils

szamitott_pvstpor = 0
szamitott_pvypor = 0
szamitott_tvy1por = 0
szamitott_tsta = 0

args = {"host": "192.168.100.100", "port": 503}
args2 = {"address": 0, "count": 20}
args3 = {"address": 0, "count": 30}

mb = ModbusClient(**args)
mb2 = ModbusClient(**args)
eredmeny_coils = mb2.read_coils(**args3)
eredmeny_registers = mb2.read_registers(**args2)
mb.connection.close()
#print(eredmeny_coils)
#print(eredmeny_registers)


result = eredmeny_registers
result2 = eredmeny_coils
localtime = time.asctime(time.localtime(time.time()))

fieldnames = ['PT-101',
              'PT-103',
              'PT-104',
              'TT-101',
              'TT-102',
              'TT-103',
              'TT-104',
              'TT-105',
              'TT-106',
              'TT-107',
              'TT-501',
              'FIT-101',
              'PT-501',
              'XT-501',
              'XT-502',
              'XT-503',
              'PT-201',
              'TT-201',
              'PT-151',
              'PT-152',
              'PT-251',
              'TT-151',
              'TT-451',
              'TT-251',
              'TT-452',
              'TT-453',
              'TT-454',
              'TT-455',
              'ST-551',
              'TIME']
dfdata = {}
for j in range(0, len(result)):
    result[j] /= float(10)
    dfdata[fieldnames[j]] = result[j]

dfdata[fieldnames[29]] = localtime


if result2[2] == "true":
    result2[2] = 1
else:result2[2] = 0

if result2[3] == "true":
    result2[3] = 1
else:result2[3] = 0

if result2[4] == "true":
    result2[4] = 1
else:result2[4] = 0

if result2[7] == "true":
    result2[7] = 1
else:result2[7] = 0

if result2[19] == "true" or result2[22] == "true":
    szamitott_pvstpor = 1

if result2[24] == "true":
    szamitott_pvypor = 1

if result2[21] == "true":
    szamitott_tvy1por = 1

if (result[13] * 10) > 50:
    szamitott_tsta = 1
json_obj = OrderedDict({
    "typeSt": "EO TREBOVA",  #EO TREBOVA
    "idSt": "100", #100
    "schVer": "0.2",
    "time": localtime,
    "values": {
        "venVAP": "1",
        "venVst": result2[2],
        "venOdk1A": result2[3],

        "k1": result2[4],
        "k1mot": result[17] * 10,
        "vtr": result2[7],
        "vtrPor": "0",

        "pVst": result[15]/10,
        "pVys": result[10]* 10,
        "tVys1": result[12] * 10,
        "tSta": result[13] * 10,

        "pVstPor": szamitott_pvstpor,
        "pVysPor": szamitott_pvypor,
        "tVys1Por": szamitott_tvy1por,
        "tStaPor": "1",

        "aut": "1",
        "porSdr": "1",
    }
})


json_obj3 = {}

json_obj3['typeSt'] = "EO TREBOVA"
json_obj3['idSt'] = "100"
json_obj3['schVer'] = "0.2"
json_obj3['time'] = localtime

json_obj3['values["venVAP"]'] = "1"
json_obj3['values["venVst"]'] = result2[2]
json_obj3['values["venOdk1A"]'] = result2[3]
json_obj3['values["k1"]'] = result2[4]
json_obj3['values["k1mot"]'] = result[17] * 10
json_obj3['values["vtr"]'] = result2[7]
json_obj3['values["vtrPor"]'] = "0"
json_obj3['values["pVst"]'] = result[15]/10
json_obj3['values["pVys"]'] = result[10]* 10
json_obj3['values["tVys1"]'] = result[12] * 10
json_obj3['values["tSta"]'] = result[13] * 10
json_obj3['values["pVstPor"]'] = szamitott_pvstpor
json_obj3['values["pVysPor"]'] = szamitott_pvypor
json_obj3['values["tVys1Por"]'] = szamitott_tvy1por
json_obj3['values["tStaPor"]'] = szamitott_tsta
json_obj3['values["aut"]'] = "1"
json_obj3['values["porSdr"]'] = "1"

#fo = open("teszt.json", "w+")

#print(json.dumps(json_obj, sort_keys=False, indent=4))

headers = {'content-type': 'application/json'}
#r = requests.post(url='http://www.adastzona.cz/kompresory.php', json=json.dumps(json_obj, sort_keys=True, indent=4), headers=headers)
#r = requests.post(url='http://imi.dev:8080/imi.php', data=json.dumps(json_obj, sort_keys=True, indent=4), headers=headers)
#r = requests.post(url='http://www.adastzona.cz:80/kompresory.php', json=json.dumps(json_obj))
r = requests.post(url='http://www.adastzona.cz:80/kompresory.php', data=json_obj3)


#fo.close()
print(r.status_code)
#print(r.headers)
print(r.text[:1000])