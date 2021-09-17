
import board
import time
import pwmio
import servo
import touchio

touch_a4 = touchio.TouchIn(board.A4)
touch_a5 = touchio.TouchIn(board.A5)

pwm = pwmio.PWMOut(board.A2, duty_cycle=2**15, frequency=200)
MyServo = servo.Servo(pwm)
MyServo.angle = 90
angle = 90

while True:
    if touch_a4.value:
        print("fowards!")
        if angle in range(0, 175):
            angle += 5
            MyServo.angle = angle
            print(angle)
        time.sleep(0.05)

    if touch_a5.value:
        print("back!")
        if angle in range(5, 180):
            angle -= 5
            MyServo.angle = angle
            print(angle)
            time.sleep(0.05)

    time.sleep(.05)