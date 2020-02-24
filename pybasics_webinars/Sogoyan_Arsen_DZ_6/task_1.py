import time


class TrafficLight:

    def __init__(self):
        self.__color = None
        self.pattern = ['red', 'yellow', 'green']
        self.running()

    def set_color(self, color, period):
        self.__color = color
        print(f'Traffic light is: {color}')
        time.sleep(period)

    def running(self):
        try:
            if self.pattern == ['red', 'yellow', 'green']:
                self.set_color(self.pattern[0], 7)
                self.set_color(self.pattern[1], 2)
                self.set_color(self.pattern[2], 5)
            else:
                raise Exception('Wrong color order')
        except Exception as e:
            exit(e)


a = TrafficLight()
