import math
from ActionPool import *
from CompositionPool import *
from Character import *
from ScenePool import *
from ImageObj import *
from ImagePool import *

class Parameters:
    def __init__(self, window_h, window_w, panel_h, panel_w, defaultLength, isPage, horizontal_max, vertical_max, default_panel_number):
        # self.taskQueue = queue.Queue()
        self.taskQueue = []
        self.window_h = window_h
        self.window_w = window_w
        self.panel_h = panel_h
        self.panel_w = panel_w
        self.defaultLength = defaultLength
        self.isPage = isPage
        self.horizontal_max = horizontal_max
        self.vertical_max = vertical_max

        self.default_panel_number = default_panel_number

        self.customizedDictionary= {}
        self.customizedInfo= {}



        self.storyContent = "A and B are in the forest.  A has B's Apple. B enter the scene. B is angry"
        
        #A and B are in the forest
        # A has B's Apple
        # B enter the scene
        # B is angry

        self.storyAssertions = self.getStoryAssertions(self.storyContent)

        

        self.action_remain_exception = [
            "collide",
            "jump",
            "fall",
            "spit"
        ]
        self.action_moving_list = [
            "fly",
            "run",
            "roll",
        ]

        # TODO 
        self.text_list = {}
        # talk
        self.text_list[1] = {}
        self.text_list[1]["name"] = "text_1"
        self.text_list[1]["action"] = [
            "stand",
            "sit",
            "laugh",
            "cry",
        ]

        # think
        self.text_list[2] = {}
        self.text_list[2]["name"] = "text_2"
        self.text_list[2]["action"] = [
            "eat",
            "drink",
            "dizzy",
            "sleep"
        ]

        # shock
        self.text_list[3] = {}
        self.text_list[3]["name"] = "text_3"
        self.text_list[3]["action"] = [
            "collide",
            "angry",
            "shock",
        ]
        
        # TODO 
        self.grammar_base_score = {}
        self.grammar_base_score["E"] = 0
        self.grammar_base_score["I"] = 3
        self.grammar_base_score["P"] = 8
        self.grammar_base_score["R"] = 4

        self.grammar_likelyhood = 2



        # set composition
        # self.compositionPool = CompositionPool().CompositionPool
        self.compositionPool = CompositionPool()
        self.composition_w = math.floor (self.panel_w / 3)
        self.composition_h = math.floor (self.panel_h / 3)

        self.setCompositionPool(self.composition_w, self.composition_h)
        # print(self.compositionPool.CompositionPool)

        self.imagePool = self.initialImagePools()

        # set action network
        self.actionDictionary = {}
        self.actionSentimentLevel = {}
        self.sentimentLevelAction = {}
        self.sentimentThreshold = 2
        self.setActionSentiment()

        self.actionNet = {}
        self.actionIndex = {}
        self.actionPool = ActionPool(self.actionSentimentLevel, self.imagePool["Symbol"])
        self.actionPool.initialActionPool()


        self.setActionPool()
        
        # action: index
        # print(self.actionPool)
        # index: action
        # print(self.actionDictionary)
        self.initActionRelations()

        self.scenePool = ScenePool()
        
        # relations
        # print(self.actionNet)

        # set default characters
        # self.characterList = [] 

        # tension level
        # 0 ~ 10

    def createNewInfo(self, infoName, info):
        self.customizedInfo[infoName] = {}
        self.customizedInfo[infoName]['info'] = info
        self.customizedInfo[infoName]['type'] = type(info)




    def addToDictinoary(self, targetDictionary, newKey, newValue):
        if newKey in self.customizedDictionary[targetDictionary]:
            self.customizedDictionary[targetDictionary][newKey] = newValue
        else:
            self.customizedDictionary[targetDictionary][newKey] = {}
            self.customizedDictionary[targetDictionary][newKey] = newValue 

    def getDictionary(self, dictionaryName):
        return self.customizedDictionary[dictionaryName]


    def createNewDictionary(self, dictionaryName):
        self.customizedDictionary[dictionaryName] = {}


    def getStoryAssertions(self, storyContent):
        
        #TODO: use rensa to get assertions

        # temp: 
        # A and B are in the forest
        # A has B's Apple
        # B enter the scene
        # B is angry

        assertions = {}
        assertions[0] = {}
        assertions[1] = {}
        assertions[2] = {}
        assertions[3] = {}
        
        for i in range(len(assertions)):
            assertions[i]['l'] = {} 
            assertions[i]['relation'] = {} 
            assertions[i]['r'] = {} 
            assertions[i]['action_object'] = {}
            assertions[i]['with_property'] = {} 
            assertions[i]['tense'] = {} 
        
        # A and B are in the forest
        assertions[0]['l'] = {} 
        assertions[0]['l']['0'] = "A"
        assertions[0]['l']['1'] = "B" 
        assertions[0]['relation'] = {}         
        assertions[0]['relation']['0'] = "location_on" 
        assertions[0]['r'] = {}         
        assertions[0]['r']['0'] = "forest" 
        assertions[0]['action_object'] = {}
        assertions[0]['with_property'] = {} 
        assertions[0]['tense'] = {} 
        
        # A has B's Apple
        assertions[1]['l'] = {} 
        assertions[1]['l']['0'] = "A"         
        assertions[1]['relation'] = {} 
        assertions[1]['relation']['0'] = "has" 
        assertions[1]['r'] = {}
        assertions[1]['r']['0'] = "r_owner"          
        assertions[1]['action_object'] = {}
        assertions[1]['with_property'] = {} 
        assertions[1]['tense'] = {} 

        # B enter the forest
        assertions[2]['l'] = {} 
        assertions[2]['l']['0'] = "B"         
        assertions[2]['relation'] = {} 
        assertions[2]['relation']['0'] = "action" 
        assertions[2]['r'] = {} 
        assertions[2]['r']['0'] = "enter"         
        assertions[2]['action_object'] = {}
        assertions[2]['action_object']['0'] = "forest"
        assertions[2]['with_property'] = {} 
        assertions[2]['tense'] = {} 

        # B is angry
        assertions[3]['l'] = {} 
        assertions[3]['l']['0'] = "B" 
        assertions[3]['relation'] = {}         
        assertions[3]['relation']['0'] = "action"
        assertions[3]['r'] = {} 
        assertions[3]['r']['0'] = "angry" 
        assertions[3]['action_object'] = {}
        assertions[3]['with_property'] = {} 
        assertions[3]['tense'] = {}                 


        return assertions

    def checkList(self, target):
        if isinstance(target, list) == True:
            return target[0]
        else:
            return target
    def decideCenter(self, index):
        # print("This is #", index, " center in ")

        row = math.floor(index / self.horizontal_max)
        column = index % self.horizontal_max
        print("row: ", row, " cloumn: ", column)

        top_y = math.floor(self.window_h / self.vertical_max) * row
        top_x = math.floor(self.window_w / self.horizontal_max) * column
        center_y = top_y + math.floor(self.window_h / self.vertical_max / 2)
        center_x = top_x + math.floor(self.window_w / self.horizontal_max / 2)

        # center_y = math.floor(self.window_h / self.vertical_max)
        return [top_x, top_y, center_x, center_y]
    
    def setCompositionPool(self, composition_w, composition_h):


        self.compositionPool.CompositionPool[0] = {}
        self.compositionPool.CompositionPool[1] = {}
        self.compositionPool.CompositionPool[2] = {}
        self.compositionPool.CompositionPool[3] = {}
        self.compositionPool.CompositionPool[4] = {}
        self.compositionPool.CompositionPool[5] = {}

        # (left, top, w, h)
        
        
        new_width = math.floor(self.panel_w/4)
        new_height = math.floor(self.panel_h/5*3)
        new_top = math.floor(self.panel_h/5)
        new_margin = math.floor(self.panel_h/4)
        new_left = math.floor(self.panel_h/10)

        composition_index = 0
        com_index_x = 0
        self.compositionPool.CompositionPool[composition_index][com_index_x] = {}
        self.compositionPool.CompositionPool[composition_index][com_index_x]["box"] = [ new_left + new_margin* com_index_x, new_top, new_width, new_height]
        self.compositionPool.CompositionPool[composition_index][com_index_x]["level"] = 3 

        com_index_x = 1
        self.compositionPool.CompositionPool[composition_index][com_index_x] = {}
        self.compositionPool.CompositionPool[composition_index][com_index_x]["box"] = [ new_left + new_margin* com_index_x, new_top, new_width, new_height]
        self.compositionPool.CompositionPool[composition_index][com_index_x]["level"] = 3 

        com_index_x = 2
        self.compositionPool.CompositionPool[composition_index][com_index_x] = {}
        self.compositionPool.CompositionPool[composition_index][com_index_x]["box"] = [ new_left + new_margin* com_index_x, new_top, new_width, new_height]
        self.compositionPool.CompositionPool[composition_index][com_index_x]["level"] = 3 



        new_width = math.floor(self.panel_w/9*2)
        new_height = math.floor(self.panel_h/5*3)
        new_top = math.floor(self.panel_h/5)
        new_left = math.floor(self.panel_h/9*2)
        new_margin = math.floor(self.panel_h/9*3)

        composition_index = 1
        com_index_x = 0
        # com_index_y = 0
        self.compositionPool.CompositionPool[composition_index][com_index_x] = {}
        self.compositionPool.CompositionPool[composition_index][com_index_x]["box"] = [ new_left + new_margin* com_index_x, new_top, new_width, new_height]
        self.compositionPool.CompositionPool[composition_index][com_index_x]["level"] = 3 
        # self.compositionPool.CompositionPool[0][0][0] = [composition_w * com_index_x, composition_h * com_index_y]
        com_index_x = 1
        # com_index_y = 0
        self.compositionPool.CompositionPool[composition_index][com_index_x] = {}
        self.compositionPool.CompositionPool[composition_index][com_index_x]["box"] = [ new_left + new_margin* com_index_x, new_top, new_width, new_height]
        self.compositionPool.CompositionPool[composition_index][com_index_x]["level"] = 3 



        new_width = math.floor(self.panel_w/3)
        new_height = math.floor(self.panel_h/5*3)
        new_top = math.floor(self.panel_h/7*2)
        new_left = math.floor(self.panel_h/9)
        new_margin = math.floor(self.panel_h/2)

        composition_index = 2
        com_index_x = 0
        # com_index_y = 0
        self.compositionPool.CompositionPool[composition_index][com_index_x] = {}
        self.compositionPool.CompositionPool[composition_index][com_index_x]["box"] = [ new_left + new_margin* com_index_x, new_top, new_width, new_height]
        self.compositionPool.CompositionPool[composition_index][com_index_x]["level"] = 3 
        # self.compositionPool.CompositionPool[0][0][0] = [composition_w * com_index_x, composition_h * com_index_y]
        
        new_width = math.floor(self.panel_w/5)
        new_height = math.floor(self.panel_h/2)
        new_top = math.floor(self.panel_h/7)
        new_left = math.floor(self.panel_h/9)
        new_margin = math.floor(self.panel_h/2)

        com_index_x = 1
        # com_index_y = 0
        self.compositionPool.CompositionPool[composition_index][com_index_x] = {}
        self.compositionPool.CompositionPool[composition_index][com_index_x]["box"] = [ new_left + new_margin* com_index_x, new_top, new_width, new_height]
        self.compositionPool.CompositionPool[composition_index][com_index_x]["level"] = 3 




        new_width = math.floor(self.panel_w/5)
        new_height = math.floor(self.panel_h/2)
        new_top = math.floor(self.panel_h/7)
        new_left = math.floor(self.panel_h/9)
        new_margin = math.floor(self.panel_h/2)


        composition_index = 3
        com_index_x = 0
        # com_index_y = 0
        self.compositionPool.CompositionPool[composition_index][com_index_x] = {}
        self.compositionPool.CompositionPool[composition_index][com_index_x]["box"] = [ new_left + new_margin* com_index_x, new_top, new_width, new_height]
        self.compositionPool.CompositionPool[composition_index][com_index_x]["level"] = 3 
        # self.compositionPool.CompositionPool[0][0][0] = [composition_w * com_index_x, composition_h * com_index_y]


        new_width = math.floor(self.panel_w/3)
        new_height = math.floor(self.panel_h/5*3)
        new_top = math.floor(self.panel_h/7*2)
        new_left = math.floor(self.panel_h/9)
        new_margin = math.floor(self.panel_h/3)

        com_index_x = 1
        # com_index_y = 0
        self.compositionPool.CompositionPool[composition_index][com_index_x] = {}
        self.compositionPool.CompositionPool[composition_index][com_index_x]["box"] = [ new_left + new_margin* com_index_x, new_top, new_width, new_height]
        self.compositionPool.CompositionPool[composition_index][com_index_x]["level"] = 3 





        new_width = math.floor(self.panel_w/5)
        new_height = math.floor(self.panel_h/2)
        new_top = math.floor(self.panel_h/7)
        new_left = math.floor(self.panel_h/9)
        new_margin = math.floor(self.panel_h/2)


        composition_index = 4
        com_index_x = 0
        # com_index_y = 0
        self.compositionPool.CompositionPool[composition_index][com_index_x] = {}
        self.compositionPool.CompositionPool[composition_index][com_index_x]["box"] = [ new_left + new_margin* com_index_x, new_top, new_width, new_height]
        self.compositionPool.CompositionPool[composition_index][com_index_x]["level"] = 3 
        # self.compositionPool.CompositionPool[0][0][0] = [composition_w * com_index_x, composition_h * com_index_y]


        new_width = math.floor(self.panel_w/2)
        new_height = math.floor(self.panel_h/2)
        new_top = math.floor(self.panel_h/7*3)
        new_left = math.floor(self.panel_h/9)
        new_margin = math.floor(self.panel_h/3)

        com_index_x = 1
        # com_index_y = 0
        self.compositionPool.CompositionPool[composition_index][com_index_x] = {}
        self.compositionPool.CompositionPool[composition_index][com_index_x]["box"] = [ new_left + new_margin* com_index_x, new_top, new_width, new_height]
        self.compositionPool.CompositionPool[composition_index][com_index_x]["level"] = 2




        new_width = math.floor(self.panel_w/2)
        new_height = math.floor(self.panel_h/2)
        new_top = math.floor(self.panel_h/7*3)
        new_left = math.floor(self.panel_h/9)
        new_margin = math.floor(self.panel_h/3)

        composition_index = 5
        com_index_x = 0
        # com_index_y = 0
        self.compositionPool.CompositionPool[composition_index][com_index_x] = {}
        self.compositionPool.CompositionPool[composition_index][com_index_x]["box"] = [ new_left + new_margin* com_index_x, new_top, new_width, new_height]
        self.compositionPool.CompositionPool[composition_index][com_index_x]["level"] = 2 
        # self.compositionPool.CompositionPool[0][0][0] = [composition_w * com_index_x, composition_h * com_index_y]


        new_width = math.floor(self.panel_w/5)
        new_height = math.floor(self.panel_h/2)
        new_top = math.floor(self.panel_h/7)
        new_left = math.floor(self.panel_h/9)
        new_margin = math.floor(self.panel_h/2)

        com_index_x = 1
        # com_index_y = 0
        self.compositionPool.CompositionPool[composition_index][com_index_x] = {}
        self.compositionPool.CompositionPool[composition_index][com_index_x]["box"] = [ new_left + new_margin* com_index_x, new_top, new_width, new_height]
        self.compositionPool.CompositionPool[composition_index][com_index_x]["level"] = 3



    def setCompositionPool_bk(self, composition_w, composition_h):


        self.compositionPool.CompositionPool[0] = {}
        self.compositionPool.CompositionPool[1] = {}
        self.compositionPool.CompositionPool[2] = {}
        self.compositionPool.CompositionPool[3] = {}

        
        com_index_x = 0
        com_index_y = 0
        self.compositionPool.CompositionPool[0] = {}
        self.compositionPool.CompositionPool[0][0] = {}
        self.compositionPool.CompositionPool[0][0][0] = [composition_w * com_index_x, composition_h * com_index_y]
        com_index_x = 1
        com_index_y = 0
        self.compositionPool.CompositionPool[0] = {}
        self.compositionPool.CompositionPool[0][1] = {}
        self.compositionPool.CompositionPool[0][1][0] = [composition_w * com_index_x, composition_h * com_index_y]
        com_index_x = 2
        com_index_y = 0
        self.compositionPool.CompositionPool[0] = {}
        self.compositionPool.CompositionPool[0][2] = {}
        self.compositionPool.CompositionPool[0][2][0] = [composition_w * com_index_x, composition_h * com_index_y]

        com_index_x = 0
        com_index_y = 1
        self.compositionPool.CompositionPool[0] = {}
        self.compositionPool.CompositionPool[0][0] = {}
        self.compositionPool.CompositionPool[0][0][1] = [composition_w * com_index_x, composition_h * com_index_y]
        com_index_x = 1
        com_index_y = 1
        self.compositionPool.CompositionPool[0] = {}
        self.compositionPool.CompositionPool[0][1] = {}
        self.compositionPool.CompositionPool[0][1][1] = [composition_w * com_index_x, composition_h * com_index_y]
        com_index_x = 2
        com_index_y = 1
        self.compositionPool.CompositionPool[0] = {}
        self.compositionPool.CompositionPool[0][2] = {}
        self.compositionPool.CompositionPool[0][2][1] = [composition_w * com_index_x, composition_h * com_index_y]

        com_index_x = 0
        com_index_y = 2
        self.compositionPool.CompositionPool[0] = {}
        self.compositionPool.CompositionPool[0][0] = {}
        self.compositionPool.CompositionPool[0][0][2] = [composition_w * com_index_x, composition_h * com_index_y]
        com_index_x = 1
        com_index_y = 2
        self.compositionPool.CompositionPool[0] = {}
        self.compositionPool.CompositionPool[0][1] = {}
        self.compositionPool.CompositionPool[0][1][2] = [composition_w * com_index_x, composition_h * com_index_y]
        com_index_x = 2
        com_index_y = 2
        self.compositionPool.CompositionPool[0] = {}
        self.compositionPool.CompositionPool[0][2] = {}
        self.compositionPool.CompositionPool[0][2][2] = [composition_w * com_index_x, composition_h * com_index_y]


    def setActionSentiment(self):
        # valence  emotion, arousal (how much) good + negtive -. emotion models: arousal, calence, dominance
        self.actionSentimentLevel["stand"] = [0,0]
        self.actionSentimentLevel["sit"] = [-1,0]
        self.actionSentimentLevel["eat"] = [3,2]
        self.actionSentimentLevel["drink"] = [2, 2]
        self.actionSentimentLevel["run"] = [6, 0]
        self.actionSentimentLevel["collide"] = [5, -2]
        self.actionSentimentLevel["dizzy"] = [-3, -3]
        self.actionSentimentLevel["shock"] = [4, -3.7]
        self.actionSentimentLevel["jump"] = [5, 0]
        self.actionSentimentLevel["laugh"] = [1.5, 4]
        self.actionSentimentLevel["cry"] = [-1, -5]
        self.actionSentimentLevel["angry"] = [5.5, -2]
        self.actionSentimentLevel["fall"] = [3.5, -3.5]
        self.actionSentimentLevel["fly"] = [1, 0]
        self.actionSentimentLevel["roll"] = [2.5, -1]
        self.actionSentimentLevel["sleep"] = [-3.7, 3]
        self.actionSentimentLevel["think"] = [0, 2]
        self.actionSentimentLevel["spit"] = [-1, -3]


        # for action in self.actionSentimentLevel:
        #     if self.actionSentimentLevel[action] in self.sentimentLevelAction:
        #         self.sentimentLevelAction[self.actionSentimentLevel[action]].append(action)
        #     else:
        #         self.sentimentLevelAction[self.actionSentimentLevel[action]] = []
        #         self.sentimentLevelAction[self.actionSentimentLevel[action]].append(action)
        
        

    def setActionPool(self):
        self.actionIndex["eat"] = "0"
        self.actionIndex["drink"] = "1"
        self.actionIndex["run"] = "2"
        self.actionIndex["collide"] = "3"
        self.actionIndex["sit"] = "4"
        self.actionIndex["dizzy"] = "5"
        self.actionIndex["shock"] = "6"
        self.actionIndex["stand"] = "7"
        self.actionIndex["jump"] = "8"
        self.actionIndex["laugh"] = "9"
        self.actionIndex["cry"] = "10"
        self.actionIndex["angry"] = "11"
        self.actionIndex["fall"] = "12"
        self.actionIndex["fly"] = "13"
        self.actionIndex["roll"] = "14"
        self.actionIndex["sleep"] = "15"
        self.actionIndex["think"] = "16"
        self.actionIndex["spit"] = "17"

        # create index to action dictionary
        # initial action network
        for action in self.actionIndex:
            # print(action)
            self.actionDictionary[self.actionIndex[action]] = action
            self.actionNet[action] = {}

    def initActionRelations(self):

        # base list
        # self.setActionLink("stand", "stand", True)
        # self.setActionLink("stand", "eat", True)
        # self.setActionLink("stand", "drink", True)
        # self.setActionLink("stand", "collide", True)
        # self.setActionLink("stand", "run", True)
        # self.setActionLink("stand", "sit", True)
        # self.setActionLink("stand", "dizzy", True)
        # self.setActionLink("stand", "jump", True)
        # self.setActionLink("stand", "laugh", True)
        # self.setActionLink("stand", "cry", True)
        # self.setActionLink("stand", "angry", True)
        # self.setActionLink("stand", "fall", True)
        # self.setActionLink("stand", "fly", True)
        # self.setActionLink("stand", "roll", True)
        # self.setActionLink("stand", "sleep", True)
        # self.setActionLink("stand", "think", True)
        # self.setActionLink("stand", "spit", True)
        # self.setActionLink("stand", "shock", True)

        self.setActionLink("stand", "stand", True)
        self.setActionLink("stand", "run", True)
        self.setActionLink("stand", "sit", True)
        self.setActionLink("stand", "dizzy", True)
        self.setActionLink("stand", "jump", True)
        self.setActionLink("stand", "laugh", True)
        self.setActionLink("stand", "cry", True)
        self.setActionLink("stand", "angry", True)
        self.setActionLink("stand", "fly", True)
        self.setActionLink("stand", "think", True)
        self.setActionLink("stand", "shock", True)

        self.setActionLink("eat", "stand", True)
        self.setActionLink("eat", "eat", True)
        self.setActionLink("eat", "drink", True)
        self.setActionLink("eat", "sit", True)
        self.setActionLink("eat", "dizzy", True)
        self.setActionLink("eat", "laugh", True)
        self.setActionLink("eat", "cry", True)
        self.setActionLink("eat", "angry", True)
        self.setActionLink("eat", "spit", True)
        self.setActionLink("eat", "shock", True)

        self.setActionLink("drink", "stand", True)
        self.setActionLink("drink", "eat", True)
        self.setActionLink("drink", "drink", True)
        self.setActionLink("drink", "sit", True)
        self.setActionLink("drink", "dizzy", True)
        self.setActionLink("drink", "laugh", True)
        self.setActionLink("drink", "cry", True)
        self.setActionLink("drink", "angry", True)
        self.setActionLink("drink", "sleep", True)
        self.setActionLink("drink", "spit", True)
        self.setActionLink("drink", "shock", True)

        self.setActionLink("run", "stand", True)
        self.setActionLink("run", "collide", True)
        self.setActionLink("run", "run", True)
        self.setActionLink("run", "dizzy", True)
        self.setActionLink("run", "jump", True)
        self.setActionLink("run", "fall", True)
        self.setActionLink("run", "fly", True)
        self.setActionLink("run", "roll", True)
        self.setActionLink("run", "shock", True)

        self.setActionLink("sit", "stand", True)
        self.setActionLink("sit", "eat", True)
        self.setActionLink("sit", "drink", True)
        self.setActionLink("sit", "sit", True)
        self.setActionLink("sit", "dizzy", True)
        self.setActionLink("sit", "laugh", True)
        self.setActionLink("sit", "cry", True)
        self.setActionLink("sit", "angry", True)
        self.setActionLink("sit", "sleep", True)
        self.setActionLink("sit", "think", True)
        self.setActionLink("sit", "shock", True)

        self.setActionLink("collide", "dizzy", True)
        self.setActionLink("collide", "cry", True)
        self.setActionLink("collide", "angry", True)
        self.setActionLink("collide", "shock", True)

        self.setActionLink("dizzy", "sit", True)
        self.setActionLink("dizzy", "dizzy", True)
        self.setActionLink("dizzy", "cry", True)
        self.setActionLink("dizzy", "angry", True)
        self.setActionLink("dizzy", "shock", True)

        self.setActionLink("jump", "stand", True)
        self.setActionLink("jump", "run", True)
        self.setActionLink("jump", "fall", True)
        self.setActionLink("jump", "fly", True)

        self.setActionLink("laugh", "stand", True)
        self.setActionLink("laugh", "sit", True)
        self.setActionLink("laugh", "laugh", True)
        self.setActionLink("laugh", "cry", True)
        self.setActionLink("laugh", "angry", True)
        self.setActionLink("laugh", "think", True)

        self.setActionLink("cry", "stand", True)
        self.setActionLink("cry", "sit", True)
        self.setActionLink("cry", "dizzy", True)
        self.setActionLink("cry", "laugh", True)
        self.setActionLink("cry", "cry", True)
        self.setActionLink("cry", "angry", True)
        self.setActionLink("cry", "sleep", True)
        self.setActionLink("cry", "think", True)
        self.setActionLink("cry", "shock", True)

        self.setActionLink("angry", "stand", True)
        self.setActionLink("angry", "eat", True)
        self.setActionLink("angry", "drink", True)
        self.setActionLink("angry", "run", True)
        self.setActionLink("angry", "sit", True)
        self.setActionLink("angry", "dizzy", True)
        self.setActionLink("angry", "cry", True)
        self.setActionLink("angry", "angry", True)
        self.setActionLink("angry", "shock", True)

        self.setActionLink("fall", "dizzy", True)
        self.setActionLink("fall", "cry", True)
        self.setActionLink("fall", "angry", True)
        self.setActionLink("fall", "shock", True)

        self.setActionLink("fly", "fall", True)
        self.setActionLink("fly", "fly", True)

        self.setActionLink("roll", "collide", True)
        self.setActionLink("roll", "sit", True)
        self.setActionLink("roll", "dizzy", True)
        self.setActionLink("roll", "laugh", True)
        self.setActionLink("roll", "cry", True)
        self.setActionLink("roll", "angry", True)
        self.setActionLink("roll", "roll", True)

        self.setActionLink("sleep", "sit", True)
        self.setActionLink("sleep", "dizzy", True)

        self.setActionLink("think", "stand", True)
        self.setActionLink("think", "sit", True)
        self.setActionLink("think", "laugh", True)
        self.setActionLink("think", "cry", True)
        self.setActionLink("think", "angry", True)
        self.setActionLink("think", "shock", True)

        self.setActionLink("spit", "stand", True)
        self.setActionLink("spit", "sit", True)
        self.setActionLink("spit", "cry", True)
        self.setActionLink("spit", "angry", True)
        self.setActionLink("spit", "shock", True)

        self.setActionLink("shock", "stand", True)
        self.setActionLink("shock", "collide", True)
        self.setActionLink("shock", "run", True)
        self.setActionLink("shock", "sit", True)
        self.setActionLink("shock", "think", True)




    def setActionLink(self, action_1, action_2, relation: bool):
        if action_1 in self.actionNet and action_2 in self.actionNet:
            self.actionNet[action_1][action_2] = relation
        else:
            print("Error: requested action does not exist!")


    def initialImagePools(self):
        image_default_height = self.composition_w
        image_default_width = self.composition_h
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



        imgTextPool = ImagePool()

        newImageAlias = "text_1"
        newImageFile = "text_1.png"
        newImage = ImageObj([image_default_top_x, image_default_top_y], [image_default_width, image_default_height], default_symbol_depth, symbolImageRootPath, newImageAlias, newImageFile)
        imgTextPool.addImageToPool(newImageAlias, newImage)    

        newImageAlias = "text_2"
        newImageFile = "text_2.png"
        newImage = ImageObj([image_default_top_x, image_default_top_y], [image_default_width, image_default_height], default_symbol_depth, symbolImageRootPath, newImageAlias, newImageFile)
        imgTextPool.addImageToPool(newImageAlias, newImage)    


        newImageAlias = "text_3"
        newImageFile = "text_3.png"
        newImage = ImageObj([image_default_top_x, image_default_top_y], [image_default_width, image_default_height], default_symbol_depth, symbolImageRootPath, newImageAlias, newImageFile)
        imgTextPool.addImageToPool(newImageAlias, newImage)    


        # scene image
        scene_default_x = 0
        scene_default_y = 0
        scene_default_height = self.panel_h
        scene_default_width = self.panel_w
        
        imgScenePool = ImagePool()

        newImageAlias = "forest"
        # newImageFile = "003-Forest01.jpg"
        newImageFile = "forest.jpg"

        newImage = ImageObj([scene_default_x, scene_default_y], [scene_default_width, scene_default_height], default_scene_depth , sceneImageRootPath, newImageAlias, newImageFile)
        imgScenePool.addImageToPool(newImageAlias, newImage)        


        newImageAlias = "garden"
        # newImageFile = "025-Castle01.jpg"
        newImageFile = "garden.jpg"

        newImage = ImageObj([scene_default_x, scene_default_y], [scene_default_width, scene_default_height], default_scene_depth , sceneImageRootPath, newImageAlias, newImageFile)
        imgScenePool.addImageToPool(newImageAlias, newImage)        


        newImageAlias = "beach"
        # newImageFile = "005-Beach01.jpg"
        newImageFile = "beach.jpg"
        newImage = ImageObj([scene_default_x, scene_default_y], [scene_default_width, scene_default_height], default_scene_depth , sceneImageRootPath, newImageAlias, newImageFile)
        imgScenePool.addImageToPool(newImageAlias, newImage)        


        newImageAlias = "town"
        # newImageFile = "018-MineTown02.jpg"
        newImageFile = "town.jpg"

        newImage = ImageObj([scene_default_x, scene_default_y], [scene_default_width, scene_default_height], default_scene_depth , sceneImageRootPath, newImageAlias, newImageFile)
        imgScenePool.addImageToPool(newImageAlias, newImage)        


        newImageAlias = "room"
        # newImageFile = "026-Castle02.jpg"
        newImageFile = "castle.jpg"

        newImage = ImageObj([scene_default_x, scene_default_y], [scene_default_width, scene_default_height], default_scene_depth , sceneImageRootPath, newImageAlias, newImageFile)
        imgScenePool.addImageToPool(newImageAlias, newImage)        


        imageReturnPool = {}
        imageReturnPool["Chara"] = imgCharaPool
        imageReturnPool["Symbol"] = imgSymbolPool
        imageReturnPool["Scene"] = imgScenePool 
        imageReturnPool["Text"] = imgTextPool 
        # return [imgCharaPool, imgSymbolPool, imgScenePool]
        return imageReturnPool
