import can
import time

bus = can.interface.Bus(channel="can0", bustype="socketcan_native")

msgOn = can.Message(arbitration_id=0x6B2, data=[1], extended_id=False)
msgOff = can.Message(arbitration_id=0x6B2, data=[0], extended_id=False)

count = 0
while count < 3000:
    bus.send(msgOn)
    time.sleep(0.01)
    count += 10
bus.send(msgOff)
