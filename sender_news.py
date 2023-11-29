
import paho.mqtt.client as mqttClient
import time
from scraper import *

blocks = scrape()


def on_connect(client, userdata, flags, rc):
     if rc == 0:
         print("Connected to broker")
         global Connected
         Connected = True

     else:
         print("Connection failed")


def on_publish(client, userdata, result):
     print("data published \n")
     pass

Connected = False
 # broker_address= "broker.hivemq.com"
broker_address = "localhost"  # Mosquitto en local
port = 1883

client = mqttClient.Client("Python_publisher")  # create new instance
client.on_connect = on_connect  # attach function to callback
client.on_publish = on_publish  # attach function to callback
client.connect(broker_address, port=port)  # connect to broker
client.loop_start()  # start the loop

while Connected != True:  # Wait for connection
     time.sleep(0.1)


try:     
         list_new = []
         for block in blocks:  
            value = {'Headline': block.get_attribute('aria-label'), 'url': block.get_attribute('href')}
            list_new.append(value)
            client.publish("test-/messagenews", payload=str(value))
            time.sleep(1)
         print("message published with success to News/Value")
         
except KeyboardInterrupt:
     print("sortir de la boucle exiting")
     client.disconnect()
     client.loop_stop()

