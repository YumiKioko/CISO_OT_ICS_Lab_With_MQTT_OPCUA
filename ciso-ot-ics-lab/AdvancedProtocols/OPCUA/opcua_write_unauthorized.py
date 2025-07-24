from opcua import Client
from opcua.ua.uaerrors import UaStatusCodeError
client = Client("opc.tcp://localhost:4840")
client.connect()
try:
    node = client.get_node("ns=2;s=Motor.Speed")
    print("Original value:", node.get_value())
    node.set_value(9999)
    print("Value overwritten!")
except UaStatusCodeError as e:
    print("Write failed:", e)
client.disconnect()
