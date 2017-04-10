from FlightSimulator import FlightSimulator
from Generator import Generator
from time import sleep
import sys
from select import select


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
