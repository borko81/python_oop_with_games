class TV:
    MAX_VOLUME = 100
    MAX_BRIGHT = 10

    def __init__(self):
        self.is_on = False
        self.bright = 0
        self.volume = 0
        self.programs = [2, 4, 5, 8, 10]
        self.current_chanel = 0
        self.mute = False

    def power(self):
        self.is_on = not self.is_on

    def increase_bright(self):
        if self.is_on and self.bright < self.MAX_BRIGHT:
            self.bright += 1
        else:
            print('TV is down')

    def decrease_bright(self):
        if self.is_on and self.bright >= 1:
            self.bright -= 1
        else:
            print('TV is down')

    def volume_up(self):
        if self.is_on and self.volume < self.MAX_VOLUME:
            self.mute = False
            self.volume += 1
        else:
            print('TV is down')

    def volume_down(self):
        if self.is_on and self.volume >= 1:
            self.volume -= 1
            if self.volume == 0:
                self.mute = True
        else:
            print('TV is down')

    def change_chanel(self, value):
        if not self.is_on:
            return
        if 0 <= value < len(self.programs):
            self.current_chanel = value
            print(self.programs[self.current_chanel])

    def mute(self):
        self.mute = not self.mute


if __name__ == '__main__':
    tv = TV()
    tv.power()
    tv.volume_up()
    tv.volume_down()
    print(tv.volume, tv.mute)
    tv.change_chanel(1)
