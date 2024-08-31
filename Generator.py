from Parameters import *
from Sequence import *
from Layer import *



class Generator:
    def __init__(self, parameter: Parameters):
        print("Initialize the generator")
        self.taskQueue = []
        self.parameter = parameter
    
    ### add all registered layer into task queue
    def addAllTaskLayer(self):
        for layer in self.parameter.layer_register:
            self.taskQueue.append(self.parameter.layer_register[layer])
    ### execute the task queue
    def executeTaskLayers(self, sequence):
        for task in self.taskQueue:
            # apply layer modifications to comic sequence
            sequence = task.apply(sequence)

        return sequence

    # def framePage(self, sequence: Sequence):
    #     result = sequence
    #     return result
    # def addNewCharacter(self, character: Character):
    #     self.characterList.append(character)


