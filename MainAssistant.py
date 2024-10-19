### import libraries

# import queue
# import os
# import imp
import importlib
import math
# import tkinter as tk
import kivy
from kivy.app import App
from kivy.graphics import Color, Rectangle
# from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.image import AsyncImage, Image
from kivy.config import Config
from kivy.uix.button import Button

import random
from random import randrange, randint

### import self-defined classes
from Parameters import*
from AttributeNode import *
from Sequence import *
from Generator import *
from Layer import *
from Models import *

DEFAULT_SEQUENCE_LENGTH = 4
DEFAULLT_WINDOW_HEIGHT = 800
DEFAULLT_WINDOW_WIDTH = 1200
### 3 menus + comic area
DEFAULT_MENU_WIDTH = DEFAULLT_WINDOW_WIDTH/6

PANEL_VERTIVAL_MAX = 2
PANEL_HORIZONTAL_MAX = 4

EQUAL_PANEL_HEIGHT = math.floor(DEFAULLT_WINDOW_HEIGHT / (PANEL_VERTIVAL_MAX+1))
EQUAL_PANEL_WIDTH = math.floor((DEFAULT_MENU_WIDTH*3) / (PANEL_HORIZONTAL_MAX+1))

DEFAULT_COMPOSITION_ALPHA = 0
FOLDER_PATH = "Image/"


### Renderer
class MainApp(App):
    def build(self):
        print(" Invoke kivy interface")

class GUIInterface():
    def __init__(self, parameter):
        print("SYSTEM: Lauch the application interface")
        self.app = MainApp()
        # # app.testFunction()
        # self.app.initailComicData(window_w, window_h, imagePoolList, parameter, generator)
        # app.generateNewComicSequence()
        self.app.run()

if __name__ == "__main__":

   
    ### ---------------
    # initial the tool and interface
    ###----------------

    ### Register all the parameters
    parameter = Parameters(DEFAULLT_WINDOW_WIDTH, DEFAULLT_WINDOW_HEIGHT, DEFAULT_MENU_WIDTH, DEFAULT_SEQUENCE_LENGTH)
    ### Initial Models
    parameter.addModel("Sentiment")    
    parameter.addModel("Img2ImgDiffusion")
    ### import ML Models
    parameter.importModelClass()
    models = Models(parameter)
    # Decide modules you want to import, register to module list    
    parameter.addModule("NarrativeGrammarLayer")
    parameter.addModule("PanelRelationLayer")
    parameter.addModule("StoryArcLayer")
    ### import modules
    parameter.importModules()
    ### Inital Sequence Model 
    seqeunce = Sequence("sequence", parameter)
    seqeunce.apply()
    ### Initial Generator, take layers
    generator = Generator(parameter)
    ### Import Visual Sets and Datas
    parameter.addVisuals("EmojiSet", FOLDER_PATH)
    ### Launch Renderer
    app = GUIInterface(parameter)