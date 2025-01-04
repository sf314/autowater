from gpiozero import LED
from time import sleep

# GPIOZERO mapping:
pumpPin1 = 17 # physical pin 11
pumpPin2 = 27 # physical pin 13
pumpPin3 = 22 # physical pin 15

durationLine1 = 4
durationLine2 = 4
durationLine3 = 4

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

print("Turning pump1 on for", durationLine1)
pump1.off()
sleep(durationLine1)
pump1.on()

print("Turning pump2 on for", durationLine2)
pump2.off()
sleep(durationLine2)
pump2.on()

print("Turning pump3 on for", durationLine3)
pump3.on()
sleep(durationLine3)
pump3.off()
