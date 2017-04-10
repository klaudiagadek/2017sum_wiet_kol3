import random
import sys
from select import select
from time import sleep


class FlightSimulator(object):

    def __init__(self, angle):
        self.angle = int(angle)
        self.max_angle = 90

    def draw_angle(self):
        self.angle = random.randint(1, 360)

    def correct_angle(self):
        if self.angle > self.max_angle:
            return self.angle % self.max_angle
        else:
            return self.angle

if __name__ == "__main__":
    angle = sys.argv[1]
    simulator = FlightSimulator(angle)
    print "Press enter to stop"
    while True:
        sleep(0.5)
        if sys.stdin in select([sys.stdin, ], [], [], 0)[0]:
            raise StopIteration()
        else:
            print "{} -> Current state".format(angle)
            print "{} -> State after correction".format(simulator.correct_angle())
            simulator.draw_angle()
