# import queue
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

# from Tkinter import Tk, Frame, Canvas
# import ImageTk
import random
from random import randrange, randint
# from PIL import Image, ImageTk

# processing program here
from typing import Sequence
from Parameters import *
from Parameter_2 import *
from Panel import *
from Sequence import *
from Layer import *
from Grammar import *
from Actions import *
from Transitions import *
from Textbox import *
from StoryContent import *
from EyePath import *
from Sentiment import *
from Scene import *
from Compositions import *
from NarrativeArc import *
from ImageObj import *
from ImagePool import *


# parameters
DEFAULT_LENGTH = 5
IS_PAGE = False
DEFAULLT_WINDOW_HEIGHT = 800
DEFAULLT_WINDOW_WIDTH = 1200
DEFAULT_MENU_WIDTH = 300
PANEL_VERTIVAL_MAX = 2
PANEL_HORIZONTAL_MAX = 4
EQUAL_PANEL_HEIGHT = math.floor(DEFAULLT_WINDOW_HEIGHT / (PANEL_VERTIVAL_MAX+1))
EQUAL_PANEL_WIDTH = math.floor((DEFAULLT_WINDOW_WIDTH) / (PANEL_HORIZONTAL_MAX+1))

DEFAULT_COMPOSITION_ALPHA = 0

global window
# window = tk.Tk()
Config.set('graphics', 'resizable', '0')
  
# fix the width of the window 
Config.set('graphics', 'width', DEFAULLT_WINDOW_WIDTH + DEFAULT_MENU_WIDTH*2)
  
# fix the height of the window 
Config.set('graphics', 'height', DEFAULLT_WINDOW_HEIGHT)


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
            sequence = task.apply(sequence)

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



### Kivy sample code
class RootWidget(FloatLayout):

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(RootWidget, self).__init__(**kwargs)


# class MainApp(App):

#     def build(self):
#         self.root = root = RootWidget()
#         root.bind(size=self._update_rect, pos=self._update_rect)

#         with root.canvas.before:
#             Color(0, 1, 0, 1)  # green; colors range from 0-1 not 0-255
#             self.rect = Rectangle(size=root.size, pos=root.pos)
#         return root

#     def _update_rect(self, instance, value):
#         self.rect.pos = instance.pos
#         self.rect.size = instance.size
def coord_x(x, width):
    new_x = x - math.floor(width/2)
    return new_x
def coord_y(y, height):
    new_y = -(y - math.floor(height/2))
    return new_y

def panel_coord_x(x):
    new_x = x
    # new_x =300
    
    return new_x
def panel_coord_y(y):
    new_y = -(y)
    new_y = 400
    
    return new_y    

def coord_modify(orgin,  anchor_point, x, y, parent_width, parent_height, size_w, size_h):
    if orgin == "center":
        new_target_x = x - math.floor(parent_width/2)
        new_target_y = -(y - math.floor(parent_height/2))
    elif orgin == "left_top":
        # print("SYSTEM: follow normal coordinate, do nothign")
        new_target_x = x
        new_target_y = y
    elif orgin == "left_bottom":
        if anchor_point == "center":
            new_target_x = x - math.floor(size_w/2)
            new_target_y = parent_height - y - math.floor(size_h/2)
        elif anchor_point =="left_bottom":
            new_target_x = x
            new_target_y = parent_height - y
        elif anchor_point == "left_top":
            new_target_x = x
            new_target_y = parent_height - y - size_h 



    return [new_target_x, new_target_y]

class InnerLayout(FloatLayout):
    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(InnerLayout, self).__init__(**kwargs)
        self.size = kwargs["size"]
        self.pos = kwargs["pos"]

        # background
        with self.canvas.before:
            Color(0.5, 0.5, 0.5, 1)  # green; colors range from 0-1 instead of 0-255
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)

    def setColor(self, color):
        self.color = color

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

class InputLayout(FloatLayout):
    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(InputLayout, self).__init__(**kwargs)
        self.size = kwargs["size"]
        self.pos = kwargs["pos"]

        # background
        with self.canvas.before:
            Color(0, 0, 0, 1)  # green; colors range from 0-1 instead of 0-255
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)

    def setColor(self, color):
        self.color = color

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

class InputLayout2(FloatLayout):
    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(InputLayout2, self).__init__(**kwargs)
        self.size = kwargs["size"]
        self.pos = kwargs["pos"]

        # background
        with self.canvas.before:
            Color(0.25, 0.25, 0.25, 1)  # green; colors range from 0-1 instead of 0-255
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)

    def setColor(self, color):
        self.color = color

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size



class InterfaceLayout(FloatLayout):
    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(InterfaceLayout, self).__init__(**kwargs)
        self.size = kwargs["size"]
        self.pos = kwargs["pos"]

        # background
        with self.canvas.before:
            Color(1, 1, 1, 1)  # green; colors range from 0-1 instead of 0-255
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)

    def setColor(self, color):
        self.color = color

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


class PanelLayout(FloatLayout):
    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(PanelLayout, self).__init__(**kwargs)
        self.size = kwargs["size"]
        self.pos = kwargs["pos"]

        # background
        with self.canvas.before:
            Color(1, 1, 1, 0.5)  # green; colors range from 0-1 instead of 0-255
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)

    def setColor(self, color):
        self.color = color

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

class CompositionLayout(FloatLayout):
    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(CompositionLayout, self).__init__(**kwargs)
        self.size = kwargs["size"]
        self.pos = kwargs["pos"]

        # background
        with self.canvas.before:
            Color(0, 0, 1, DEFAULT_COMPOSITION_ALPHA)  # green; colors range from 0-1 instead of 0-255
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)

    def setColor(self, color):
        self.color = color

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size    

class MainApp(App):

    def build(self):

        # print("---------------SYSTEM: ", self.testString)

        resultSequence = self.generateNewComicSequence()
        resultSequence.printSequence()


        self.root = root = RootWidget()
        root.bind(size=self._update_rect, pos=self._update_rect)

        intereface_size_w = DEFAULLT_WINDOW_WIDTH + (DEFAULT_MENU_WIDTH * 3)
        interface_size_h = DEFAULLT_WINDOW_HEIGHT
        interface_panel = InterfaceLayout(size=(intereface_size_w, interface_size_h), pos = (0, DEFAULLT_WINDOW_HEIGHT - interface_size_h), size_hint=(None, None))
        root.add_widget(interface_panel)

        
        inner_back_w = DEFAULLT_WINDOW_WIDTH 
        inner_back_h = DEFAULLT_WINDOW_HEIGHT
        inner_back = InnerLayout(size=(inner_back_w , inner_back_h ), pos = (DEFAULT_MENU_WIDTH, DEFAULLT_WINDOW_HEIGHT - inner_back_h ), size_hint=(None, None))
        interface_panel.add_widget(inner_back)

        input_w = DEFAULT_MENU_WIDTH/2 
        input_h = DEFAULLT_WINDOW_HEIGHT
        input_back = InputLayout(size=(input_w , input_h ), pos = (0, DEFAULLT_WINDOW_HEIGHT - input_h ), size_hint=(None, None))
        interface_panel.add_widget(input_back)

        input_w_2 = DEFAULT_MENU_WIDTH/2 
        input_h_2 = DEFAULLT_WINDOW_HEIGHT
        input_back_2 = InputLayout2(size=(input_w_2 , input_h_2 ), pos = (input_w, DEFAULLT_WINDOW_HEIGHT - input_h ), size_hint=(None, None))
        interface_panel.add_widget(input_back_2)



        # reference_y = 200
        ### Add input image panels
        menu_count = 0

        input_height = input_h /6 
        input_width = input_w *0.8
        width_shift = 0.1 * input_w
        vertical_shift = input_height + 50

        input_button_h = 30
        input_button_w = input_width / 2
        button_height_shift = input_button_h
        button_width_shift = input_button_w
        
        input_top = 800
        index = 1
        # button_count = 1
        chara_input_1 = PanelLayout(size=(input_width, input_height), pos = (menu_count*input_w + width_shift, input_top - vertical_shift * index), size_hint=(None, None))
        # panelFrameList[str(panelIndex)] = new_panel_layout
        input_back.add_widget(chara_input_1)

        # selectedChracterList = [
        #     "chara_1",
        #     "chara_2"
        # ]

        targetChara = imagePoolList["Chara"].getImageObjFromDictionary("chara_1").getPath()
        # print("target_chara: ", targetChara)
        # print("==================================")
        img_x = menu_count*input_w + width_shift
        img_y = input_top - vertical_shift * index
        new_chara_image = Image(
            source= targetChara,
            size=(input_width,input_height),
            # pos = (reference_x+parent_shift_left, reference_y+parent_shift_top)
            pos = (img_x, img_y),
            )
        chara_input_1.add_widget(new_chara_image)


        import_button_L1 = Button(text ='Import', size =(input_button_w, input_button_h), pos = (menu_count*input_w + width_shift, input_top - vertical_shift * index - button_height_shift), background_normal ="", background_color =(37/255, 100/255, 77/255, 1), size_hint=(None, None))
        input_back.add_widget(import_button_L1)

        import_button_R1 = Button(text ='Modify', size =(input_button_w, input_button_h), pos = (menu_count*input_w + width_shift +button_width_shift, input_top - vertical_shift * index - button_height_shift), background_normal ="", background_color =(37/255, 80/255, 77/255, 1), size_hint=(None, None))
        input_back.add_widget(import_button_R1)


        index = 2
        # button_count = 2
        chara_input_2 = PanelLayout(size=(input_width, input_height), pos = (menu_count*input_w + width_shift, input_top - vertical_shift * index), size_hint=(None, None))
        # panelFrameList[str(panelIndex)] = new_panel_layout
        input_back.add_widget(chara_input_2)



        targetChara = imagePoolList["Chara"].getImageObjFromDictionary("chara_2").getPath()
        # print("target_chara: ", targetChara)
        # print("==================================")
        img_x = menu_count*input_w + width_shift
        img_y = input_top - vertical_shift * index
        new_chara_image = Image(
            source= targetChara,
            size=(input_width,input_height),
            # pos = (reference_x+parent_shift_left, reference_y+parent_shift_top)
            pos = (img_x, img_y),
            )
        chara_input_2.add_widget(new_chara_image)



        import_button_L2 = Button(text ='Import', size =(input_button_w, input_button_h), pos = (menu_count*input_w + width_shift, input_top - vertical_shift * index - button_height_shift), background_normal ="", background_color =(37/255, 100/255, 77/255, 1), size_hint=(None, None))
        input_back.add_widget(import_button_L2)

        import_button_R2 = Button(text ='Modify', size =(input_button_w, input_button_h), pos = (menu_count*input_w + width_shift +button_width_shift, input_top - vertical_shift * index - button_height_shift), background_normal ="", background_color =(37/255, 80/255, 77/255, 1), size_hint=(None, None))
        input_back.add_widget(import_button_R2)



        menu_count = menu_count + 1
        index = 1
        scene_input_1 = PanelLayout(size=(input_width, input_height), pos = (menu_count*input_w + width_shift, input_top - vertical_shift * index), size_hint=(None, None))
        # panelFrameList[str(panelIndex)] = new_panel_layout
        input_back_2.add_widget(scene_input_1)

        import_button_scene_L1 = Button(text ='Import', size =(input_button_w, input_button_h), pos = (menu_count*input_w + width_shift, input_top - vertical_shift * index - button_height_shift), background_normal ="", background_color =(37/255, 100/255, 77/255, 1), size_hint=(None, None))
        input_back_2.add_widget(import_button_scene_L1)

        import_button_scene_R1 = Button(text ='Modify', size =(input_button_w, input_button_h), pos = (menu_count*input_w + width_shift +button_width_shift, input_top - vertical_shift * index - button_height_shift), background_normal ="", background_color =(37/255, 80/255, 77/255, 1), size_hint=(None, None))
        input_back_2.add_widget(import_button_scene_R1)

        targetChara = imagePoolList["Scene"].getImageObjFromDictionary("garden").getPath()
        # print("target_chara: ", targetChara)
        # print("==================================")
        img_x = menu_count*input_w + width_shift
        img_y = input_top - vertical_shift * index
        new_chara_image = Image(
            source= targetChara,
            size=(input_width,input_height),
            # pos = (reference_x+parent_shift_left, reference_y+parent_shift_top)
            pos = (img_x, img_y),
            )
        scene_input_1.add_widget(new_chara_image)



        index = 2
        scene_input_2 = PanelLayout(size=(input_width, input_height), pos = (menu_count*input_w + width_shift, input_top - vertical_shift * index), size_hint=(None, None))
        # panelFrameList[str(panelIndex)] = new_panel_layout
        input_back_2.add_widget(scene_input_2)

        import_button_scene_L2 = Button(text ='Import', size =(input_button_w, input_button_h), pos = (menu_count*input_w + width_shift, input_top - vertical_shift * index - button_height_shift), background_normal ="", background_color =(37/255, 100/255, 77/255, 1), size_hint=(None, None))
        input_back_2.add_widget(import_button_scene_L2)

        import_button_scene_R2 = Button(text ='Modify', size =(input_button_w, input_button_h), pos = (menu_count*input_w + width_shift +button_width_shift, input_top - vertical_shift * index - button_height_shift), background_normal ="", background_color =(37/255, 80/255, 77/255, 1), size_hint=(None, None))
        input_back_2.add_widget(import_button_scene_R2)


        targetChara = imagePoolList["Scene"].getImageObjFromDictionary("forest").getPath()
        # print("target_chara: ", targetChara)
        # print("==================================")
        img_x = menu_count*input_w + width_shift
        img_y = input_top - vertical_shift * index
        new_chara_image = Image(
            source= targetChara,
            size=(input_width,input_height),
            # pos = (reference_x+parent_shift_left, reference_y+parent_shift_top)
            pos = (img_x, img_y),
            )
        scene_input_2.add_widget(new_chara_image)


        # reload_shift = 30
        reload_w = 200
        reload_h = 30

        new_position_w = inner_back_w + input_w + input_w_2
        reload_button = Button(text ='Generate', size =(reload_w, reload_h), pos = (new_position_w + (DEFAULT_MENU_WIDTH-(reload_w))/2, 50), background_normal ="", background_color =(156/255, 207/255, 83/255, 1), size_hint=(None, None))
        interface_panel.add_widget(reload_button)

        layer_button_1 = Button(text ='NarrativeGrammarLayer', size =(reload_w, reload_h), pos = (new_position_w + (DEFAULT_MENU_WIDTH-(reload_w))/2, 750), background_normal ="", background_color =(156/255, 207/255, 83/255, 1), size_hint=(None, None))
        interface_panel.add_widget(layer_button_1)

        layer_button_1 = Button(text ='StoryArcLayer', size =(reload_w, reload_h), pos = (new_position_w + (DEFAULT_MENU_WIDTH-(reload_w))/2, 700), background_normal ="", background_color =(156/255, 207/255, 83/255, 1), size_hint=(None, None))
        interface_panel.add_widget(layer_button_1)

        layer_button_2 = Button(text ='PanelRelationLayer', size =(reload_w, reload_h), pos = (new_position_w + (DEFAULT_MENU_WIDTH-(reload_w))/2, 650), background_normal ="", background_color =(156/255, 207/255, 83/255, 1), size_hint=(None, None))
        interface_panel.add_widget(layer_button_2)

        layer_button_3 = Button(text ='+', size =(reload_w, reload_h), pos = (new_position_w + (DEFAULT_MENU_WIDTH-(reload_w))/2, 600), background_normal ="", background_color =(156/255, 207/255, 83/255, 1), size_hint=(None, None))
        interface_panel.add_widget(layer_button_3)                


        panelFrameList = {}
        panelIndex = 0
        for panel in resultSequence.panelQueue:

            # print(panel)
            print("======================================")
            # create panel back accoring to position
            # new_panel_frame = tk.Frame(page_frame, width=EQUAL_PANEL_WIDTH, height=EQUAL_PANEL_HEIGHT, bg=from_rgb((255, 255, 255)), borderwidth=2)
            # pos = getTopPos(panel.center, [EQUAL_PANEL_WIDTH, EQUAL_PANEL_HEIGHT])
            pos = panel.center
            # new_panel_frame.place(x = pos[0], y = pos[1])
            # left, bottom
            [reference_x, reference_y] = coord_modify("left_bottom",  "center", panel.center[0], panel.center[1], DEFAULLT_WINDOW_WIDTH, DEFAULLT_WINDOW_HEIGHT, EQUAL_PANEL_WIDTH, EQUAL_PANEL_HEIGHT)
            reference_x = reference_x + DEFAULT_MENU_WIDTH
            # print("x= ", panel.center[0]," y= ", panel.center[1])
            # print("new_x = ",reference_x, " new_y= ", reference_y)

            # reference_x = 30
            # reference_y = 200
            new_panel_layout = PanelLayout(size=(EQUAL_PANEL_WIDTH,EQUAL_PANEL_HEIGHT), pos = (reference_x, reference_y), size_hint=(None, None))
            panelFrameList[str(panelIndex)] = new_panel_layout
            inner_back.add_widget(new_panel_layout)


            # print("-----Scene: ", panel.scene)
            targetScene = imagePoolList["Scene"].getImageObjFromDictionary(panel.scene).getPath()
            # print(targetScene)
            new_scene_Image =  Image(
                source= targetScene,
                size=(EQUAL_PANEL_WIDTH,EQUAL_PANEL_HEIGHT),
                pos = (reference_x, reference_y),
                allow_stretch = True,
                keep_ratio = False)
            # new_scene_Image.rescale(EQUAL_PANEL_WIDTH, EQUAL_PANEL_HEIGHT)


            new_panel_layout.add_widget(new_scene_Image)
            # new_scene_Label = tk.Label(panelFrameList[str(panelIndex)], image = targetScene.getImageObj(), bg="grey")
            # # window.wm_attributes("-transparentcolor", 'grey')
            # new_scene_Label.place(x = 0, y = 0) 

             # composition

            composition_mask_dictionary = {}
            # panel index, position
            # print("panel composition = ", panel.composition)
            for composition in self.parameter.compositionPool.CompositionPool[panel.composition]:
                

                new_left = self.parameter.compositionPool.CompositionPool[panel.composition][composition]["box"][0]
                new_top = self.parameter.compositionPool.CompositionPool[panel.composition][composition]["box"][1]
                new_w = self.parameter.compositionPool.CompositionPool[panel.composition][composition]["box"][2]
                new_h = self.parameter.compositionPool.CompositionPool[panel.composition][composition]["box"][3]
                parent_shift_left = new_panel_layout.pos[0]
                parent_shift_top = new_panel_layout.pos[1]
                # print(parent_shift_left)

                [new_left, new_top] = coord_modify("left_bottom",  "left_top", new_left , new_top, EQUAL_PANEL_WIDTH, EQUAL_PANEL_HEIGHT, new_w, new_h)

                # print("left: ", new_left, " top: ", new_top, " w: ", new_w, " h: ", new_h)
                new_composition_mask = CompositionLayout(size=(new_w,new_h), pos = (parent_shift_left+new_left, parent_shift_top+new_top), size_hint=(None, None))
                new_panel_layout.add_widget(new_composition_mask)

                # for this panel
                # composition_mask_dictionary[panel.composition] ={}
                if composition not in composition_mask_dictionary:
                    composition_mask_dictionary[composition] = {}
                    composition_mask_dictionary[composition]["panel"] = new_composition_mask
                    composition_mask_dictionary[composition]["box"] = self.parameter.compositionPool.CompositionPool[panel.composition][composition]["box"]
                    composition_mask_dictionary[composition]["level"] = self.parameter.compositionPool.CompositionPool[panel.composition][composition]["level"]
                    
                else:
                    composition_mask_dictionary[composition]["panel"] = new_composition_mask
                    composition_mask_dictionary[composition]["box"] = self.parameter.compositionPool.CompositionPool[panel.composition][composition]["box"]
                    composition_mask_dictionary[composition]["level"] = self.parameter.compositionPool.CompositionPool[panel.composition][composition]["level"]
            
            # print("composition mask dictionary: ", composition_mask_dictionary)
            
            # print("Character list: ", panel.characterList)
            
            charaFrameList = {}
            for chara in panel.characterList:
                # self.compositionPosition = [[0,2]]
                # composition = panel.composition
                # print(panel.composition)
                action = chara.action
                # print("action: ", action)
                action = parameter.checkList(action)
                height_level = self.parameter.actionPool.getAction(action).getPositionLevel()
                # print("height_level:", height_level)
                chara_position = chara.compositionPosition[0][0]
                # print("chara_position_x:", chara.compositionPosition[0][0], " chara_position_y: ", chara.compositionPosition[0][1])
                # print("panel index: ", panelIndex)
                # max_pos = len(composition_mask_dictionary) -1
                # print("max_pos: ", max_pos)

                target_composition = composition_mask_dictionary[chara_position]
                target_composition_mask = target_composition["panel"]
                mask_level_total = target_composition["level"]

                # print("target_composition_mask: ", target_composition_mask)

                # print(self.parameter.compositionPool.CompositionPool)
                # print("===============================")
                # print(self.parameter.compositionPool.CompositionPool[panel.composition])

                # position (center)
                new_left = target_composition["box"][0]
                new_top = target_composition["box"][1]
                new_w = target_composition["box"][2]
                new_h = math.floor(target_composition["box"][3]/mask_level_total)

                if new_w < new_h:
                    new_w = new_h
                else:
                    new_h = new_w


                # reference_x = new_left
                # reference_y = new_top

                
                # print("compostion: ", composition, " position: ", chara_position)
                # parent_composition_mask = composition_mask_dictionary[chara_position]["panel"]
                
                
                # center
                parent_shift_left = target_composition_mask.pos[0]
                parent_shift_top = target_composition_mask.pos[1]
                # reference_x =  coord_modify("center",  "center", parent_shift_left, parent_shift_top, new_w, new_h, new_w, new_h)
                reference_x =  parent_shift_left

                # back to low position (2)
                reference_y = (parent_shift_top) - math.floor(target_composition["box"][3]/2) + math.floor(new_h/2)
                reference_y = reference_y + new_h * height_level
                #  +  (new_h* (mask_level_total - height_level))


                
                # print("x:", reference_x, " y: ", reference_y)
                # print("parent_shift_left: ", parent_shift_left, "parent_shift_top: ", parent_shift_top)

                targetChara = imagePoolList["Chara"].getImageObjFromDictionary(chara.characterName).getPath()
                # print("target_chara: ", targetChara)
                # print("==================================")
                new_chara_image = Image(
                    source= targetChara,
                    size=(new_w,new_h),
                    # pos = (reference_x+parent_shift_left, reference_y+parent_shift_top)
                    pos = (reference_x, reference_y),
                    )
                target_composition_mask.add_widget(new_chara_image)

                targetAction = parameter.actionPool.ActionPool[action]
                # print("action obj: ", targetAction, " action name:", targetAction.actionName)
                # print(targetAction.imageQueue)



                for img in targetAction.imageQueue:
                    target_image = targetAction.imageQueue[img]["imageObj"].getPath()
                    # print(target_image)
                    mod_x = reference_x +math.floor(new_w * targetAction.imageQueue[img]["pos_mod"][0])
                    mod_y = reference_y +math.floor(new_h * targetAction.imageQueue[img]["pos_mod"][1])
                    new_action_image = Image(
                        source= target_image,
                        size=(new_w,new_h),
                        # pos = (reference_x+parent_shift_left, reference_y+parent_shift_top)
                        pos = (mod_x, mod_y),
                    )
                    target_composition_mask.add_widget(new_action_image)

                if chara.textbox in parameter.text_list:
                    # if textbox exist
                    targetText = parameter.text_list[chara.textbox]["name"]
                    targetText_image = imagePoolList["Text"].getImageObjFromDictionary(targetText).getPath()
                    mod_x = reference_x +math.floor(new_w * 0)
                    mod_y = reference_y +math.floor(new_h * 1.25)

                    new_text_image = Image(
                        source= targetText_image ,
                        size=(new_w,new_h),
                        # pos = (reference_x+parent_shift_left, reference_y+parent_shift_top)
                        pos = (mod_x, mod_y),
                        )
                    target_composition_mask.add_widget(new_text_image)

                # targetAction = parameter.actionPool.ActionPool[action]               
                
                # charaFrameList[chara.characterName] = new_chara_frame        
            panelIndex = panelIndex + 1

        ## back ground
        with root.canvas.before:
            Color(0.25, 0.25, 0.25, 1)  # green; colors range from 0-1 not 0-255
            self.rect = Rectangle(size=root.size, pos=root.pos)
        
        return root
    def testFunction(self):
        self.testString = "This is used to test whether variable can be retrieved."

    def initailComicData(self, window_w, window_h, imagePoolList, parameter, generator):
        self.window_w = window_w
        self.window_h = window_h
        # self.resultSeuqence = resultSequence
        self.imagePoolList = imagePoolList
        self.generator = generator
        self.parameter = parameter


    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


    def generateNewComicSequence(self):
 
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
        resultSequence = self.generator.executeTaskLayers(sequence)
        # resultSequence.printSequence()

        return resultSequence

def GUIterface(window_w, window_h, resultSequence, imagePoolList, parameter):
    print("SYSTEM: Lauch the application interface")

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

    app = MainApp()
    # app.testFunction()
    app.initailComicData(window_h, window_w, resultSequence, imagePoolList, parameter)
    app.run()


def New_GUIInterface(window_w, window_h, imagePoolList, parameter, generator):
    print("SYSTEM: Lauch the application interface")
    app = MainApp()
    # app.testFunction()
    app.initailComicData(window_w, window_h, imagePoolList, parameter, generator)
    # app.generateNewComicSequence()
    app.run()




if __name__ == "__main__":

    # initial the tool and interface
    # generator = Generator()
    # def __init__(self, window_h, window_w, panel_h, panel_w, defaultLength, isPage):    
    # parameter = Parameters(DEFAULLT_WINDOW_HEIGHT, DEFAULLT_WINDOW_WIDTH, EQUAL_PANEL_HEIGHT, EQUAL_PANEL_WIDTH, DEFAULT_LENGTH, IS_PAGE, PANEL_HORIZONTAL_MAX, PANEL_VERTIVAL_MAX, DEFAULT_LENGTH)
    parameter = Parameters2(DEFAULLT_WINDOW_HEIGHT, DEFAULLT_WINDOW_WIDTH, EQUAL_PANEL_HEIGHT, EQUAL_PANEL_WIDTH, DEFAULT_LENGTH, IS_PAGE, PANEL_HORIZONTAL_MAX, PANEL_VERTIVAL_MAX, DEFAULT_LENGTH)

# from Grammar import *
# from Actions import *
# from Transitions import *
# from Textbox import *
# from EyePath import *
# from Sentiment import *
# from Scene import *

    # initial the tool and interface
    generator = Generator()    
    # Add task layers
    grammarLayer = Grammar("Grammar", parameter)
    generator.addTaskLayer(grammarLayer)
    narrativeLayer = NarrativeArc("NarrativeArc", parameter)
    generator.addTaskLayer(narrativeLayer)
    actionLayer = Actions("Actions", parameter)
    generator.addTaskLayer(actionLayer)
    transitionsLayer = Transitions("Transitions", parameter)
    generator.addTaskLayer(transitionsLayer)            
    compositionLayer = Compositions("Compositions", parameter)
    generator.addTaskLayer(compositionLayer)            
    textboxLayer = Textbox("Textboxes", parameter)
    generator.addTaskLayer(textboxLayer)       

    storyLayer = StoryContent("StoryContent", parameter)
    generator.addTaskLayer(storyLayer)   

    # eyePathLayer = EyePath("EyePath", parameter)
    # generator.addTaskLayer(eyePathLayer)       
    # sentimentLayer = Sentiment("Sentiment", parameter)
    # generator.addTaskLayer(sentimentLayer)   
    # sceneLayer = Scene("Scene", parameter)
    # generator.addTaskLayer(sceneLayer)   


    imagePoolList = {}
    imagePoolList["Chara"] = parameter.imagePool["Chara"]
    imagePoolList["Symbol"] = parameter.imagePool["Symbol"]
    imagePoolList["Scene"] = parameter.imagePool["Scene"]
    imagePoolList["Text"] = parameter.imagePool["Text"]
    # print(imagePoolList)

    # GUIterface(DEFAULLT_WINDOW_HEIGHT, DEFAULLT_WINDOW_WIDTH, resultSequence, imagePoolList, parameter)
    New_GUIInterface(DEFAULLT_WINDOW_WIDTH, DEFAULLT_WINDOW_HEIGHT, imagePoolList, parameter, generator)
 
