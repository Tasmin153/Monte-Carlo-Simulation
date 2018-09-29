# Problem Set 4(b): plot showing dependence of cleaning time on various area of room by 2 robots
# Name: Mahbuba Tasmin
# Collaborators: None

from runSimulation import *
import matplotlib.pyplot as plt
import operator




def showPlot2():
   
    
    rooms = [(20, 20), (25, 16), (40, 10), (50, 8), (80, 5), (100, 4)]
    X = [20, 25, 40, 50, 80, 100]
    Y = []

    for width, height in rooms:
        timeStep = runSimulation(2, 1.0, width, height, 0.75,1000,0.5, StandardRobot, False)
        Y.append(timeStep)
     
    plt.plot(X, Y)
    plt.xlabel('Room shape')
    plt.ylabel('Timesteps')
    plt.title('Time to clean 80% of a room of area 400 with 2 robots, for various room shapes')
    plt.savefig('plot2.png')

    plt.show()


if __name__ == '__main__':
     showPlot2()
