# Problem Set 6: plot showing comparable performance of two types of robots
# Name: Mahbuba Tasmin
# Collaborators: None

from runSimulation import *
import matplotlib.pyplot as plt
import operator
import numpy as np

def showPlot6():

    num_robots = 1
    speed = 1.0
    width, height = 25, 25
    ## np.linspace used to split the numbers within a given upper and lower limit
    coverages =  plt.np.linspace(0.1, 1.0, 10)
    num_trials = 100000
    for robot, name, color in [(StandardRobot, 'StandardRobot', 'blue'), (RandomWalkRobot,'RandomWalkRobot', 'red')]:
        Y = []
        for coverage in coverages:
            timeStep= runSimulation(num_robots, speed, width, height,coverage, num_trials,0.5, robot, False)
            Y.append(timeStep)
        plt.plot(coverages, Y, color=color, label=name)
    plt.xlabel('Percentage cleaned')
    plt.ylabel('Timesteps')
    plt.title('Time to clean various percentages of certain room, for each of StandardRobot and RandomWalkRobot')
    plt.legend(loc='upper left')
    plt.savefig('plot6.png')

    plt.show()






if __name__ == '__main__':
     showPlot6()
