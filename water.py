from gpiozero import LED
from time import sleep

# GPIOZERO mapping:
pumpPin1 = 17 # physical pin 11
pumpPin2 = 27 # physical pin 13
pumpPin3 = 22 # physical pin 15

# Pretend they're LEDs
print("Initializing pumps")
pump1 = LED(pumpPin1)
pump2 = LED(pumpPin2)
pump3 = LED(pumpPin3)

# Init
print("Turning all pumps off")
pump1.on()
pump2.on()
pump3.off()
sleep(1)

print("Turning pump1 on for 1s")
pump1.off()
pump2.off()
pump3.on()
sleep(1)
pump1.on()
pump2.on()
pump3.off()
print("Pump1 off")