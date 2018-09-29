# Problem 3: Simulating robots
# Name: Mahbuba Tasmin
# Collaborators: None


from Robot import *
from Position import *
from ps6_visualize import *
from RectangularRoom import *


 

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,delay,
                  robot_type, visualize = False):
    
       
    totalTimeStepsInNumTrials = 0

## runs the program for the given number of trials

    for num_trial in xrange(num_trials):
        
        #if visualize:
           #anim = RobotVisualization(num_robots, width, height)
        robotRoom = RectangularRoom(width, height)
        numTotalTiles = robotRoom.getNumTiles()
        robotCollection = [robot_type(robotRoom, speed) for ind in range(num_robots)]
        current_coverage = 0.0 
       
## runs the loop until the given percentage of coverage is fulfilled

        while (current_coverage < min_coverage):
            totalTimeStepsInNumTrials =   totalTimeStepsInNumTrials +1
            for robot in robotCollection:
                robot.updatePositionAndClean()
             
                #if visualize:
                   #anim.update(robotRoom, robotCollection)
              
                current_coverage = float(robotRoom.getNumCleanedTiles())/numTotalTiles
                #print current_coverage
                
        #if visualize:
           #anim.done()
          
 
  
    return 1.0*totalTimeStepsInNumTrials/float(num_trials) 
        


#runSimulation(1, 1, 5, 5, 0.8, 1, 0.5,RandomWalkRobot,True)

 
