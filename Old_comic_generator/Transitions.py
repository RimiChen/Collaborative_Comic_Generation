from Layer import *
from Panel import *
from Character import *
import random

class Transitions(Layer):

    transitionSequence = []

    def generateTransition(self):
        
        
        transitions = [
            "action",
            # "subject",
            "scene",
            "aspect",
            "moment"
        ]

        resultTransition = random.choice(transitions)
        return resultTransition

    def apply(self, sequence):

        if self.isFrist(sequence) == True:
            self.firstApply(sequence)
        else:
            self.otherApply(sequence)

        return sequence

    def isFrist(self, sequence):
        if sequence.getSequenceLength() == 0:
            return True
        else:
            return False
    
    def adjustTransition(self, seuqence):

        assignScene = ""
        assign_composition = -1
        assign_action = {}
        for panel in seuqence.panelQueue:
            if assignScene != "":
                panel.scene = assignScene

            if assign_composition >= 0:
                panel.composition = assign_composition

            if len(assign_action) > 0:
                for chara in panel.characterList:
                    if chara.characterName in assign_action:
                        next_action = assign_action[chara.characterName]
                        chara.action = next_action
                # assign_action = {}
                    # if chara.aciton not in self.parameter.action_remain_exception:
                    #     # remain action
                    #     assign_aciton[chara.characterName] = chara.action

                    # else:
                    #     print("still change action")


            if panel.transition == "action":
                # no transition, add random transition
                new_transition = self.generateTransition()
                panel.transition = new_transition

            else:
                print(panel.transition)


            if panel.transition == "action":
                print("Do nothing for action transition")

                # change action otherwise
            else:
                print("Remain action")
                temp_action = {}
                for chara in panel.characterList:
                    if chara.action not in self.parameter.action_remain_exception:
                        # remain action
                        assign_action[chara.characterName] = chara.action

                    else:
                        print("still change action")

                        if chara.characterName in assign_action:
                            next_action =  self.adjustAction(assign_action[chara.characterName])
                            temp_action[chara.characterName] = next_action
                        
                assign_action = {}

                for temp in temp_action:
                    assign_action[temp] = temp_action[temp]

                if panel.transition == "scene":


                    print("change scene for scene transition")
                    print("old scene: ", panel.scene)
                    scene_dictinary = {}
                    scene_dictinary[panel.scene] = True
                    
                    new_scene = self.parameter.scenePool.getRandomScene(1)
                    while new_scene in scene_dictinary:
                        new_scene = self.parameter.scenePool.getRandomScene(1)
                    
                    scene_dictinary[new_scene] = True
                    # panel.scene = new_scene
                    assignScene = new_scene
                    
                    print("new scene: ", panel.scene)

                # elif panel.transition == "subject":
                #     print("change focus subject")
                elif panel.transition == "moment":
                    print("remain action for moment transition")

                    temp_action = {}
                    for chara in panel.characterList:
                        if chara.action not in self.parameter.action_remain_exception:
                            # remain action
                            assign_action[chara.characterName] = chara.action

                    #     else:
                    #         print("still change action")

                    #         if chara.characterName in assign_action:
                    #             next_action =  self.adjustAction(assign_action[chara.characterName])
                    #             temp_action[chara.characterName] = next_action
                            
                    # assign_action = {}

                    # for temp in temp_action:
                    #     assign_action[temp] = temp_action[temp]


                elif panel.transition == "aspect":
                    print("change composition aspect transition")

                    print("old composition: ", panel.composition)
                    composition_dictinary = {}
                    composition_dictinary[panel.composition] = True
                    
                    new_composition = self.parameter.compositionPool.generateRandCompositions()
                    while new_composition in composition_dictinary:
                        new_composition = self.parameter.compositionPool.generateRandCompositions()
                    
                    composition_dictinary[new_composition] = True
                    # panel.scene = new_scene
                    
                    assign_composition = new_composition
                    
                    print("new scene: ", panel.composition)                


        
        return seuqence

    def adjustAction(self, now_action):

        next_action = random.choice(list(self.parameter.actionNet[now_action].keys()))


        return next_action

    def firstApply(self, sequence):
        print("SYSTEM: ", self.layerName, " is the first generting layer.")

        # self.transitionSequence = self.generateTransition()

        # panel_index = 0
        # for panel in range(self.parameter.default_panel_number):
        #     [top_x, top_y, center_x, center_y] = self.parameter.decideCenter(panel_index)

        #     characterList =[]
        #     for chara in sequence.selectedCharacterList:
        #         new_chara =  Character(chara,self.parameter)
                
        #         characterList.append(new_chara)

        #     new_transition = self.generateTransition()
        #     scene = sequence.defaultScene
        #     composition = self.parameter.compositionPool.generateRandCompositions()
        #     new_panel = Panel([top_x, top_y],[center_x, center_y], "", scene, new_transition, characterList, composition, 1)
            
        #     sequence.appendToSequence(new_panel)

        #     panel_index = panel_index + 1        


        panel_index = 0
        new_range = randint(self.parameter.default_panel_number-1, self.parameter.default_panel_number+1)
        for panel in range(new_range):
            # def __init__(self, center, grammar, transition):
            [top_x, top_y, center_x, center_y] = self.parameter.decideCenter(panel_index)
            

            characterList =[]
            for chara in sequence.selectedCharacterList:
                new_chara =  Character(chara,self.parameter)
                characterList.append(new_chara)

            scene = sequence.defaultScene
            # composition = self.parameter.compositionPool.generateRandCompositions()
            composition = self.parameter.compositionPool.generateDefaultCompositions()
            # def __init__(self, top,  center, grammar, scene, transition, characterList, composition, modifyCount):
            # default action transition
            temp_grammar = [
                "E",
                "I",
                "P",
                "R"
            ]
            temp =  random.choice(temp_grammar)

            new_transition = self.generateTransition()
            new_panel = Panel([top_x, top_y],[center_x, center_y], temp, scene, new_transition, characterList, composition, 1)
            
            sequence.appendToSequence(new_panel)

            panel_index = panel_index + 1    


        sequence = self.adjustTransition(sequence)
    
    def otherApply(self, sequence):
        # print("Error: the panel has alradey been generated without ", self.layerName, ".")
        sequence = self.adjustTransition(sequence)