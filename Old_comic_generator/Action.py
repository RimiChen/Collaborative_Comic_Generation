from ImageObj import *

# A Sample class with init method
class Action:
   
    # init method or constructor 
    def __init__(self, actionName, actionPositionLevel, actionSentimentLevel, action_x_adjust, action_y_adjust):
        # [x, y]
        self.imageObjList = []
        self.imageQueue = {}
        self.actionName = actionName
        self.action_x_adjust = action_x_adjust
        self.action_y_adjust = action_y_adjust
        self.actionPositionLevel = actionPositionLevel
        self.actionSentimentLevel = actionSentimentLevel
   
    def getPositionLevel(self):
        return self.actionPositionLevel
    # Sample Method 
    def addToImageList(self, imageObj: ImageObj):
        self.imageObjList.append(imageObj)

    def addToImageQueue(self, imageObj: ImageObj, position_modifier_x, position_modifier_y, imageName):
        self.imageQueue[imageName] ={}
        self.imageQueue[imageName]["imageObj"] = imageObj
        self.imageQueue[imageName]["pos_mod"] = [position_modifier_x, position_modifier_y]

    def testMethod(self):
        print('The ImageObj class.')