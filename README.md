# CircuitPython
This repository will actually serve as a aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
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
This was pretty easy once I remebered how to code in Python.




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
This took me a while but I eventualy got it.



## CircuitPython_LCD

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
Ian github

https://github.com/inovotn04/CircuitPython/blob/main/README.md
### Wiring
<img src="https://github.com/Jhouse53/CircuitPython/blob/main/GIF%20and%20Images/UltraSonicSensor%20wiring.PNG?raw=true" width="400">
### Reflection
I had a lot of problems with this one. There was random bugs that would fix themselves and it was really hard to get the distance function to work with the colors. If not for the hint on the canvas page I would have gotton stuck for a long time.




## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection
