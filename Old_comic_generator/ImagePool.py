from ImageObj import *
import random
# A Sample class with init method
class ImagePool:
   
    # init method or constructor 
    def __init__(self):
        # [x, y]
        self.imageDictionary = {}
        # self.imageRootPath = imageRootPath
    # Sample Method 
    # def initImagePool():
    #     # def __init__(self, top, side, depth, imagePath, imgName):
    #     newImage = ImageObj([0, 0], [128, 128], 0, self.imageRootPath, )
        # self.compositionPosition = 
    def addImageToPool(self, imageAlias, imageObj: ImageObj):
        if imageAlias in self.imageDictionary:
            print("Error: ", imageAlias, " already exist!")
        else:
            self.imageDictionary[imageAlias] = imageObj

    def getImagePoolLength(self):
        return len(self.imageDictionary)
    
    def getRandomList(self, randomNumber):
        resultList = []
        while len(resultList) < randomNumber:
            selection = random.choice(list(self.imageDictionary.keys()))
            if selection not in resultList:
                resultList.append(selection)
        
        # print(resultList)
        return resultList

    def getImageObjFromDictionary(self, image_key):
        if image_key in self.imageDictionary:
            return self.imageDictionary[image_key]
            # return self.imageDictionary[image_key].getPath()
        else:
            return None

    def testMethod(self):
        print('The ImagePool class.')