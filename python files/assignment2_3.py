# Problem Set 3: plot showing time required by a StandardRobot to clean a 10x10 room
# Name: Mahbuba Tasmin
# Collaborators: None
from runSimulation import *
import matplotlib.pyplot as plt
import operator



def showPlot2_3():
     
  
    X = range(100,100000,1000)
    Y = []
 
    for numberOftrial in X:
        timeStep = runSimulation(1,1.0, 10,10,0.8,numberOftrial,0.5,StandardRobot,False)    
      
        Y.append(timeStep)
   
 
    plt.plot(X, Y)
    plt.xlabel('Number of iteration')
    plt.ylabel('Timesteps')
   
    plt.title('Time to clean 80% of a 10*10 room with a StandardRobot')
    plt.savefig('plot2_3.png')

    plt.show()


if __name__ == '__main__':
     showPlot2_3()
