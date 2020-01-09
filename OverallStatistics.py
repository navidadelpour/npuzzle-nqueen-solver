
class OverallStatistics:

    overallWin = 0
    overallAccuracy = 0
    overallTime = 0
    overallCost = 0
    problemName = ""
    algorithm = ""
    testNum = 0

    def __init__(self, problemName, algorithm, testNum):
        self.problemName = problemName
        self.algorithm = algorithm
        self.testNum = testNum

    def add(self, problemStatistics):
        self.overallWin += 1 if problemStatistics.isGoal else 0
        self.overallAccuracy += problemStatistics.accuracy
        self.overallTime += problemStatistics.timeElapsed
        self.overallCost += problemStatistics.cost

    def report(self):
        print("------------------------------------------------")
        print "algorithm: \t\t" + str(self.algorithm)
        print "problem: \t\t" + str(self.problemName)
        print 'overall win: \t\t' + str(int(float(self.overallWin) / float(self.testNum) * 100)) + "%"
        print 'overall accuracy: \t' + str(int(float(self.overallAccuracy) / float(self.testNum) * 100)) + "%"
        print 'overall time: \t\t' + str(int((float(self.overallTime) / float(self.testNum)) * 1000)) + ' ms'
        print 'overall cost: \t\t' + str((float(self.overallCost) / float(self.testNum)))
        print("------------------------------------------------")
