from FlightSimulator import FlightSimulator
import sys
from select import select
from time import sleep


class Generator(object):
    def __init__(self, flight_simulator):
        self.my_object = flight_simulator

    def __next__(self):
        return self.next()

    def next(self):
        yield self.my_object.draw_angle()


if __name__ == "__main__":
    angle = sys.argv[1]
    simulator = FlightSimulator(angle)
    while True:
            sleep(0.5)
            if sys.stdin in select([sys.stdin, ], [], [], 0)[0]:
                raise StopIteration()
            else:
                print "{} -> Current state".format(simulator.angle)
                print "{} -> State after correction".format(simulator.correct_angle())
                simulator.draw_angle()
                Generator(simulator).next()
