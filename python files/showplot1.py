# Problem Set 4(a): plot showing dependence of cleaning time on various number of robots
# Name: Mahbuba Tasmin
# Collaborators: None
from runSimulation import *
import matplotlib.pyplot as plt
import operator



def showPlot1():
   
  
    X = range(1,11)
    Y = []
   
    for numberOfRobot in X:
        timeStep = runSimulation(numberOfRobot, 1.0, 20, 20,0.8,1000,0.5, StandardRobot,False)   
       
        Y.append(timeStep)
   
   
    plt.plot(X, Y)
    plt.xlabel('Number of robots')
    plt.ylabel('Timesteps')
    plt.title('Time to clean 80% of a 20*20 room with various robots, from 1 to 10')
    plt.savefig('plot1.png')

    plt.show()


if __name__ == '__main__':
     showPlot1()


