from Layer import *
from Panel import *
from Character import *
import random

class Grammar(Layer):

    grammarTree = []

    def generateGrammarTree(self):
        
        root_grammar = self.getRandomGrammar()

        new_grammar = []

        current_grammar = root_grammar
        while len(new_grammar) < 3 or len(new_grammar) > 8:
            new_grammar = []

            for grammar in current_grammar:
                if grammar == "I" or grammar == "P":
                    # poss = randint(0,2)
                    poss = randint(1,2)
                    if poss == 0:
                        # 1/3
                        # replace with new sequence
                        temp_new_grammar = self.getRandomGrammar()
                        for temp in temp_new_grammar:
                            new_grammar.append(temp)
                    else:
                        new_grammar.append(grammar)
                else:
                    new_grammar.append(grammar)

            print(new_grammar)
            current_grammar = new_grammar


        resultGrammar = current_grammar
        return resultGrammar

    def getRandomGrammar(self):
        grammarSequence = [
            # ["E","P"],
            # ["E","I","P"],
            ["E","I","P","R"],
            # ["E","P","R"],
            # ["I","P"],
            # ["I","P","R"],
            # ["P","R"],
        # ["E","I","I", "P","R"]
        ]  
        resultGrammar = random.choice(grammarSequence)
        return resultGrammar

    def apply(self, sequence):
        # print("apply ", self.layerName)
        # sequence.appendToSequence(self.layerName)
        # print("w = ", self.parameter.window_w, "h", self.parameter.window_h)
        
        # replace this by grammar tree0

        # def __init__(self, center, grammar, transition):

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
    def firstApply(self, sequence):
        print("SYSTEM: ", self.layerName, " is the first generting layer.")
        self.grammarTree = self.generateGrammarTree()

        panel_index = 0
        for grammar in self.grammarTree:
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
            new_panel = Panel([top_x, top_y],[center_x, center_y], grammar, scene, "action", characterList, composition, 1)
            
            sequence.appendToSequence(new_panel)

            panel_index = panel_index + 1        

    def otherApply(self, sequence):
         print("Error: the panel has alradey been generated without ", self.layerName, ".")