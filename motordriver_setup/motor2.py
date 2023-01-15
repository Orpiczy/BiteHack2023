from time import sleep
import wiringpi as wpi
class MotorDriver:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        wpi.wiringPiSetupGpio()
        wpi.pinMode(p1, wpi.GPIO.OUTPUT)
        wpi.digitalWrite(p1, wpi.GPIO.LOW)
        wpi.pinMode(p2, wpi.GPIO.OUTPUT)
        wpi.digitalWrite(p2, wpi.GPIO.LOW)

    def forward(self):
        wpi.digitalWrite(self.p1, wpi.GPIO.HIGH)
        wpi.digitalWrite(self.p2, wpi.GPIO.LOW)

    def stop(self):
        wpi.digitalWrite(self.p1, wpi.GPIO.LOW)
        wpi.digitalWrite(self.p2, wpi.GPIO.LOW)

    def reverse(self):
        wpi.digitalWrite(self.p1, wpi.GPIO.LOW)
        wpi.digitalWrite(self.p2, wpi.GPIO.HIGH)


class ChooseDirection:
    def __init__(self, m1_p1, m1_p2, m2_p1, m2_p2):
        self.m1 = MotorDriver(m1_p1, m1_p2)  # Set pin for motor1
        self.m2 = MotorDriver(m2_p1, m2_p2)  # Set pin for motor2

    def go_forward(self):
        self.m1.forward()
        self.m2.forward()

    def go_left(self):
        self.m1.forward()
        self.m2.stop()

    def go_right(self):
        self.m1.stop()
        self.m2.forward()

    def go_back(self):
        self.m1.reverse()
        self.m2.reverse()

    def stop(self):
        self.m1.stop()
        self.m2.stop()