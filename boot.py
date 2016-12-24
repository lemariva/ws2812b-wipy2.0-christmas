# boot.py -- run on boot-up
import os
import pycom
from machine import UART
from network import WLAN

uart = UART(0, 115200)
os.dupterm(uart)

pycom.heartbeat(False)

# wlan access
ssid_ = #### your_ssid
wp2_pass = #### your_password

# addressing (change the ###)
wipy_ip = '192.168.###.###'
wipy_mask = '255.255.255.0'
gateway_ip = '192.168.###.###'
dns_ip = '192.168.###.###'

# configure the WLAN subsystem in station mode (the default is AP)
wlan = WLAN(mode=WLAN.STA)
# go for fixed IP settings (IP, Subnet, Gateway, DNS)
wlan.ifconfig(config=(wipy_ip, wipy_mask, gateway_ip, dns_ip))
wlan.scan()     # scan for available networks
wlan.connect(ssid=ssid_, auth=(WLAN.WPA2, wp2_pass))

while not wlan.isconnected():
    pycom.rgbled(0xFF0000)      
    pass

pycom.rgbled(0x050505)  