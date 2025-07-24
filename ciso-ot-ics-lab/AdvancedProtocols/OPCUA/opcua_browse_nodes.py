from opcua import Client
client = Client("opc.tcp://localhost:4840")
client.connect()
root = client.get_root_node()
print("Root node is:", root)
objects = client.get_objects_node()
print("Children of objects node:", objects.get_children())
client.disconnect()
