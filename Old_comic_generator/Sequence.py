from Character import *

# A Sample class with init method
class Sequence:
   
    # init method or constructor 
    def __init__(self, parameters, selectedCharacterList):
        self.panelQueue = []
        self.selectedCharacterList = selectedCharacterList
        self.defaultScene = parameters.scenePool.getRandomScene(1)
        self.isNarrative = False
        self.scorePath = {}
        self.actionPath = {}
        # self.actionDictionary = {}
        # self.actionNet = {}
        # self.actionPool = ActionPool().ActionPool
        # self.actionPool = parameters.actionPool
        # self.actionDictionary = parameters.actionDictionary
        # self.actionNet = parameters.actionNot 
   
    # Sample Method 
    def testMethod(self):
        print("apply ", self.layerName)

    def appendToSequence(self, panel):
        self.panelQueue.append(panel)
    
    def printSequence(self):
        # print(self.panelQueue)
        for panel in self.panelQueue:
            panel.printPanel()
            # print("grammar: ", panel.grammar, " center: ", panel.center)

    def getSequenceLength(self):
        return len(self.panelQueue)

    def addCaracterToList(self, character: Character):
        self.selectedCharacterList.append(character)
    # TODO remove        