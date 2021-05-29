
#Majority Element
#Using Moore voting algorithm

class MooreVotingAlgorithm():
    def __init__(self, array):
        self.array = array
        self.candidate = 0
        self.counter = 0
        self.validityCounter = 0

    def validateCandidate(self):
        for i in range(0, len(self.array)):
            if self.array[i] == self.candidate:
                self.validityCounter += 1
        if self.validityCounter > len(self.array)//2:
            print("Maximum governance: ", self.candidate)
        else:
            print("No maximum governance")

    def getMaximumOccurance(self):
        for i in range(0, len(self.array)):
            if self.counter == 0:
                self.candidate = self.array[i]
            
            if self.array[i] == self.candidate:
                self.counter += 1
            else:
                self.counter -= 1

        self.validateCandidate()
        


array = [3, 3, 4, 2, 4, 4, 2, 4, 4]
obj = MooreVotingAlgorithm(array)
obj.getMaximumOccurance()
