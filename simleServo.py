
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