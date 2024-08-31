from Layer import *
from Panel import *
from Character import *
import random
import json

class StoryContent(Layer):







    def sortAssertions(self,  assertions):
        print("System: sort assetions according to assigned order")
        return assertions

    def linkWordsWithActions(self):
        print("System: link the words from story with actions")
        
    def apply(self, sequence):
        # print("apply ", self.layerName)
        # sequence.appendToSequence(self.layerName)
        # print("w = ", self.parameter.window_w, "h", self.parameter.window_h)
        
        # replace this by grammar tree0

        # def __init__(self, center, grammar, transition):

        # infoName, info, type
        self.parameter.createNewInfo("story_content", self.parameter.storyContent)




        if self.isFrist(sequence) == True:
            self.firstApply(sequence)
        else:
            self.otherApply(sequence)
            assertions =  self.parameter.getStoryAssertions(self.parameter.customizedInfo["story_content"])
            sortedAssertions = self.sortAssertions(assertions)
            self.parameter.createNewDictionary("assertions")

            print(json.dumps(sortedAssertions, indent = 4))
            self.parameter.createNewInfo("story_assertions", sortedAssertions)

            # refrence this link to 
            self.parameter.createNewDictionary("action_links")
            self.parameter.addToDictinoary("action_links", "has", ["eat", "drink", ""])
            self.parameter.addToDictinoary("action_links", "enter", ["add"])
            self.parameter.addToDictinoary("action_links", "angry", ["angry"])
            self.parameter.addToDictinoary("action_links", "A", ["Char_1"])
            self.parameter.addToDictinoary("action_links", "B", ["Char_2"])
            self.parameter.addToDictinoary("action_links", "forest", ["forest"])            


            panel_count = 0
            panel_max = 4
            for panel in  sequence.panelQueue:
                
                if panel_count < panel_max:
                    print("================================================")
                    # print(sortedAssertions[panel_count])
                    self.printContent(sortedAssertions[panel_count])

                panel_count = panel_count + 1

            # print()


        return sequence

    def isFrist(self, sequence):
        if sequence.getSequenceLength() == 0:
            return True
        else:
            return False
    def firstApply(self, sequence):
        print("SYSTEM: ", self.layerName, " is the story content layer.")

    def otherApply(self, sequence):
         print("Error: the panel has alradey been generated without ", self.layerName, ".")
    def printContent(self, assertion):
        # input an assertion and print out content in the panel
        targetDictionary = self.parameter.getDictionary("action_links")
        print("88888888888888888888888888888888")
        print(assertion)
        print("88888888888888888888888888888888")

        print(json.dumps(targetDictionary, indent = 4))