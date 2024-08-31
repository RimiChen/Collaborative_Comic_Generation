# import queue
import math
# import tkinter as tk
# from Tkinter import Tk, Frame, Canvas
# import ImageTk
from PyQt5.QtWidgets import *


import random
from random import randrange, randint
from PIL import Image, ImageTk

# processing program here
from typing import Sequence
from Parameters import *
from Panel import *
from Sequence import *
from Layer import *
from Grammar import *
from Actions import *
from Transitions import *
from Textbox import *
from EyePath import *
from Sentiment import *
from Scene import *
from ImageObj import *
from ImagePool import *


# parameters
DEFAULT_LENGTH = 5
IS_PAGE = False
DEFAULLT_WINDOW_HEIGHT = 800
DEFAULLT_WINDOW_WIDTH = 1200
PANEL_VERTIVAL_MAX = 2
PANEL_HORIZONTAL_MAX = 4
EQUAL_PANEL_HEIGHT = math.floor(DEFAULLT_WINDOW_HEIGHT / (PANEL_VERTIVAL_MAX+1))
EQUAL_PANEL_WIDTH = math.floor(DEFAULLT_WINDOW_WIDTH / (PANEL_HORIZONTAL_MAX+1))



# global window
# window = tk.Tk()


class Generator:
    def __init__(self):
        # self.taskQueue = queue.Queue()
        self.taskQueue = []
        self.characterList = []
        # self.window_h = DEFAULLT_WINDOW_HEIGHT
        # self.window_w = DEFAULLT_WINDOW_WIDTH
        # self.panel_h = EQUAL_PANEL_HEIGHT
        # self.panel_w = EQUAL_PANEL_WIDTH
        # self.defaultLength = DEFAULT_LENGTH
        # self.isPage = IS_PAGE

    def addTaskLayer(self, taskLayer: Layer):
        # self.taskQueue.put(taskLayer)
        self.taskQueue.append(taskLayer)

    def executeTaskLayers(self, sequence):
        for task in self.taskQueue:
            seuqnece = task.apply(sequence)

        # sequence.printSequence()

        return sequence

    def framePage(self, sequence: Sequence):
        result = sequence
        return result
    
    def addNewCharacter(self, character: Character):
        self.characterList.append(character)


def from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb

def getRandomColor():
    new_color = (randrange(256), randrange(256), randrange(256))
    return new_color

def getTopPos(center, side):
    top_x = center[0] - math.floor(side[0] / 2)
    top_y = center[1] - math.floor(side[1] / 2)
    
    return [top_x, top_y] 



def updatePanelColor(childFrame, color):
    childFrame.configure(bg = from_rgb(color))
    childFrame.update()


def getTopAndSizefromComposition(compositionList, parameter):
    
    top = [5000, 5000]
    side = [0, 0]

    for composition in compositionList:
        x = composition[0]
        y = composition[1]
        temp_top_min_x = parameter.compositionPool.CompositionPool[x][y][0]
        temp_top_min_y = parameter.compositionPool.CompositionPool[x][y][1]

        temp_top_max_x = temp_top_min_x + parameter.composition_w
        temp_top_max_y = temp_top_min_y + parameter.composition_h

        if temp_top_min_x <= top[0]:
            top[0] = temp_top_min_x
        if temp_top_min_y <= top[1]:
            top[1] = temp_top_min_y


        if temp_top_max_x >= top[0] + side[0]:
            side[0] = temp_top_max_x - top[0]
        if temp_top_max_y >= top[1] + side[1]:
            side[1] = temp_top_max_y - top[1]

        # print("top = ", parameter.compositionPool.CompositionPool[x][y])
    
    return [top, side]





def GUIterface(window_h, window_w, resultSequence, imagePoolList, parameter):
    print("SYSTEM: Lauch the interface")


    app = QApplication([])
    window = QWidget()


    layout = QVBoxLayout()
    layout.addWidget(QPushButton('Top'))
    layout.addWidget(QPushButton('Bottom'))
    
    
    window.setLayout(layout)
    window.show()
    app.exec()

    # global window
    # #window = tk.Tk()
    # window.title("Comic Generator")

    # page_frame = tk.Frame(master=window, width=window_w, height=window_h, background=from_rgb((200, 200, 200)))
    # page_frame.pack()

    # panelFrameList = {}
    # panelIndex = 0
    # for panel in resultSequence.panelQueue:
    #     # print(panel)

    #     # create panel back accoring to position
    #     new_panel_frame = tk.Frame(page_frame, width=EQUAL_PANEL_WIDTH, height=EQUAL_PANEL_HEIGHT, bg=from_rgb((255, 255, 255)), borderwidth=2)
    #     pos = getTopPos(panel.center, [EQUAL_PANEL_WIDTH, EQUAL_PANEL_HEIGHT])
    #     new_panel_frame.place(x = pos[0], y = pos[1])
    #     panelFrameList[str(panelIndex)] = new_panel_frame

    #     # print("-----Scene: ", panel.scene)
    #     targetScene = imagePoolList["Scene"].getImageObjFromDictionary(panel.scene)
    #     new_scene_Label = tk.Label(panelFrameList[str(panelIndex)], image = targetScene.getImageObj(), bg="grey")
    #     # window.wm_attributes("-transparentcolor", 'grey')
    #     new_scene_Label.place(x = 0, y = 0)        
    #     # print(new_panel_frame)
    #     # create character frame in the panel
    #     charaFrameList = {}
    #     for chara in panel.characterList:
    #         # self.compositionPosition = [[0,2]]
    #         [chara_top, chara_side] = getTopAndSizefromComposition(chara.compositionPosition, parameter)

    #         new_chara_frame = tk.Frame(panelFrameList[str(panelIndex)], width=chara_side[0], height=chara_side[1])
    #         new_chara_frame.place(x = chara_top[0], y = chara_top[1])
    #         charaFrameList[chara.characterName] = new_chara_frame
            
            
    #         targetChara = imagePoolList["Chara"].getImageObjFromDictionary(chara.characterName)
    #         new_charc_Label = tk.Label(charaFrameList[chara.characterName], image = targetChara.getImageObj(), bg="grey")
    #         # window.wm_attributes("-transparentcolor", 'grey')
    #         new_charc_Label.place(x = 0, y = 0)


    #         targetSymbol = imagePoolList["Symbol"].getImageObjFromDictionary(chara.action)
    #         # new_charc_Label = tk.Label(charaFrameList[chara.characterName], image = targetImage.getImageObj())

    #         # create_rectangle(0, 0, chara_side[0], chara_side[1], fill = "black", alpha = 0.0)
    #         new_symbol_label = tk.Label(charaFrameList[chara.characterName], image = targetSymbol.getImageObj(), bg="grey")
    #         new_symbol_label.place(x = 10 , y = 10)


    #     panelIndex = panelIndex + 1


    # window.mainloop()

def initialImagePools(parameter):
    image_default_height = parameter.composition_w
    image_default_width = parameter.composition_h
    image_default_top_x = 0
    image_default_top_y = 0


    default_character_depth = 0
    default_symbol_depth = 1
    default_scene_depth = -1

    characterImageRootPath = "Images/Characters/"
    symbolImageRootPath = "Images/Symbols/"
    sceneImageRootPath = "Images/Scenes/"


    # character pool
    imgCharaPool = ImagePool()

    newImageAlias = "chara_0"
    newImageFile = "chara_0.png"
    newImage = ImageObj([image_default_top_x, image_default_top_y], [image_default_width, image_default_height], default_character_depth, characterImageRootPath, newImageAlias, newImageFile)
    imgCharaPool.addImageToPool(newImageAlias, newImage)

    newImageAlias = "chara_1"
    newImageFile = "chara_1.png"
    newImage = ImageObj([image_default_top_x, image_default_top_y], [image_default_width, image_default_height], default_character_depth, characterImageRootPath, newImageAlias, newImageFile)
    imgCharaPool.addImageToPool(newImageAlias, newImage)


    newImageAlias = "chara_2"
    newImageFile = "chara_2.png"
    newImage = ImageObj([image_default_top_x, image_default_top_y], [image_default_width, image_default_height], default_character_depth, characterImageRootPath, newImageAlias, newImageFile)
    imgCharaPool.addImageToPool(newImageAlias, newImage)

    newImageAlias = "chara_3"
    newImageFile = "chara_3.png"
    newImage = ImageObj([image_default_top_x, image_default_top_y], [image_default_width, image_default_height], default_character_depth, characterImageRootPath, newImageAlias, newImageFile)
    imgCharaPool.addImageToPool(newImageAlias, newImage)    

    # symbol pool
    imgSymbolPool = ImagePool()

    newImageAlias = "angry"
    newImageFile = "angry.png"
    newImage = ImageObj([image_default_top_x, image_default_top_y], [image_default_width, image_default_height], default_symbol_depth, symbolImageRootPath, newImageAlias, newImageFile)
    imgSymbolPool.addImageToPool(newImageAlias, newImage)

    newImageAlias = "collide"
    newImageFile = "collide.png"
    newImage = ImageObj([image_default_top_x, image_default_top_y], [image_default_width, image_default_height], default_symbol_depth, symbolImageRootPath, newImageAlias, newImageFile)
    imgSymbolPool.addImageToPool(newImageAlias, newImage)


    newImageAlias = "dizzy"
    newImageFile = "dizzy.png"
    newImage = ImageObj([image_default_top_x, image_default_top_y], [image_default_width, image_default_height], default_symbol_depth, symbolImageRootPath, newImageAlias, newImageFile)
    imgSymbolPool.addImageToPool(newImageAlias, newImage)


    newImageAlias = "drink"
    newImageFile = "drink.png"
    newImage = ImageObj([image_default_top_x, image_default_top_y], [image_default_width, image_default_height], default_symbol_depth, symbolImageRootPath, newImageAlias, newImageFile)
    imgSymbolPool.addImageToPool(newImageAlias, newImage)


    newImageAlias = "eat"
    newImageFile = "eat.png"
    newImage = ImageObj([image_default_top_x, image_default_top_y], [image_default_width, image_default_height], default_symbol_depth, symbolImageRootPath, newImageAlias, newImageFile)
    imgSymbolPool.addImageToPool(newImageAlias, newImage)

    newImageAlias = "fall"
    newImageFile = "fall.png"
    newImage = ImageObj([image_default_top_x, image_default_top_y], [image_default_width, image_default_height], default_symbol_depth, symbolImageRootPath, newImageAlias, newImageFile)
    imgSymbolPool.addImageToPool(newImageAlias, newImage)

    newImageAlias = "fly"
    newImageFile = "fly.png"
    newImage = ImageObj([image_default_top_x, image_default_top_y], [image_default_width, image_default_height], default_symbol_depth, symbolImageRootPath, newImageAlias, newImageFile)
    imgSymbolPool.addImageToPool(newImageAlias, newImage)
    
    newImageAlias = "laugh"
    newImageFile = "happy.png"
    newImage = ImageObj([image_default_top_x, image_default_top_y], [image_default_width, image_default_height], default_symbol_depth, symbolImageRootPath, newImageAlias, newImageFile)
    imgSymbolPool.addImageToPool(newImageAlias, newImage)

    newImageAlias = "jump"
    newImageFile = "jump.png"
    newImage = ImageObj([image_default_top_x, image_default_top_y], [image_default_width, image_default_height], default_symbol_depth, symbolImageRootPath, newImageAlias, newImageFile)
    imgSymbolPool.addImageToPool(newImageAlias, newImage)

    newImageAlias = "roll"
    newImageFile = "roll.png"
    newImage = ImageObj([image_default_top_x, image_default_top_y], [image_default_width, image_default_height], default_symbol_depth, symbolImageRootPath, newImageAlias, newImageFile)
    imgSymbolPool.addImageToPool(newImageAlias, newImage)

    newImageAlias = "run"
    newImageFile = "run.png"
    newImage = ImageObj([image_default_top_x, image_default_top_y], [image_default_width, image_default_height], default_symbol_depth, symbolImageRootPath, newImageAlias, newImageFile)
    imgSymbolPool.addImageToPool(newImageAlias, newImage)

    newImageAlias = "cry"
    newImageFile = "sad.png"
    newImage = ImageObj([image_default_top_x, image_default_top_y], [image_default_width, image_default_height], default_symbol_depth, symbolImageRootPath, newImageAlias, newImageFile)
    imgSymbolPool.addImageToPool(newImageAlias, newImage)

    newImageAlias = "shock"
    newImageFile = "shock.png"
    newImage = ImageObj([image_default_top_x, image_default_top_y], [image_default_width, image_default_height], default_symbol_depth, symbolImageRootPath, newImageAlias, newImageFile)
    imgSymbolPool.addImageToPool(newImageAlias, newImage)

    newImageAlias = "sit"
    newImageFile = "sit.png"
    newImage = ImageObj([image_default_top_x, image_default_top_y], [image_default_width, image_default_height], default_symbol_depth, symbolImageRootPath, newImageAlias, newImageFile)
    imgSymbolPool.addImageToPool(newImageAlias, newImage)

    newImageAlias = "sleep"
    newImageFile = "sleep.png"
    newImage = ImageObj([image_default_top_x, image_default_top_y], [image_default_width, image_default_height], default_symbol_depth, symbolImageRootPath, newImageAlias, newImageFile)
    imgSymbolPool.addImageToPool(newImageAlias, newImage)        

    newImageAlias = "spit"
    newImageFile = "spit.png"
    newImage = ImageObj([image_default_top_x, image_default_top_y], [image_default_width, image_default_height], default_symbol_depth, symbolImageRootPath, newImageAlias, newImageFile)
    imgSymbolPool.addImageToPool(newImageAlias, newImage)        


    newImageAlias = "think"
    newImageFile = "think.png"
    newImage = ImageObj([image_default_top_x, image_default_top_y], [image_default_width, image_default_height], default_symbol_depth, symbolImageRootPath, newImageAlias, newImageFile)
    imgSymbolPool.addImageToPool(newImageAlias, newImage)        


    newImageAlias = "stand"
    newImageFile = "walk.png"
    newImage = ImageObj([image_default_top_x, image_default_top_y], [image_default_width, image_default_height], default_symbol_depth, symbolImageRootPath, newImageAlias, newImageFile)
    imgSymbolPool.addImageToPool(newImageAlias, newImage)        

    
    # scene image
    scene_default_x = 0
    scene_default_y = 0
    scene_default_height = parameter.panel_h
    scene_default_width = parameter.panel_w
    
    imgScenePool = ImagePool()

    newImageAlias = "forest"
    newImageFile = "003-Forest01.jpg"
    newImage = ImageObj([scene_default_x, scene_default_y], [scene_default_width, scene_default_height], default_scene_depth , sceneImageRootPath, newImageAlias, newImageFile)
    imgScenePool.addImageToPool(newImageAlias, newImage)        


    newImageAlias = "garden"
    newImageFile = "025-Castle01.jpg"
    newImage = ImageObj([scene_default_x, scene_default_y], [scene_default_width, scene_default_height], default_scene_depth , sceneImageRootPath, newImageAlias, newImageFile)
    imgScenePool.addImageToPool(newImageAlias, newImage)        


    newImageAlias = "beach"
    newImageFile = "005-Beach01.jpg"
    newImage = ImageObj([scene_default_x, scene_default_y], [scene_default_width, scene_default_height], default_scene_depth , sceneImageRootPath, newImageAlias, newImageFile)
    imgScenePool.addImageToPool(newImageAlias, newImage)        


    newImageAlias = "town"
    newImageFile = "018-MineTown02.jpg"
    newImage = ImageObj([scene_default_x, scene_default_y], [scene_default_width, scene_default_height], default_scene_depth , sceneImageRootPath, newImageAlias, newImageFile)
    imgScenePool.addImageToPool(newImageAlias, newImage)        


    newImageAlias = "room"
    newImageFile = "026-Castle02.jpg"
    newImage = ImageObj([scene_default_x, scene_default_y], [scene_default_width, scene_default_height], default_scene_depth , sceneImageRootPath, newImageAlias, newImageFile)
    imgScenePool.addImageToPool(newImageAlias, newImage)        


    return [imgCharaPool, imgSymbolPool, imgScenePool]



if __name__ == "__main__":

    # initial the tool and interface
    generator = Generator()
    # def __init__(self, window_h, window_w, panel_h, panel_w, defaultLength, isPage):    
    parameter = Parameters(DEFAULLT_WINDOW_HEIGHT, DEFAULLT_WINDOW_WIDTH, EQUAL_PANEL_HEIGHT, EQUAL_PANEL_WIDTH, DEFAULT_LENGTH, IS_PAGE, PANEL_HORIZONTAL_MAX, PANEL_VERTIVAL_MAX, DEFAULT_LENGTH)

# from Grammar import *
# from Actions import *
# from Transitions import *
# from Textbox import *
# from EyePath import *
# from Sentiment import *
# from Scene import *

    
    # Add task layers
    grammarLayer = Grammar("Grammar", parameter)
    generator.addTaskLayer(grammarLayer)
    actionLayer = Actions("Actions", parameter)
    generator.addTaskLayer(actionLayer)
    transitionsLayer = Transitions("Transitions", parameter)
    generator.addTaskLayer(transitionsLayer)            
    textboxLayer = Textbox("Textboxes", parameter)
    generator.addTaskLayer(textboxLayer)       
    eyePathLayer = EyePath("EyePath", parameter)
    generator.addTaskLayer(eyePathLayer)       
    sentimentLayer = Sentiment("Sentiment", parameter)
    generator.addTaskLayer(sentimentLayer)   
    sceneLayer = Scene("Scene", parameter)
    generator.addTaskLayer(sceneLayer)   


    # image pool
    # def __init__(self, imageRootPath):
    # def __init__(self, top, side, depth, imageRootPath, imgAlias, imageFileName):

    # character depth: 0
    # symbol depth: 1
    # default height = 128
    # default width = 128

    # [imgCharaPool, imgSymbolPool, imgScenePool] = initialImagePools(parameter)
    # print(imgCharaPool.imageDictionary)
    # print(imgSymbolPool.imageDictionary)

    # initial sequence
    # characterNum = randint(1 , imgCharaPool.getImagePoolLength())
    characterNum = randint(1, 2)
    # selectedChracterList = imgCharaPool.getRandomList(characterNum)
    # print(selectedChracterList)
    selectedChracterList = [
        "chara_1",
        "chara_2"
    ]


    sequence = Sequence(parameter, selectedChracterList)

    # initial character


    # generating comic sequence, controled by a button
    resultSequence = generator.executeTaskLayers(sequence)
    resultSequence.printSequence()

    # result = generator.framePage(sequence)
    # print(result)


    # initialized the GUI
    # print("SYSTEM: Lauch the interface")
    # # global window
    # window.title("Comic Generator")
    imagePoolList = {}
    # imagePoolList["Chara"] = imgCharaPool
    # imagePoolList["Symbol"] = imgSymbolPool
    # imagePoolList["Scene"] = imgScenePool
    # print(imagePoolList)

    GUIterface(DEFAULLT_WINDOW_HEIGHT, DEFAULLT_WINDOW_WIDTH, resultSequence, imagePoolList, parameter)
 
 
