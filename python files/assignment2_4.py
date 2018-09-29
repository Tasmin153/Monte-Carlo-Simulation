# Problem Set 6: plot showing comparable performance of two types of robots on a single graph
# Name: Mahbuba Tasmin
# Collaborators: None
from runSimulation import *
import matplotlib.pyplot as plt
import operator
import numpy as np

def showPlot4():

    num_robots = 1
    speed = 1.0
    width, height = 10, 10
## np.linspace used to split the numbers within a given upper and lower limit
## range() works for integer numbers
    coverages = plt.np.linspace(0.1,1,10)
    num_trials = 10000
    for robot, name, color in [(StandardRobot, 'StandardRobot', 'blue'), (RandomWalkRobot,'RandomWalkRobot', 'red')]:
        Y = []
        for coverage in coverages:
            timeStep= runSimulation(num_robots, speed, width, height,coverage, num_trials,0.5, robot, False)
            Y.append(timeStep)
        plt.plot(coverages, Y, color=color, label=name)
    plt.xlabel('Percentage cleaned')
    plt.ylabel('Timesteps')
    plt.title('Time to clean various percentages of certain room, for each of StandardRobot and RandomWalkRobot')
    plt.legend(loc='upper right')
    plt.savefig('plot4.png')

    plt.show()






if __name__ == '__main__':
     showPlot4()
