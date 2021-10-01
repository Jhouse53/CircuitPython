import digitalio
import time
import board


intertupter_pin = digitalio.DigitalInOut(board.D8)
intertupter_pin.switch_to_input
intertupter_pin.pull = digitalio.Pull.UP


counter = 0
photo = False
state = False
max = 4

while True:
    photo = intertupter_pin.value
    if photo and not state:
        counter += 1
        print(str(counter))

    state = photo

    remaining = max - time.monotonic()

    if remaining <= 0:
        print(str(counter))
        max = time.monotonic() + 4
        counter = 0