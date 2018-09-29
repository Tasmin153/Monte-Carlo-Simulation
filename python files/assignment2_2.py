# Problem Set 2: plot showing time required by a RandomWalkRobot to clean a 10x10 room
# Name: Mahbuba Tasmin
# Collaborators: None
from runSimulation import *
import matplotlib.pyplot as plt
import operator



def showPlot2_2():
    
  
    X = range(100,10000,1000)
    Y = []
 
    for numberOftrial in X:
        timeStep = runSimulation(1,1.0, 10,10,0.8,numberOftrial,0.5, RandomWalkRobot,False)    
       
        Y.append(timeStep)
   
     
    plt.plot(X, Y)
    plt.xlabel('Number of iteration')
    plt.ylabel('Timesteps')
    plt.title('Time to clean 80% of a 10*10 room with a RandomWalkRobot')
    plt.savefig('plot2_2.png')

    plt.show()


if __name__ == '__main__':
     showPlot2_2()
