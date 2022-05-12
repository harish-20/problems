#This robot roams around a 2D grid. It starts at (0, 0) facing North. After each time it moves, the robot rotates 90 degrees clockwise. Given the amount the robot has moved each time, you have to calculate the robot's final position.
def robo(*moves):
    moves = list(moves)
    pos = [0,0]
    axis = 1
    print(moves)
    while axis <= len(moves):
        if((axis % 4) in [3,0]):
            moves[axis-1] = -moves[axis-1]
        pos[axis%2] += moves[axis-1]
        axis += 1
    return pos
print(robo(5,5,-5,-5,10,20,20))
