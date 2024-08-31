import random
from random import randint
# A Sample class with init method
class CompositionPool:
   
    # init method or constructor 
    def __init__(self):
        self.CompositionPool = {}
        # self.CompositionPool[0] = []
        # self.CompositionPool[1] = []
        # self.CompositionPool[2] = []

        # self.CompositionPool[0][0] = []
        # self.CompositionPool[0][1] = []
        # self.CompositionPool[0][2] = []
    def generateDefaultCompositions(self):
            # resultTransition = random.choice(transitions)
            resultComposition = randint(0, 0) 
            return resultComposition

    def generateRandCompositions(self):
        # resultTransition = random.choice(transitions)
        resultComposition = randint(0, 5) 
        return resultComposition

    def generateNonBasicCompositions(self):
        # resultTransition = random.choice(transitions)
        resultComposition = randint(1, 5) 
        return resultComposition