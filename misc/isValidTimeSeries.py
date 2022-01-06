"""
Given a grid of robot positions, indicate if it is a valid time series for the number of robots
specified if robots can only travel up to 1 index further than their position 1 step before. This

Input format: an array of arrays, of which each index can be 0 or 1. 
An index corresponds to the physical location which is either occupied by a robot(1) or empty(0)

Ex: 
Grid: [[1, 0, 0, 1], [0, 1, 1, 0]] is a valid time series for 2 robots because 
the first robot moved from index 0 to 1 and robot 2 moved from index 3 to 2

Grid: [[1, 0, 0, 0, 1], [1, 0, 1, 0, 0]] is not valid because the second robot started at index 4 but did not have a valid position on the next step 
"""


"""
Questions to ask: 
 - data input/ data format
 - constrains for data fields
 - are the array lengths the same 
 - are the number of robots can be 0 or negative
 - 
"""

"""
Two things must be done:
 - count the number of robots
 - check that they are valid and don't take the same time slot 
"""
def isValidTimeSeries(grid, numRobots):
    robots = 0

    for i in range(len(grid[0])):
        if grid[0][i] ==  1: 
            robots += 1
    if robots != numRobots: 
        return False
    
    # for i in range(len(grid[0])):
    #     if grid[0][i] == 1 and grid[1][i] != 1 and (grid[]: 
    #         print("1")
    for i in range(len(grid)):
        print("i", len(grid))
        for j in range(len(grid[0])):
            if grid[i][j] == 1 and i != len(grid) -1 and grid[i + 1][j] != 1 and j != len(grid[0]) and grid: 
                print(grid)
                
            
"""
 0  1  2  3
[1, 0, 0, 1]
[0, 1, 1, 0]

grid[0][i] == 1 and grid[1][i] != 1 and 
"""
    
    
    
    #print(grid[0][i])
        

    # def getRobotIndeces(gridRow):
    #     robotPositions = [0 for i in range(numRobots)]
    #     curRobot = 0 
    #     for i in range(len(gridRow)):
    #         if gridRow[i] == 1:
    #             curRobot += 1
    #             robotPositions[curRobot] = i
    #     return robotPositions

    # for i in range(len(grid)): 
    #    # print("i", i)
    #     #resets per row
    #     robotsPerRow = 0
    #     for j in range(len(grid[i])):
    #        # print("j",j)
    #         if grid[i][j] == 1: 
    #             robotsPerRow += 1
        
    #     print("robotsPerRow",robotsPerRow)
    #     if(robotsPerRow != numRobots):
    #         return False
    # print(grid[0])
    # currentRobotIndeces = getRobotIndeces(grid[0])
    # print(":",currentRobotIndeces)


    

    #print(len(grid[0]))

    #return(numRobots)


grid = [[1, 0, 0, 1], [0, 1, 1, 0]]
numRobots = 2
#return True bc 0 -> 1 and 3 -> 2 and none collide and all are valid 

print(isValidTimeSeries(grid, numRobots))