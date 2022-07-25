# Broadcast its state whenever change is observed
# Broadcast its energy usage once per second

import paho.mqtt.client as mqtt 
from random import randrange, uniform
import time

LOCAL_HOST = "localhost"  #127.0.0.1
PORT = 1883 #mqtt broker port
PUBLISH_TOPIC_ENERGY_USAGE = "Energy_Usage"
SUBSCRIBE_TOPIC_PLUG_STATE = "Plug_State"

switch_state = 0    # variable to store plug state

# Called when a message has been received on a topic that the client subscribes to
def on_message(client, userdata, message):
    global switch_state
    print("Received plug state : " ,str(message.payload.decode("utf-8")))
    switch_state = int(message.payload.decode("utf-8"))

client = mqtt.Client("Very_Smart_Plug") # client name

# To set your local device as mqtt broker
mqttBroker = LOCAL_HOST
client.connect(mqttBroker, PORT)

client.subscribe(SUBSCRIBE_TOPIC_PLUG_STATE)  # client subscription to topic

# Energy usuage is generated as random number with precision 2
while True:
    client.loop_start()
    client.on_message=on_message
    if(switch_state == 0):
        randNumber = round(uniform(1.0, 2.0), 2) # between 1 to 2 when state is 0
    else:
        randNumber = round(uniform(10.0, 20.0), 2)  # between 10 to 20 when state is 1   
    client.publish(PUBLISH_TOPIC_ENERGY_USAGE, float(randNumber))
    print("Just published " + str(float(randNumber)) + " to topic Energy_Usage")
    time.sleep(1)
    client.loop_stop()