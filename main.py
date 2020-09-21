# ESP32 - Pin assignment
# i2c = I2C(scl=Pin(22), sda=Pin(21), freq=10000)
# ESP8266 - Pin assignment
from bme280 import BME280
from utime import sleep, time, localtime
from machine import I2C, Pin
import urequests
import network
import json

i2c = I2C(scl=Pin(26), sda=Pin(25), freq=10000)
sta_if = network.WLAN(network.STA_IF)
url_temp = 'https://cr3whome.herokuapp.com/api/temperature/'
url_hum = 'https://cr3whome.herokuapp.com/api/humidity/'
url_pres = 'https://cr3whome.herokuapp.com/api/pressure/'

headers = {'Content-type': 'application/json'}

def do_connect():
  if not sta_if.isconnected():
    print('connecting to network...')
    sta_if.active(True)
    sta_if.connect('Home-8', '0973039408')
    while not sta_if.isconnected():
      pass
  # print('network config:', sta_if.ifconfig())

while True:
  bme = BME280(i2c=i2c)
  temp = bme.temperature
  hum = bme.humidity
  pres = bme.pressure

  temp_data = {"value": float(temp), "room": 1 }
  hum_data = {"value": float(hum), "room": 1 }
  pres_data = {"value": float(pres), "room": 1 }

  if sta_if.isconnected():
    print("---- Ready to send ----")
    rt = urequests.post(url_temp, data=json.dumps(temp_data), headers=headers)
    rt.close()
    rh = urequests.post(url_hum, data=json.dumps(hum_data), headers=headers)
    rh.close()
    rp = urequests.post(url_pres, data=json.dumps(pres_data), headers=headers)
    rp.close()
    print("Temperature: {} C°".format(temp))
    print("Humidity: {} %".format(hum))
    print("Pressure: {} Hm".format(pres))
    print("------ Data sent ------")
    sleep(300)
  else:
    do_connect()
    print("Connection error!")
    sleep(3)




