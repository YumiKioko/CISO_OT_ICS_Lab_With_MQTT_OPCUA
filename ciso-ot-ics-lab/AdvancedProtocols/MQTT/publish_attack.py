import paho.mqtt.client as mqtt

broker = "localhost"
topic = "factory/machine1/control"
message = "START"

client = mqtt.Client()
client.connect(broker, 1883, 60)

print(f"Publishing '{message}' to topic '{topic}'")
client.publish(topic, message)
client.disconnect()
