from Layer import *
from Panel import *
import random

class Sentiment(Layer):

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
    
    def adjustSentiment(self, seuqence):

        # adjust action according to sentiment
        character_last_action = {}
        for panel in seuqence.panelQueue:
            # check if the action match the sentiment level
        # self.actionSentimentLevel = {}
        # self.sentimentLevelAction = {}
            sentimentLevel = int(panel.sentimentLevel)
            
            sentiment_min = sentimentLevel -  self.parameter.sentimentThreshold           
            if sentiment_min < 0:
                sentiment_min = 0
            sentiment_max = sentimentLevel +  self.parameter.sentimentThreshold
            if sentiment_max > 10:
                sentiment_max = 10
            for chara in panel.characterList:
                if int(self.parameter.actionSentimentLevel[chara.action]) >=sentiment_min and int(self.parameter.actionSentimentLevel[chara.action]) <=sentiment_max:
                    print("don't need to change action")
                else:

                    possible_action_list = []
                    for level in range(sentiment_min, sentiment_max):
                        if str(level) in self.parameter.sentimentLevelAction:
                            for action in self.parameter.sentimentLevelAction[str(level)]:
                                possible_action_list.append(action)                    

                    if chara.characterName not in character_last_action:
                        # no last action, change directly
                        if len(possible_action_list) == 0:
                            # no possible action
                            print("no possible action in this tange, keep old action")
                            character_last_action[chara.characterName] = chara.action
                        else:
                            new_action = random.choice(possible_action_list)
                            chara.action = new_action
                            character_last_action[chara.characterName] = new_action
                    # else:
                    #     last_action = character_last_action[chara.characterName]

                    #     linked_action = 


    # def getRandomAction(self, randomNumber):
    #     resultList = []
    #     while len(resultList) < randomNumber:
    #         selection = random.choice(list(self.ActionPool.keys()))
    #         if selection not in resultList:
    #             resultList.append(selection)
        
    #     # print(resultList)
    #     return resultList 


                        character_last_action

        
        return seuqence


    def firstApply(self, sequence):
        print("SYSTEM: ", self.layerName, " is the first generting layer.")

        panel_index = 0
        for panel in range(self.parameter.default_panel_number):
            [top_x, top_y, center_x, center_y] = self.parameter.decideCenter(panel_index)

            characterList =[]
            for chara in sequence.selectedCharacterList:
                new_chara =  Character(chara,self.parameter)
                
                characterList.append(new_chara)

            scene = sequence.defaultScene
            composition = self.parameter.compositionPool.generateRandCompositions()
            new_panel = Panel([top_x, top_y],[center_x, center_y], "", scene, "", characterList,composition, 1)
            
            sequence.appendToSequence(new_panel)

            panel_index = panel_index + 1        
        
        sequence = self.adjustSentiment(sequence)
    
    def otherApply(self, sequence):
        # print("Error: the panel has alradey been generated without ", self.layerName, ".")
        sequence = self.adjustSentiment(sequence)