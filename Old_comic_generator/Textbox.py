
from Layer import *
from Panel import *
from Character import *
import random

class Textbox(Layer):

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

    
    def adjustTextbox(self, sequence):
        print("System: adjust action sequence")
        # self.actionSentimentLevel = {}
        # self.SentimentLevelAction = {}
        # total_length = len(sequence.panelQueue)
        # panel_count = 1

        # Assign_action_list = {}
        # Assign_position_list = {}
        for panel in sequence.panelQueue:
        #     # print("--------------------------------------")

            for chara in panel.characterList:
                if chara.textbox == 0:
                    new_text = 0
                    poss = randint(0,0)
                    if poss == 0:
                        for textbox_type in self.parameter.text_list:

                            if chara.action in self.parameter.text_list[textbox_type]["action"]:

                                new_text = textbox_type
                    chara.textbox = new_text

        #         if chara.characterName not in Assign_action_list:
        #             print("System: keep current action, just update position")
        #             # print("old action: ", chara.action, "old position: ", chara.compositionPosition)
        #             current_x = chara.compositionPosition[0][0]
        #             current_y = chara.compositionPosition[0][1]
        #             right_y = self.parameter.actionPool.ActionPool[chara.action].actionPositionLevel
        #             chara.assignPosition(current_x, right_y)
        #             Assign_position_list[chara.characterName] = [current_x, right_y]
        #             # print("new action: ", chara.action, "new position: ", chara.compositionPosition)


        #         else:
        #             # print("old action: ", chara.action, "old position: ", chara.compositionPosition)
        #             chara.chanageAction(Assign_action_list[chara.characterName])
        #             # Assign_position_list[chara.characterName] = [current_x, right_y]
        #             chara.assignPosition(Assign_position_list[chara.characterName][0], Assign_position_list[chara.characterName][1]) 
        #             adjust_x = self.parameter.actionPool.ActionPool[Assign_action_list[chara.characterName]].action_x_adjust
        #             adjust_y = self.parameter.actionPool.ActionPool[Assign_action_list[chara.characterName]].action_y_adjust
        #             chara.adjustPosition(adjust_x, adjust_y, panel.composition)
        #             Assign_position_list[chara.characterName] = [chara.compositionPosition[0][0], chara.compositionPosition[0][1]]

        #             # print("new action: ", chara.action, "new position: ", chara.compositionPosition)

                
        #         # print("Current Action: ", chara.action)
        #         next_action = random.choice(list(self.parameter.actionNet[chara.action].keys()))

        #         if chara.characterName not in Assign_action_list:
        #             # print("System: keep current action, just update position")
        #             Assign_action_list[chara.characterName] = next_action
        #         else:
        #             Assign_action_list[chara.characterName] = next_action


        return sequence

    
    
    def firstApply(self, sequence):
        print("SYSTEM: ", self.layerName, " is the first generting layer.")

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

            new_panel = Panel([top_x, top_y],[center_x, center_y], temp, scene, "action", characterList, composition, 1)
            
            sequence.appendToSequence(new_panel)

            panel_index = panel_index + 1     
        
        sequence = self.adjustTextbox(sequence)       
    
    def otherApply(self, sequence):
        # print("Error: the panel has alradey been generated without ", self.layerName, ".")
        sequence = self.adjustTextbox(sequence)