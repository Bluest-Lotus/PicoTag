# Load libraries
from machine import Pin
from ir_tx.nec import NEC
from time import sleep

# Initialization from transmitter with NEC protocol to GPIO26
nec = NEC(Pin(16, Pin.OUT, value = 0))

# Variables for sending the data
address = 0x00
data = 0x34

print("KY-005 Infrared transmitter test")

while True:
    # Display transmission values
    print("Now it will be sent: Address=", hex(address),", Command=", hex(data))
    # Send data
    nec.transmit(address, data)
    # Increment send values
    data += 0x11
    # wait one second
    sleep(1)
