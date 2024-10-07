# Load libraries
from machine import Pin, Timer

# Initialization of GPIO26 as input
sensor = Pin(26, Pin.IN, Pin.PULL_DOWN)

# Create timer
timer = Timer()

# Initialization of variables
counter = 0

print("KY-004 Button test")

# Function for counting keystrokes
def up(timer):
    global counter
    counter = counter + 1
    print(counter)

# Set debounce function around timer
def btn(pin):
    timer.init(mode=Timer.ONE_SHOT, period=200, callback=up)

# Initialization of the interrupt
sensor.irq(trigger=Pin.IRQ_FALLING, handler=btn)
