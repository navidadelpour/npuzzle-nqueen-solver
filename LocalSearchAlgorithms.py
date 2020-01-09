from NPuzzleProblem import NPuzzleProblem
from NQueenProblem import NQueenProblem
from ProblemStatistics import ProblemStatistics
from OverallStatistics import OverallStatistics
import random
import math
from pprint import pprint
import time
import sys

def hillClimbing(problem, hardrate):
    problemStatistics = ProblemStatistics()

    problem.generateRandomBoard(hardrate)
    initialH = problem.heuristic()
    current = (problem, initialH, [])
    answer = None
    
    while(True):
        successors = current[0].getSuccessors()
        successor = successors[0]
        if successor[1] >= current[1]:
            answer = current
            break
        current = (successor[0], successor[1], current[2] + successor[2])

    problemStatistics.calculate(answer, initialH)
    return (answer + (problem,), problemStatistics)

def simulatedAnnealing(problem, hardrate, isComplete):
    problemStatistics = ProblemStatistics()

    calls = 0
    maxCalls = 1000
    temperature = 10
    coolingRate = .3
    
    problem.generateRandomBoard(hardrate)
    initialH = problem.heuristic()
    current = (problem, initialH, [])
    answer = None

    while(True if isComplete else calls < maxCalls):
        answer = current
        if(current[0].isGoal()):
            break

        successors = current[0].getSuccessors()
        successor = successors[random.randrange(len(successors))]

        if(random.uniform(0, 1) < probability(successor[1], current[1], temperature)):
            current = (successor[0], successor[1], current[2] + successor[2])

        temperature = current[1] if isComplete else temperature - temperature * coolingRate
        calls += 1

    problemStatistics.calculate(answer, initialH)
    return (answer + (problem,), problemStatistics)

def probability(e1, e2, t):
    de = e2 - e1
    return 1 if de > 0 else math.exp(de / t)

def solve(args):
    testNum, problemName, problemFactor, algorithm, trace = args
    overallStatistics = OverallStatistics(problemName, algorithm, testNum)
    hardrate = 20
    isComplete = False

    if problemName == "NPuzzleProblem":
        problem = NPuzzleProblem(int(problemFactor))
    elif problemName == "NQueenProblem":
        problem = NQueenProblem(int(problemFactor))
    else:
        return

    for i in range (int(testNum)):
        if algorithm == 'hillClimbing':
            answer = hillClimbing(problem, hardrate)
        elif algorithm == 'simulatedAnnealing':
            answer = simulatedAnnealing(problem, hardrate, isComplete)
        else:
            return

        data, problemStatistics = answer

        overallStatistics.add(problemStatistics)
        trace == "true" and problemStatistics.trace(data)

    overallStatistics.report()

args = sys.argv
if len(args) > 5:
    solve(args[1:])
else:
    print(" * * * * * * * * * * * * NPuzzleProblem * * * * * * * * * * * * * *")

    solve([12, "NPuzzleProblem", 8, "hillClimbing", False])
    solve([12, "NPuzzleProblem", 8, "simulatedAnnealing", False])
    
    print(" * * * * * * * * * * * * NQueenProblem * * * * * * * * * * * * * *")
    
    solve([12, "NQueenProblem", 8, "hillClimbing", False])
    solve([12, "NQueenProblem", 8, "simulatedAnnealing", False])

