# esptool.py --chip esp32 --port /dev/cu.SLAB_USBtoUART erase_flash
# esptool.py --chip esp32 --port /dev/cu.SLAB_USBtoUART --baud 460800 write_flash -z 0x1000 esp32-idf3-20191220-v1.12.bin
# file Desktop/Micropython
# os.listdir()) проверить файла на контроллере
# ampy -p /dev/cu.SLAB_USBtoUART ls // rm // put  somefile (просто в терминале)

""" BME """
# from machine import Pin, I2C
# from time import sleep
# import bme280 as BME280
#
# # ESP32 - Pin assignment
# i2c = I2C(scl=Pin(22), sda=Pin(21), freq=10000)
# # ESP8266 - Pin assignment
# #i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)
#
# while True:
#   bme = BME280.BME280(i2c=i2c)
#   temp = bme.temperature
#   hum = bme.humidity
#   pres = bme.pressure
#   # uncomment for temperature in Fahrenheit
#   #temp = (bme.read_temperature()/100) * (9/5) + 32
#   #temp = str(round(temp, 2)) + 'F'
#   print('Temperature: ', temp)
#   print('Humidity: ', hum)
#   print('Pressure: ', pres)
#
#   sleep(5)


""" Relay """
# from machine import Pin
# from time import sleep
#
# relay = Pin(12, Pin.OUT)
# # relay.value(1)
# #relay.on()
#
#
# while True:
#   # RELAY ON
#   relay.value(0)
#   sleep(3)
#   # RELAY OFF
#   relay.value(1)
#   sleep(3)

""" Neopixel """
# import machine, neopixel
# import time
# n = 10
# p = 12
#
# np = neopixel.NeoPixel(machine.Pin(p), n)
#
# while 1:
#
#     for x in range(10):
#         np[x] = (239, 255, 0)
#         np.write()
#     time.sleep(3)
#     for x in range(10):
#         np[x] = (255, 0, 255)
#         np.write()
#     time.sleep(3)
#     for x in range(10):
#         np[x] = (51, 255, 51)
#         np.write()
#     time.sleep(3)
#     print("Done")

""" DS18B20 """
#import time
# import ds18b20
# from ds18b20 import ds
#
# time.sleep(1)
# sensor=ds(pin=26) #creates sensor object set to default pin 2, units in Celcius, resolution 12 bit
# #sensor.addr, sensor.pin, sensor.unit, and sensor.res values are now available
# #you can change the object parameters by the following:
# #pin number - sensor.pin=[number]
# #unit - sensor.unit=['c'|'f']
# #resolution - sensor.res=[9|10|11|12]
#
# while True:
#     temp=ds18b20.read(sensor) # a time.sleep is builtin to the function to allow time to take the reading
#     #the builtin time.sleep is currently set to 1 second for all resolutions but will eventually
#     #take less time for the lower resolutions once it has been added to the library
#     print (temp)

""" Servo """
# from machine import Pin, PWM
# import utime
#
# servo = PWM(Pin(26), freq=50)
# servo.duty(600) # 27 127
#
# while True:
#     servo.duty(27)
#     utime.sleep(2)
#     servo.duty(129)
#     utime.sleep(2)

""" LED """
# from machine import Pin, PWM
# import utime
#
# p2 = Pin(26, Pin.OUT)
#
# while True:
#     p2.on()
#     utime.sleep(2)
#     print("off")
#     p2.off()
#     utime.sleep(2)
#     print("on")

""" Potenceometr """
# from machine import Pin, ADC
# from time import sleep
#
# pot = ADC(Pin(34))             # Pin 34 analog support
# pot.atten(ADC.ATTN_11DB)       #Full range: 3.3v
#
# while True:
#   pot_value = pot.read()
#   print(pot_value)
#   sleep(0.1)

""" Rotart (maybe doesnt work) """

