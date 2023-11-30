import dht
from machine import Pin
import time
import linenotify as ln
import network

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect('PALAKORN 2.4G', 'palakorn68')
while not wifi.isconnected():
    pass
print(wifi.ifconfig())

line = ln.LineNotify('Mmmdo5JGu2J0TaOLOr8MxDzUFVy5ww1vV7tHI6TlGcl')

fan = Pin(19, Pin.OUT)
pump = Pin(23, Pin.OUT)

pump.value(0)
fan.value(0)

while True:
    try:
        sensor = dht.DHT22(Pin(18))
        time.sleep(0.5)
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        
        print(temp)
        print(hum)
        line.notify('Humidity: ')
        line.notify(hum)
        line.notify('Temperature: ')
        line.notify(temp)
    except OSError as e:
        print("faild")
    
    if hum <= 60 and hum >= 50:
        if temp < 40:
            pump.value(1)
            time.sleep(10)
            pump.value(0)
            
        elif temp >= 50:
            fan.value(1)
            time.sleep(10)
            fan.value(0)
        
    elif hum > 60:
        fan.value(1)
        time.sleep(10)
        fan.value(0)
        
    elif hum < 50:
        pump.value(1)
        time.sleep(10)
        pump.value(0)
        
    time.sleep(2)
