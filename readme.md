
## Prerequisites
Below instructions is for Mac users
1. Install `python3` and `pip3` and `homebrew` in your system
2. Run command `brew install mosquitto`- This will install mqtt broker locally
3. Run `pip3 install paho-mqtt` - This will instal python mqtt client
4. Run `brew install hivemq/mqtt-cli/mqtt-cli` - This is the cli interface for publishing/subscribing mqtt messages to broker

## Wiki

#### span_panel.py
This is a consumer client(localhost:1883) which is subscribed to
- Energy usage readings - The readings are aggregated and displayed
- Toggle vsp switch state every 5 seconds
- Subscribed to Energy_Usage topic

#### vsp.py
This is a producer client(localhost:1883) which
- Sends out energy consumption on 'Energy_Usage' mqtt topic every 1 sec
- Subscribed to Plug_State topic and displays the state whenever it changes
- Listens to hardware switch on/off message

Usage and Running the program:
1. Start MQTT broker locally
2. Run each of the programs in different tabs/terminal windows

To start the MQTT broker locally, run
```bash
$ /usr/local/opt/mosquitto/sbin/mosquitto -c /usr/local/etc/mosquitto/mosquitto.conf
```

Start the span panel program
```bash
$ python3 ./span-panel/span_panel.py
```

Start the switch program
```bash
$ python3 ./very-smart-plug/vsp.py
```

To manually send data to a particular topic using CLI command:
```bash
$ mqtt pub -t Plug_State -m "1"
```


