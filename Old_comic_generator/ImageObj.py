# from PIL import Image, ImageTk
# import tkinter as tk

# A Sample class with init method
class ImageObj:
   
    # init method or constructor 
    def __init__(self, top, side, depth, imageRootPath, imgAlias, imageFileName):
        # [x, y]
        self.imageID = imgAlias
        self.top = top
        self.side = side
        self.depth = depth
        self.imageRootPath = imageRootPath
        self.isDisplay = True
        self.imageFileName = imageFileName
        self.imagePath = self.imageRootPath + imageFileName
        # print("$$$$$$$$   ", self.imagePath)
        # self.imageObj = Image.open(self.imagePath)

            # print(imagePoolList["Chara"].getImageObjFromDictionary(chara.characterName))
            # imageFromPool = Image.open(imagePoolList["Chara"].getImageObjFromDictionary(chara.characterName))
            # targetImage = imageFromPool.resize((parameter.composition_w, parameter.composition_h), Image.ANTIALIAS)
            # targetIamge = ImageTk.PhotoImage(targetImage)
        # print(self.imageObj)
        # self.resizedImage = self.imageObj.resize((self.side[0]-10, self.side[1]-10), Image.ANTIALIAS)
        # print("resize: ", self.resizedImage)
        # self.imagePhoto = ImageTk.PhotoImage(self.resizedImage)
        # self.imagePhoto = tk.PhotoImage(file = self.imagePath)

        # print("photo: ", self.imagePhoto)
        # print(self.imageObj)
        # self.imageAlias = imgAlias
   
    # Sample Method 
    def printPath(self):
        print(self.imagePath)
    def getPath(self):
        return self.imagePath

    def setIsDisplay(self, isDisplay: bool):
        self.isDisplay = isDisplay

    def testMethod(self):
        print('The ImageObj class.')

    # def getImageObj(self):
        # return self.imagePhoto