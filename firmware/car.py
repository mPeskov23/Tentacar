import RPi.GPIO as GPIO
import time

class Car:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        self.AIN1 = 23
        self.AIN2 = 24
        self.PWMA = 13

        self.BIN1 = 5
        self.BIN2 = 6
        self.PWMB = 19

        self.STBY = 21

        motor_pins = [self.AIN1, self.AIN2, self.BIN1, self.BIN2, self.PWMA, self.PWMB, self.STBY]
        for pin in motor_pins:
            GPIO.setup(pin, GPIO.OUT)

        GPIO.output(self.STBY, GPIO.HIGH)

        self.pwm_a = GPIO.PWM(self.PWMA, 1000)
        self.pwm_b = GPIO.PWM(self.PWMB, 1000)

        self.pwm_a.start(0)
        self.pwm_b.start(0)

        self.speed = 60

    def move_forward(self):
        GPIO.output(self.AIN1, GPIO.HIGH)
        GPIO.output(self.AIN2, GPIO.LOW)
        self.pwm_a.ChangeDutyCycle(self.speed)

        GPIO.output(self.BIN1, GPIO.HIGH)
        GPIO.output(self.BIN2, GPIO.LOW)
        self.pwm_b.ChangeDutyCycle(self.speed)

        time.sleep(0.5)

        self.stop()

    def stop(self):
        self.pwm_a.ChangeDutyCycle(0)
        self.pwm_b.ChangeDutyCycle(0)

    def turn_right(self, rotation=1):
        GPIO.output(self.AIN1, GPIO.LOW)
        GPIO.output(self.AIN2, GPIO.HIGH)
        self.pwm_a.ChangeDutyCycle(self.speed)

        GPIO.output(self.BIN1, GPIO.HIGH)
        GPIO.output(self.BIN2, GPIO.LOW)
        self.pwm_b.ChangeDutyCycle(self.speed)

        time.sleep(0.2 * rotation)
        self.stop()

    def turn_left(self, rotation=1):
        GPIO.output(self.AIN1, GPIO.HIGH)
        GPIO.output(self.AIN2, GPIO.LOW)
        self.pwm_a.ChangeDutyCycle(self.speed)

        GPIO.output(self.BIN1, GPIO.LOW)
        GPIO.output(self.BIN2, GPIO.HIGH)
        self.pwm_b.ChangeDutyCycle(self.speed)

        time.sleep(0.2 * rotation)
        self.stop()

    def cleanup(self):
        self.pwm_a.stop()
        self.pwm_b.stop()
        GPIO.cleanup()
  