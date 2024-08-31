from ImageObj import *
from random import randint

# A Sample class with init method
class Character:
   
    # init method or constructor 
    def __init__(self, characterName, parameter):
        # [x, y]
        self.imageObjList = []
        self.parameter = parameter

        self.characterName = characterName

        self.angle = 0
        # self.compositionPosition = [[0,1],[0,2]]
        self.compositionPosition = [[randint(0, 1),2]]
        self.textbox = 0

        # self.position = ""
        
        self.action = self.parameter.actionPool.getRandomAction(1)[0]
        
        
        # print("Initial-- charcter: ",self.characterName, "action: ", self.action, "at: ", self.compositionPosition)

   
    # Sample Method 
    def chanageAction(self, action):
        self.action = action
        # self.compositionPosition = 
    def adjustPosition(self, adjust_x, adjust_y, composition_index):
        target_composition = self.parameter.compositionPool.CompositionPool[composition_index]
        max_pos = len(target_composition)-1
        if adjust_x in target_composition:
            # enough panel
            max_level = target_composition[adjust_x]["level"]
        else:
            adjust_x = max_pos
            max_level = target_composition[adjust_x]["level"] 

        if self.compositionPosition[0][0] + adjust_x >=0 and self.compositionPosition[0][0] + adjust_x <=max_pos:
            self.compositionPosition[0][0] = self.compositionPosition[0][0] + adjust_x
        elif self.compositionPosition[0][0] + adjust_x < 0:
            self.compositionPosition[0][0] = 0
        elif self.compositionPosition[0][0] + adjust_x > max_pos:
            self.compositionPosition[0][0] = max_pos


        if self.compositionPosition[0][1] + adjust_y >=0 and self.compositionPosition[0][1] + adjust_y <=max_level:
            self.compositionPosition[0][1] = self.compositionPosition[0][1] + adjust_y
        elif self.compositionPosition[0][1] + adjust_y < 0:
            self.compositionPosition[0][1] = 0
        elif self.compositionPosition[0][1] + adjust_y > max_level:
            self.compositionPosition[0][1] = max_level

    def assignPosition(self, x, y):
        self.compositionPosition[0][0] = x
        self.compositionPosition[0][1] = y

    def addToImageList(self, imageObj: ImageObj):
        self.imageObjList.append(imageObj)

    def testMethod(self):
        print('The ImageObj class.')