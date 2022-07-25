# Control the VSP state ON/OFF
# Aggregate energy usage information for the VSP and display it

import paho.mqtt.client as mqtt
import time

ON = 1
OFF = 0
LOCAL_HOST = "localhost"  #127.0.0.1
PORT = 1883 #mqtt broker port
PUBLISH_TOPIC_PLUG_STATE = "Plug_State"
SUBSCRIBE_TOPIC_ENERGY_USAGE = "Energy_Usage"

aggregated_result = 0.0 # variable to store aggregated energy usage value

# Function to implement a threaded interface which runs in background
def loop_for_message(client):
	client.loop_start()
	client.on_message=on_message 
	time.sleep(5)
	client.loop_stop()

# Called when a message has been received on a topic that the client subscribes to
def on_message(client, userdata, message):
    global aggregated_result
    print("Received energy usage: " ,str(message.payload.decode("utf-8")))
    aggregated_result += round(float(message.payload.decode("utf-8")), 2)
    print("Aggregated Engergy = ", round(aggregated_result,2))

client = mqtt.Client("Span_Panel")	# client name

# To set your local device as mqtt broker
mqttBroker = LOCAL_HOST
client.connect(mqttBroker, PORT)

client.subscribe(SUBSCRIBE_TOPIC_ENERGY_USAGE)	# client subscription to topic

while True:
	client.publish(PUBLISH_TOPIC_PLUG_STATE, ON) # ON
	print("Published plug state 1")
	loop_for_message(client)
	client.publish(PUBLISH_TOPIC_PLUG_STATE, OFF)	# OFF
	print("Published plug state 0")
	loop_for_message(client)
