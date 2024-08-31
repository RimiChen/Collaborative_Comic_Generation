import random

   # A Sample class with init method
class ScenePool:
    # init method or constructor 
    def __init__(self):
        self.ScenePool = {}
        self.initialScenePool()
    # def getRandomAction(self):

    def initialScenePool(self):
        self.ScenePool["forest"] = True
        # self.ScenePool["beach"] = True
        # self.ScenePool["town"] =True
        self.ScenePool["garden"] = True
        # self.ScenePool["room"] = True

    def getRandomScene(self, randomNumber):
        resultList = []
        while len(resultList) < randomNumber:
            selection = random.choice(list(self.ScenePool.keys()))
            if selection not in resultList:
                resultList.append(selection)
        
        # print(resultList)
        return resultList[0] 
