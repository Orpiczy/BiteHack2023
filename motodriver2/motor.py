import wiringpi as wp

class Motor():
    def __init__(self, p1, p2):
        wp.wiringPiSetupGpio()
        wp.pinMode(p1, wp.GPIO.OUTPUT)
        wp.digitalWrite(p1, wp.GPIO.LOW)
        wp.pinMode(p2, wp.GPIO.OUTPUT)
        wp.digitalWrite(p2, wp.GPIO.LOW)
        self.p1 = p1
        self.p2 = p2

    def go(self, dir):
        if dir == 0:
            wp.digitalWrite(self.p1, wp.GPIO.LOW)
            wp.digitalWrite(self.p2, wp.GPIO.LOW)
        elif dir>0:
            wp.digitalWrite(self.p1, wp.GPIO.HIGH)
            wp.digitalWrite(self.p2, wp.GPIO.LOW)
        elif dir<0:
            wp.digitalWrite(self.p1, wp.GPIO.LOW)
            wp.digitalWrite(self.p2, wp.GPIO.HIGH)

