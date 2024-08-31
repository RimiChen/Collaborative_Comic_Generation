import random
from Action import *

# A Sample class with init method
class ActionPool:
   
    # init method or constructor 
    def __init__(self, actionSentimentLevel, imagePool):
        self.ActionPool = {}
        self.actionSentimentLevel = actionSentimentLevel
        self.imagePool = imagePool
        print(self.imagePool)
    # def getRandomAction(self):
    def getRandomAction(self, randomNumber):
        resultList = []
        while len(resultList) < randomNumber:
            selection = random.choice(list(self.ActionPool.keys()))
            if selection not in resultList:
                resultList.append(selection)
        
        # print(resultList)
        return resultList 
    def createAction(self, actionName,actionPositionLevel, actionSentimentLevel, action_x_adjust, action_y_adjust):
    #    def __init__(self, actionName, actionPositionLevel, actionSentimentLevel, action_x_adjust, action_y_adjust):
        new_action = Action(actionName, actionPositionLevel, actionSentimentLevel, action_x_adjust, action_y_adjust)
        self.ActionPool[actionName] = new_action
        return new_action

    def getAction(self, actionName):
        return self.ActionPool[actionName]

    def initialActionPool(self):
        # self.actionIndex["eat"] = "0"
        # self.actionIndex["drink"] = "1"
        # self.actionIndex["run"] = "2"
        # self.actionIndex["collide"] = "3"
        # self.actionIndex["sit"] = "4"
        # self.actionIndex["dizzy"] = "5"
        # self.actionIndex["shock"] = "6"
        # self.actionIndex["stand"] = "7"
        # self.actionIndex["jump"] = "8"
        # self.actionIndex["laugh"] = "9"
        # self.actionIndex["cry"] = "10"
        # self.actionIndex["angry"] = "11"
        
        # #self.actionPool["Fall"] = "12"
        # #self.actionPool["Fly"] = "13"
        # #self.actionPool["Roll"] = "14"
        # #self.actionPool["Sleep"] = "15"
        # #self.actionPool["Think"] = "16"
        # #self.actionPool["Spit"] = "17"

        # at ground: adjstu_y = -1, move up: adjust_y = 1

        actionName = "stand"
        actionSentimentLevel = self.actionSentimentLevel[actionName]
        self.createAction(actionName,0, actionSentimentLevel, 0, 1)

        actionName = "eat"
        actionSentimentLevel = self.actionSentimentLevel[actionName]
        self.createAction(actionName,0, actionSentimentLevel, 0, 1)
        # def addToImageQueue(self, imageObj: ImageObj, position_modifier, imageName):
        imageName = "eat"
        imageObj = self.imagePool.getImageObjFromDictionary(imageName)
        self.ActionPool[actionName].addToImageQueue(imageObj, 0, 0, imageName)


        actionName = "drink"
        actionSentimentLevel = self.actionSentimentLevel[actionName]
        self.createAction(actionName,0, actionSentimentLevel, 0, 1)
        imageName = "drink"
        imageObj = self.imagePool.getImageObjFromDictionary(imageName)
        self.ActionPool[actionName].addToImageQueue(imageObj, 0, 0, imageName)

        actionName = "run"
        actionSentimentLevel = self.actionSentimentLevel[actionName]
        self.createAction(actionName,0, actionSentimentLevel, 1, 1)
        imageName = "run"
        imageObj = self.imagePool.getImageObjFromDictionary(imageName)
        self.ActionPool[actionName].addToImageQueue(imageObj, -1, 0, imageName)


        actionName = "collide"
        actionSentimentLevel = self.actionSentimentLevel[actionName]
        self.createAction(actionName,0, actionSentimentLevel, 0, 1)
        imageName = "collide"
        imageObj = self.imagePool.getImageObjFromDictionary(imageName)
        self.ActionPool[actionName].addToImageQueue(imageObj, 0.5, 0, imageName)


        actionName = "sit"
        actionSentimentLevel = self.actionSentimentLevel[actionName]
        self.createAction(actionName,0, actionSentimentLevel, 0, 1)
        imageName = "sit"
        imageObj = self.imagePool.getImageObjFromDictionary(imageName)
        self.ActionPool[actionName].addToImageQueue(imageObj, 0, 0, imageName)        

        actionName = "dizzy"
        actionSentimentLevel = self.actionSentimentLevel[actionName]
        self.createAction(actionName,0, actionSentimentLevel, 0, 1)
        imageName = "dizzy"
        imageObj = self.imagePool.getImageObjFromDictionary(imageName)
        self.ActionPool[actionName].addToImageQueue(imageObj, 0, 0.5, imageName)


        actionName = "jump"
        actionSentimentLevel = self.actionSentimentLevel[actionName]
        self.createAction(actionName,1, actionSentimentLevel, 0, -1)
        imageName = "jump"
        imageObj = self.imagePool.getImageObjFromDictionary(imageName)
        self.ActionPool[actionName].addToImageQueue(imageObj, 0, -0.75, imageName)


        actionName = "laugh"
        actionSentimentLevel = self.actionSentimentLevel[actionName]
        self.createAction(actionName,0, actionSentimentLevel, 0, 1)
        imageName = "laugh"
        imageObj = self.imagePool.getImageObjFromDictionary(imageName)
        self.ActionPool[actionName].addToImageQueue(imageObj, 0, -0.1, imageName)

        actionName = "cry"
        actionSentimentLevel = self.actionSentimentLevel[actionName]
        self.createAction(actionName,0, actionSentimentLevel, 0, 1)
        imageName = "cry"
        imageObj = self.imagePool.getImageObjFromDictionary(imageName)
        self.ActionPool[actionName].addToImageQueue(imageObj, 0, -0.1, imageName)


        actionName = "angry"
        actionSentimentLevel = self.actionSentimentLevel[actionName]
        self.createAction(actionName,0, actionSentimentLevel, 0, 1)
        imageName = "angry"
        imageObj = self.imagePool.getImageObjFromDictionary(imageName)
        self.ActionPool[actionName].addToImageQueue(imageObj, 0, 0.25, imageName)
        

        actionName = "fall"
        actionSentimentLevel = self.actionSentimentLevel[actionName]
        self.createAction(actionName,0, actionSentimentLevel, 0, 1)
        imageName = "fall"
        imageObj = self.imagePool.getImageObjFromDictionary(imageName)
        self.ActionPool[actionName].addToImageQueue(imageObj, 0, 0, imageName)


        actionName = "fly"
        actionSentimentLevel = self.actionSentimentLevel[actionName]
        self.createAction(actionName,1, actionSentimentLevel, 0, 1)
        imageName = "fly"
        imageObj = self.imagePool.getImageObjFromDictionary(imageName)
        self.ActionPool[actionName].addToImageQueue(imageObj, 0, 0.5, imageName)


        actionName = "roll"
        actionSentimentLevel = self.actionSentimentLevel[actionName]
        self.createAction(actionName,0, actionSentimentLevel, 1, 0)
        imageName = "roll"
        imageObj = self.imagePool.getImageObjFromDictionary(imageName)
        self.ActionPool[actionName].addToImageQueue(imageObj, -1, 0, imageName)


        actionName = "sleep"
        actionSentimentLevel = self.actionSentimentLevel[actionName]
        self.createAction(actionName,0, actionSentimentLevel, 0, 0)
        imageName = "sleep"
        imageObj = self.imagePool.getImageObjFromDictionary(imageName)
        self.ActionPool[actionName].addToImageQueue(imageObj, 0, 1, imageName)


        actionName = "think"
        actionSentimentLevel = self.actionSentimentLevel[actionName]
        self.createAction(actionName,0, actionSentimentLevel, 0, 0)
        imageName = "think"
        imageObj = self.imagePool.getImageObjFromDictionary(imageName)
        self.ActionPool[actionName].addToImageQueue(imageObj, 0, 1, imageName)


        actionName = "spit"
        actionSentimentLevel = self.actionSentimentLevel[actionName]
        self.createAction(actionName,0, actionSentimentLevel, 0, 0)
        imageName = "spit"
        imageObj = self.imagePool.getImageObjFromDictionary(imageName)
        self.ActionPool[actionName].addToImageQueue(imageObj, 0.5, 0, imageName)




        actionName = "shock"
        actionSentimentLevel = self.actionSentimentLevel[actionName]
        self.createAction(actionName,0, actionSentimentLevel, 0, 1)
        imageName = "shock"
        imageObj = self.imagePool.getImageObjFromDictionary(imageName)
        self.ActionPool[actionName].addToImageQueue(imageObj, 0, 0.5, imageName)
