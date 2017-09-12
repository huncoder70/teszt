#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This is a awesome
        python script!"""
import json
import requests
import time
from collections import OrderedDict
from pymodbus3.client.sync import ModbusTcpClient
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from time import sleep
__author__ = "Zsolt Laszlo"
__copyright__ = "Copyright 2016"
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

for i in range (0, 59):

    hiba_uzenet = ""
    args = {"host": "192.168.100.100", "port": 503}
    args3 = {"address": 16, "count": 9}

    mb2 = ModbusClient(**args)
    eredmeny_coils = mb2.read_coils(**args3)

    mb2.connection.close()
    print(eredmeny_coils)

    High_gas_concentration = "Shutdown	Vysoká koncentrace plynu-vypnutí!"
    Low_suction_pressure = "Nízký sací tlak"
    High_suction_pressure = "Vysoký sací tlak"
    High_gas_concentration = "Vysoká koncetrace plynu-alarm"
    High_gas_temperature = "Vysoká teplota plynu"
    High_outlet_pressure = "Vysoký výstupní tlak"
    Low_oil_pressure = "Nízký tlak oleje"
    High_oil_pressure = "Vysoký tlak oleje"
    Stopped_by_emergency_button = "Vypnutí havarijním STOP tlačítkem"

    if eredmeny_coils[0] == True:
        hiba_uzenet = Low_oil_pressure
    if eredmeny_coils[1] == True:
        hiba_uzenet = High_oil_pressure
    if eredmeny_coils[2] == True:
        hiba_uzenet = Low_suction_pressure
    if eredmeny_coils[3] == True:
        hiba_uzenet = High_gas_concentration
    if eredmeny_coils[4] == True:
        hiba_uzenet = High_gas_temperature
    if eredmeny_coils[5] == True:
        hiba_uzenet = High_suction_pressure
    if eredmeny_coils[6] == True:
        hiba_uzenet = Stopped_by_emergency_button
    if eredmeny_coils[7] == True:
        hiba_uzenet = High_outlet_pressure

    print(eredmeny_coils[6])
    for i in range(0, len(eredmeny_coils)):
        if eredmeny_coils[i] == True:
            server = smtplib.SMTP('smtp.seznam.cz', 25)
            server.starttls()
            server.login("cng.ceska.trebova@email.cz", "cng100CT")

            # msg = "Hello! Zsolti" # The /n separates the message from the headers
            fromaddr = "cng.ceska.trebova@email.cz"
            toaddr = "info@adastengineering.cz"
            msg = MIMEMultipart()
            msg['From'] = fromaddr
            msg['To'] = toaddr
            msg['Subject'] = "Compressor error!"
            body = hiba_uzenet
            msg.attach(MIMEText(body, 'plain'))
            text = msg.as_string()
            server.sendmail(fromaddr, toaddr, text)
            print(hiba_uzenet)
            print("OK")
            exit()

    sleep(1)



#server = smtplib.SMTP('smtp.gmail.com', 25)
#server.starttls()
#server.login("lzsolti1970", "1970vernice0801")
