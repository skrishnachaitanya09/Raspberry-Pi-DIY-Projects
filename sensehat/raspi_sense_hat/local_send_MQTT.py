from sense_hat import SenseHat
import time
import paho.mqtt.client as paho
#import json


sense = SenseHat()

def on_connect(client, userdata, flags, rc):
    print('CONNACK received with code %d.' % (rc))
    
client = paho.Client()
client.on_connect = on_connect         
client.connect('192.168.1.150', 1883)

def on_publish(client, userdata, mid):
    print('mid:'+str(mid))
    
client.on_publish = on_publish 
        
client.loop_start()         
 
while True:
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()
    
    t = round(t, 1)
    p = round(p, 1)
    h = round(h, 1)
    
    info = "Temperature = %s, Pressure = %s, Humidity = %s"%(t, p, h)
    
    #sense.show_message(info, scroll_speed = 0.05)
    
    print(info)
          
    client.publish('/andrzej/sensorki', str(info))
    time.sleep(5)
    
    
