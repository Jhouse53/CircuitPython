# CircuitPython
This repository will actually serve as a aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [Photointerrupter](#NextAssignment)
---

## Hello_CircuitPython

### Description & Code
This is a flashing multicolored LED

```python

import board
import neopixel
import time

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

dot.brightness = (0.1)

while True:
    print("Make it red!")
    dot.fill((255, 0, 0))
    time.sleep(.5)
    print("Make it blue!")
    dot.fill((0, 0, 255))
    time.sleep(.5)
    print("Make it red!")
    dot.fill((0, 225, 0))
    time.sleep(.5)

```


### Evidence

<img src="https://github.com/Jhouse53/CircuitPython/blob/main/GIF%20and%20Images/IMG_1004.gif?raw=true" alt="Neopixel light up" width="300">

Just need a board.

### Reflection
This was not that much of a challenge I could have done it an easier way looking back. But this was just the way I came up with that moment.



## CircuitPython_Servo

### Description & Code
Make a servo go back and forth within 180 degrees
```python
import touchio

touch_a4 = touchio.TouchIn(board.A4)
touch_a5 = touchio.TouchIn(board.A5)

pwm = pwmio.PWMOut(board.A2, duty_cycle=2**15, frequency=200)
MyServo = servo.Servo(pwm)
MyServo.angle = 90
angle = 90


```

### Evidence

<img src="https://github.com/Jhouse53/CircuitPython/blob/main/GIF%20and%20Images/capTouchServoGIF.gif?raw=true" alt="Neopixel light up" width="300">

### Wiring

<img src="https://github.com/Jhouse53/CircuitPython/blob/main/GIF%20and%20Images/SimpleServo%20Ciruit.PNG?raw=true" width="300">

### Reflection
This took me a while but I eventualy got it. I had a little trouble doing figuring out pwm. Once I understood the touch stuff and pwm it was easy from there.



## CircuitPython_UtraSonicSensor

### Description & Code

```python
 if distance >= 5 and distance < 20:
            red = int(simpleio.map_range(distance, 5, 20, 255, 0))
            blue = int(simpleio.map_range(distance, 5, 20, 0, 255))
            green = int(simpleio.map_range(distance, 5, 20, 0, 0))
        if distance >= 20 and distance < 35:
            red = int(simpleio.map_range(distance, 20, 35, 0, 0))
            blue = int(simpleio.map_range(distance, 20, 35, 255, 0))
            green = int(simpleio.map_range(distance, 20, 35, 0, 255))
        print(red,green,blue)
        dot.fill((red, green, blue))
```

### Evidence
<img src="https://github.com/inovotn04/CircuitPython/raw/main/Images/DistanceSensorEvidence.gif?raw=true" width="300">

Source:
[Ian github](https://github.com/inovotn04/CircuitPython/blob/main/README.md)

### Wiring
<img src="https://github.com/Jhouse53/CircuitPython/blob/main/GIF%20and%20Images/UltraSonicSensor%20wiring.PNG?raw=true" width="400">

### Reflection
I had a lot of problems with this one. There was random bugs that would fix themselves and it was really hard to get the distance function to work with the colors. If not for the hint on the canvas page I would have gotton stuck for a long time. Even after that I still had some problems but with the help of some classmates I got it.




## Photointerrupters

### Description & Code
I had no clue how to start this found I [github](https://github.com/gventre04/CircuitPython)from CHS student that I used for the code

```python
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
```

### Evidence

<img src="https://github.com/jmuss07/Circuit-Python/blob/main/Images/Photointerrupter_GIF.gif?raw=true" width="400">

<img src="https://github.com/jmuss07/Circuit-Python/blob/main/Images/Photointerrupter_Code_GIF.gif?raw=true" width="400">

Image Credit goes to [Josie Muss](https://github.com/jmuss07/Circuit-Python)


### Wiring
<img src="https://github.com/jmuss07/Circuit-Python/raw/main/Images/Photointerrupter.PNG?raw=true" width="400">

Image Credit goes to [Josie Muss](https://github.com/jmuss07/Circuit-Python)


### Reflection
I dind't ge this at all but with the help of the github stated earlier I actually understood how to do it and could get it done with some of their code. I still had some problems with it but with some review from classmates I got it.




## LCD 

### Description 
For LCD I needed to use two wires to control a set of numbers on a LCD screen one of the wires had to change the number and the other had to change whether or not the number moved up or down. To do that I used touchio and had a counter variable that would be added to by a different variable that would either be positive or negative depending on if the wire was hit. I got help from [Josie Muss](https://github.com/jmuss07/Circuit-Python#CircuitPython_LCD) for making sure that the wires didn't work when you were holding them down.

```python

import board
import time
import touchio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

# get and i2c object
i2c = board.I2C()

# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)

touchA0 = touchio.TouchIn(board.A0)
touchA4 = touchio.TouchIn(board.A4)

# The variable that will show up on the screen
Counter = 0
# The variable that determinds if it goes up or down
Switch = 1
# Booleans that makes sure that holding down the button doesn't increase the value.
# Got the idea from Jmuss07
SwitchB = 0
CounterB = 0

while True:
    if touchA0.value and SwitchB == 0:
        # Turns Switch value from positive to negative and vise versa 
        Switch = -Switch
        print("Touched A0")
        
    SwitchB = touchA0.value
    
    if Switch <= 0 and touchA4.value and CounterB == 0:
        print("Touched A4")
        lcd.clear()
        lcd.set_cursor_pos(0, 0)
        # Increases Counter value by the negative or positive Switch
        Counter += Switch
        lcd.print(str(Counter))
    CounterB = touchA4.value
    
    if Switch >= 0 and touchA4.value and CounterB == 0:
        print("Touched A4")
        lcd.set_cursor_pos(0, 0)
        Counter += Switch
        lcd.print(str(Counter))
```

### Wiring
<img src="https://github.com/jmuss07/Circuit-Python/raw/main/Images/LCD.PNG?raw=true" width="400">
+
Image Credit [Josie Muss](https://github.com/jmuss07/Circuit-Python#CircuitPython_LCD) 

### Evidence
<img src="https://github.com/inovotn04/CircuitPython/raw/main/Images/LCDGif.gif?raw=true" width="400">

Image Credit [Ian Novotne](https://github.com/inovotn04/CircuitPython/raw/main/Images/LCDGif.gif?raw=true)
