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
import board
import time
import pwmio
import servo

pwm = pwmio.PWMOut(board.A2, duty_cycle=2**15, frequency=200)
my_servo=servo.Servo(pwm)

while True:
    for angle in range(0, 180, 1):
        print("Forward")
        my_servo.angle=angle
        time.sleep(0.05)

    for angle in range(180, 0, -1):
        print("Back")
        my_servo.angle=angle
        time.sleep(0.05)

```

### Evidence

<img src="https://github.com/Jhouse53/CircuitPython/blob/main/GIF%20and%20Images/ServoGIF.gif?raw=true" alt="Neopixel light up" width="300">

### Wiring

<img src="https://github.com/Jhouse53/CircuitPython/blob/main/GIF%20and%20Images/SimpleServo%20Ciruit.PNG?raw=true" width="300">

### Reflection
This took me a while but I eventualy got it.



## CircuitPython_LCD

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection





## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection
