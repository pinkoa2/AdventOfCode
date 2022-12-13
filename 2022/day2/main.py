def part1():
    correspondingMap = {
        'A': 'ROCK',
        'B': 'PAPER',
        'C': 'SCISSORS',
        'X': 'ROCK',
        'Y': 'PAPER',
        'Z': 'SCISSORS',
        'ROCK': 1,
        'PAPER': 2,
        'SCISSORS': 3
    }
    LOSING_SCORE = 0
    DRAWING_SCORE = 3
    WINNING_SCORE = 6
    def calculateWinner(opMove, myMove):
        if(opMove == myMove):
            return DRAWING_SCORE
        if(opMove == 'ROCK' and myMove == 'PAPER'):
            return WINNING_SCORE
        if(opMove == 'ROCK' and myMove == 'SCISSORS'):
            return LOSING_SCORE
        if(opMove == 'PAPER' and myMove == 'SCISSORS'):
            return WINNING_SCORE
        if(opMove == 'PAPER' and myMove == 'ROCK'):
            return LOSING_SCORE
        if(opMove == 'SCISSORS' and myMove == 'ROCK'):
            return WINNING_SCORE
        if(opMove == 'SCISSORS' and myMove == 'PAPER'):
            return LOSING_SCORE
    def calculateScore(op, me):
        moveOfOp = correspondingMap[op]
        moveOfMe = correspondingMap[me]
        return correspondingMap[moveOfMe] + calculateWinner(moveOfOp, moveOfMe)
    myScore = 0
    with open('input.txt', 'r') as file:
        for line in file:
            inputString = line.strip()
            inputs = inputString.split(' ')
            myScore += calculateScore(inputs[0], inputs[1])
    print(myScore)

def part2():
    correspondingMap = {
        'A': 'ROCK',
        'B': 'PAPER',
        'C': 'SCISSORS',
        'X': 'LOSE',
        'Y': 'DRAW',
        'Z': 'WIN',
        'ROCK': 1,
        'PAPER': 2,
        'SCISSORS': 3,
        'LOSE': 0,
        'WIN': 6,
        'DRAW': 3
    }

    def getMyMove(opMove, goal):
        if( goal == 'WIN'):
            
            if(opMove == "ROCK"):
                return "PAPER"
            
            if(opMove == "SCISSORS"):
                return 'ROCK'

            if(opMove == 'PAPER'):
                return 'SCISSORS'

        if (goal == 'LOSE'):
            
            if(opMove == "ROCK"):
                return "SCISSORS"
            
            if(opMove == "SCISSORS"):
                return 'PAPER'

            if(opMove == 'PAPER'):
                return 'ROCK'

        return opMove

    def calculateScore(opMove, goal):
        moveOfOp = correspondingMap[opMove]
        myGoal = correspondingMap[goal]
        return correspondingMap[myGoal] + correspondingMap[getMyMove(moveOfOp, myGoal)]

    myScore = 0
    with open('input.txt', 'r') as file:
        for line in file:
            inputs = line.strip().split(' ')
            myScore += calculateScore(inputs[0], inputs[1])
    print(myScore)


part1()
part2()
