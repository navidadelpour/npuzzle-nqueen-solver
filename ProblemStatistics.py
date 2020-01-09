import time

class ProblemStatistics:

    startTime = 0
    timeElapsed = 0
    cost = 0
    accuracy = 0
    optimalCost = None
    isGoal = False

    def __init__(self):
        self.startTime = time.time()

    def calculate(self, answer, initialH):
        self.timeElapsed = time.time() - self.startTime
        self.accuracy = 1 - float(answer[1]) / float(initialH) if initialH and answer[1] else 1
        self.isGoal = answer[0].isGoal()
        self.cost = len(answer[2])
        if self.isGoal: self.optimalCost = self.cost 
    
    def report(self):
        return (self.isGoal, self.accuracy, self.timeElapsed, self.cost, self.optimalCost)

    def trace(self, data):
        solution, h, path, initialState = data
        print("------------------------------------------------")
        print("problem, h: \t\t" + str((initialState.getState(), initialState.heuristic())))
        print("solution, h: \t\t" + str((solution.getState(), solution.heuristic())))
        print("path: \t\t\t" + str(path))
        print("win: \t\t\t" + str(self.isGoal))
        print("cost: \t\t\t" + str(self.cost))
        print("optimal cost: \t\t" + str(self.optimalCost))
        print("accuracy: \t\t" + str('%.2f' % self.accuracy))
        print("time elapsed: \t\t" + str(int(self.timeElapsed * 1000)) + ' ms')
