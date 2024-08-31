from Layer import *
from Panel import *
from Character import *
import random

class NarrativeArc(Layer):

    def apply(self, sequence):

        # turn on narrative
        sequence.isNarrative = True

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

    
    def adjustNarrative(self, sequence):
        print("System: adjust action sequence")
        # self.actionSentimentLevel = {}
        # self.SentimentLevelAction = {}
        # total_length = len(sequence.panelQueue)
        # panel_count = 1

        # Assign_action_list = {}
        # Assign_position_list = {}
        narrative_score = []
        for panel in sequence.panelQueue:
        #     # print("--------------------------------------")
            new_score = self.getScore(panel.grammar)
            panel.narrativeScore = new_score
            narrative_score.append(panel.narrativeScore)

        # print("----------------------------------")
        # print("Narrative Arc: ", narrative_score)
        return sequence

    
    def getScore(self, grammar):
        score =  self.parameter.grammar_base_score[grammar]+randint(-self.parameter.grammar_likelyhood, self.parameter.grammar_likelyhood)

        if score < 0:
            score = 0
        elif score > 10:
            score = 10
        return score

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
        
        sequence = self.adjustNarrative(sequence)       
    
    def otherApply(self, sequence):
        # print("Error: the panel has alradey been generated without ", self.layerName, ".")
        sequence = self.adjustNarrative(sequence)