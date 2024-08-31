
from random import randrange, randint

# A Sample class with init method
class Panel:
   
    # init method or constructor 
    def __init__(self, top,  center, grammar, scene, transition, characterList, composition, modifyCount):
        # [x, y]

        self.modifyCount = modifyCount
        self.top = top
        self.center = center
        self.grammar =grammar
        self.narrativeScore = 0
        self.transition = transition
        self.sentimentLevel = ""
        self.composition = composition

        if self.grammar == "":
            self.sentimentLevel = 2
        elif self.grammar == "I":
            self.sentimentLevel = 2
        elif self.grammar == "L": 
            self.sentimentLevel = 4
        elif self.grammar == "P":
            self.sentimentLevel = 6 
        elif self.grammar == "E": 
            self.sentimentLevel = 2 

        self.scene= scene
        self.entityList = []
        self.characterList = characterList
        self.managePosition()

   
    # Sample Method
    def managePosition(self):
        positionCheck = {}

        for chara in self.characterList:
            current_x = chara.compositionPosition[0][0]
            current_y = chara.compositionPosition[0][1]

            if current_x not in positionCheck:
                positionCheck[current_x] = True
            else:
                new_x = randint(0, 1)
                while new_x in positionCheck:
                    new_x = randint(0, 1)
                
                chara.assignPosition(new_x, current_y)
                positionCheck[new_x] = True


    def updateCount(self):
        self.modifyCount = self.modifyCount + 1

    def testMethod(self):
        print('The Panel class.')
   
    def printPanel(self):
        print("===============================")
        print("Modified by ", self.modifyCount, " generting layers.")
        print("Position at (", self.top[0],", ", self.top[1], ").")
        print("Composition: ", self.composition,". ")     
        print("Grammar: ", self.grammar,". ")
        print("Tansition: ", self.transition)
        print("Scene: ", self.scene)
        for entity in self.entityList:
            print("--Enetity: ", entity)
        # print()
        for chara in self.characterList:
            print("--Charcter: ",chara.characterName, "action: ", chara.action, "at: ", chara.compositionPosition)


