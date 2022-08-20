class LightSwitch:
    max_light = 10

    def __init__(self):
        self.state = False
        self.brightness = 0

    def turn_on(self):
        self.state = True

    def turn_off(self):
        self.state = False

    def raisebright(self):
        if self.brightness < self.max_light:
            self.brightness += 1

    def lowerbright(self):
        if self.brightness >= 1:
            self.brightness -= 1

    @property
    def show(self):
        return self.state, self.brightness


if __name__ == '__main__':
    one = LightSwitch()
    two = LightSwitch()
    print(one.show)
    one.turn_on()
    print(one.show)
    print(two.show)
    one.raisebright()
    one.lowerbright()
    one.lowerbright()
    print(one.show)
