#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
from collections import OrderedDict
import django

"""IMI, JSON küldő script!"""

__author__ = "Zsolt Laszlo"
__copyright__ = "Copyright 2017"
__credits__ = ["Zsolt Laszlo"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Zsolt Laszlo"
__email__ = "lzsolti1970@gmail.com"
__status__ = "Development"


class Teszt:
    def __init__(self):
        self.name = ""
        self.size = ""


class Teszt2(Teszt):
    def __init__(self):
        super().__init__()
        self.width = ""


t = Teszt()
t.name = "renew"
# print(t.name)

t3 = Teszt2()
t3.name = "mas valami"
# print(t3.name)
json_obj = OrderedDict({
    "typeSt": "CNG-1K",
    "idSt": "1",
    "schVer": "0.2",
    "time": "2017-06-10T09:25:00+01:00",
    "values": {
        "venVAP": "1",
        "venVst": "1",
        "venOdk1A": "1",

        "k1": "1",
        "k1mot": t.name,
        "vtr": "1",
        "vtrPor": "0",

        "pVst": "0.001",
        "pVys": "0.001",
        "tVys1": "0.001",
        "tSta": "0.001",

        "pVstPor": "1",
        "pVysPor": "1",
        "tVys1Por": "1",
        "tStaPor": "1",

        "aut": "1",
        "porSdr": "1",
    }
})

json_obj2 = {
    "typeSt": "CNG-1K",
    "idSt": "1",
    "schVer": "0.2",
    "time": "2017-06-10T09:25:00+01:00",
    "values": {
        "venVAP": "1",
        "venVst": "1",
        "venOdk1A": "1",

        "k1": "1",
        "k1mot": t.name,
        "vtr": "1",
        "vtrPor": "0",

        "pVst": "0.001",
        "pVys": "0.001",
        "tVys1": "0.001",
        "tSta": "0.001",

        "pVstPor": "1",
        "pVysPor": "1",
        "tVys1Por": "1",
        "tStaPor": "1",

        "aut": "1",
        "porSdr": "1",
    }
}

form = {
    "Email": "username",
    "Passwd": "password",
    "accountType": "GOOGLE",
    "source": "source",
    "service": "analytics"
}

json_obj3 = {}

json_obj3['typeSt'] = "CNG-1K"
json_obj3['idSt'] = 1
json_obj3['schVer'] = "0.2"
json_obj3['time'] = "2017-06-10T09:25:00+01:00"

json_obj3['values["venVAP"]'] = "123"
json_obj3['values["venVst"]'] = "10"
json_obj3['values["venOdk1A"]'] = 10
json_obj3['values["k1"]'] = 10
json_obj3['values["k1mot"]'] = "769"
json_obj3['values["vtr"]'] = 10
json_obj3['values["vtrPor"]'] = 10
json_obj3['values["pVst"]'] = 10
json_obj3['values["pVys"]'] = 10
json_obj3['values["tVys1"]'] = 10
json_obj3['values["tSta"]'] = 10
json_obj3['values["pVstPor"]'] = 10
json_obj3['values["pVysPor"]'] = 10
json_obj3['values["tVys1Por"]'] = 10
json_obj3['values["tStaPor"]'] = 10
json_obj3['values["aut"]'] = 10
json_obj3['values["porSdr"]'] = 10

# fo = open("teszt.json", "w+")
# json_data = '{"x": 9, "y": 11,"teszt_adatok": [{"teszt": "123"}], "name": "Brian", "city": "Seattle"}'
# python_obj = json.loads(json_data)
# print(python_obj)
# print(json.dumps(json_obj, sort_keys=False, indent=4))
# fo.write(json.dumps(python_obj, sort_keys=True, indent=4))
headers3 = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers2 = {'Content-Type': 'application/json'}
#r = requests.post(url='http://127.0.0.1:8080/imi.php', data=json.dumps(json_obj,
#                                                                    sort_keys=True, indent=4), headers=headers2)
# r = requests.post(url='http://127.0.0.1:8080/imi.php', json=json.dumps(json_obj,
#  sort_keys=True, indent=4), headers=headers3)

r = requests.post(url='http://192.168.1.6/imi.php', data=json_obj3)
#r.headers = headers2
# fo.close()
print(r.status_code)
# print(r.headers)
print(r.text + '...')
