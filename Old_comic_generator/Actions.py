from Layer import *
from Panel import *
from Character import *
import random
import math

class Actions(Layer):

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

    
    def adjustAction(self, sequence):
        print("System: adjust action sequence")
        # self.actionSentimentLevel = {}
        # self.SentimentLevelAction = {}
        total_length = len(sequence.panelQueue)
        panel_count = 1

        Assign_action_list = {}
        Assign_position_list = {}
        if sequence.isNarrative == False:
            panel_index = 0
            for panel in sequence.panelQueue:
            # print("--------------------------------------")
                for chara in panel.characterList:


                    if chara.characterName not in Assign_action_list:
                        print("System: keep current action, just update position")
                        print("1")
                        # print("old action: ", chara.action, "old position: ", chara.compositionPosition)
                        current_x = chara.compositionPosition[0][0]
                        current_y = chara.compositionPosition[0][1]
                        right_y = self.parameter.actionPool.ActionPool[chara.action].actionPositionLevel
                        chara.assignPosition(current_x, right_y)
                        Assign_position_list[chara.characterName] = [current_x, right_y]
                        # print("new action: ", chara.action, "new position: ", chara.compositionPosition)


                    else:
                        print("2")
                        # print("old action: ", chara.action, "old position: ", chara.compositionPosition)
                        chara.chanageAction(Assign_action_list[chara.characterName])
                        # Assign_position_list[chara.characterName] = [current_x, right_y]
                        chara.assignPosition(Assign_position_list[chara.characterName][0], Assign_position_list[chara.characterName][1]) 
                        adjust_x = self.parameter.actionPool.ActionPool[Assign_action_list[chara.characterName]].action_x_adjust
                        adjust_y = self.parameter.actionPool.ActionPool[Assign_action_list[chara.characterName]].action_y_adjust
                        chara.adjustPosition(adjust_x, adjust_y, panel.composition)
                        Assign_position_list[chara.characterName] = [chara.compositionPosition[0][0], chara.compositionPosition[0][1]]

                        # print("new action: ", chara.action, "new position: ", chara.compositionPosition)

                    
                    # print("Current Action: ", chara.action)
                    next_action = random.choice(list(self.parameter.actionNet[chara.action].keys()))

                    if chara.characterName not in sequence.scorePath:
                        sequence.scorePath[chara.characterName] = []
                        temp_action = chara.action
                        temp_action = self.parameter.checkList(temp_action)
                        base_score = self.parameter.actionSentimentLevel[temp_action][0]
                        # modify_score = self.parameter.actionSentimentLevel[][0]
                        sequence.scorePath[chara.characterName].append(base_score)
                        
                        sequence.actionPath[chara.characterName] = []
                        sequence.actionPath[chara.characterName].append(temp_action)
                    else:

                        temp_action = chara.action
                        temp_action = self.parameter.checkList(temp_action)
                        modify_score = self.parameter.actionSentimentLevel[temp_action][0] + sequence.scorePath[chara.characterName][panel_index -1]
                        sequence.scorePath[chara.characterName].append(modify_score)
                        sequence.actionPath[chara.characterName] = []
                        sequence.actionPath[chara.characterName].append(temp_action)   




                    if chara.characterName not in Assign_action_list:
                        # print("System: keep current action, just update position")
                        Assign_action_list[chara.characterName] = next_action
                    else:
                
                        Assign_action_list[chara.characterName] = next_action

                panel_index =  panel_index +1         
            print("********************************")
            print("Character Score Path: ", sequence.scorePath)
            print("Character Action Path: ", sequence.actionPath)
            print("********************************")

        else:
            print("$$$$$$  Achieve narrative score")

            narrative_score_sequence = []
            for panel in sequence.panelQueue:
                narrative_score_sequence.append(panel.narrativeScore)
            
            print("----------------------------------")
            print("Narrative Arc: ", narrative_score_sequence)


            panel_index = 0
            change_sequence = []
            for panel in sequence.panelQueue:
                if panel_index < len(sequence.panelQueue)-1:
                    # has next
                    current_score = narrative_score_sequence[panel_index]
                    next_score = narrative_score_sequence[panel_index+1]

                    if current_score > next_score:
                        change_sequence.append(-1)
                    elif current_score < next_score:
                        change_sequence.append(1)
                    else:
                        change_sequence.append(0)
                else:
                    # the last
                    change_sequence.append(0)



                panel_index = panel_index + 1

            print("Change trend: ", change_sequence)

            panel_index = 0
            default_distance = 0.1
            
            
            for panel in  sequence.panelQueue:
                for chara in panel.characterList:

                    possble_action_list = self.getPossibleActionList(chara.action)

                    if panel_index < len(sequence.panelQueue)-1:
                        # has next
                        current_score = narrative_score_sequence[panel_index]
                        next_score = narrative_score_sequence[panel_index+1]
                        target_score = abs(next_score - current_score)
                        direction = change_sequence[panel_index]

                        result_action_list = []
                        result_weifht_list = []
                        if len(possble_action_list[direction]) > 0:
                            # at least one action
                            total = 0
                            for poss_act in possble_action_list[direction]:
                                distance = abs(target_score - abs(possble_action_list[direction][poss_act]))
                                if distance == 0:
                                    distance = default_distance

                                    total = total + 1/distance

                                else:
                                    total = total + 1/distance

                                result_action_list.append(poss_act)
                                result_weifht_list.append(1/distance)

                            # distribution = {}

                            # for poss_act in possble_action_list[direction]:
                            #     distance = abs(target_score - abs(possble_action_list[direction][poss_act]))
                            #     if distance == 0:
                            #         distribution[poss_act] = 1/default_distance/total
                            #     else:
                            #         distribution[poss_act] = 1/distance/total

                        else:
                            # use [0] instead

                            total = 0
                            for poss_act in possble_action_list[0]:
                                distance = abs(target_score - abs(possble_action_list[0][poss_act]))
                                if distance == 0:
                                    distance = default_distance
                                    total = total + 1/distance
                                else:
                                    total = total + 1/distance
                                
                                result_action_list.append(poss_act)
                                result_weifht_list.append(1/distance)

                            # distribution = {}

                            # for poss_act in possble_action_list[direction]:
                            #     distance = abs(target_score - abs(possble_action_list[direction][poss_act]))
                            #     if distance == 0:
                            #         distribution[poss_act] = 1/default_distance/total
                            #     else:
                            #         distribution[poss_act] = 1/distance/total
                        
                        # next_action = random.choices(result_action_list, weights=result_weifht_list, k=1)
                        # print("NEXT: ", next_action)

                
                for chara in panel.characterList:


                    print(Assign_action_list)
                    print(Assign_position_list)
                    if chara.characterName not in Assign_action_list:
                        print("System: keep current action, just update position")
                        print("old action: ", chara.action, "old position: ", chara.compositionPosition)
                        current_x = chara.compositionPosition[0][0]
                        current_y = chara.compositionPosition[0][1]
                        right_y = self.parameter.actionPool.ActionPool[chara.action].actionPositionLevel
                        chara.assignPosition(current_x, right_y)
                        Assign_position_list[chara.characterName] = [current_x, right_y]
                        print("new action: ", chara.action, "new position: ", chara.compositionPosition)


                    else:
                        print("old action: ", chara.action, "old position: ", chara.compositionPosition)
                        # print(self.parameter.actionPool.ActionPool)
                        # print(Assign_action_list[chara.characterName])
                        # print(self.parameter.actionPool.ActionPool[Assign_action_list[chara.characterName][0]])
                        # print(self.parameter.actionPool.ActionPool[Assign_action_list[chara.characterName][0]].action_x_adjust)

                        chara.chanageAction(Assign_action_list[chara.characterName])
                        # Assign_position_list[chara.characterName] = [current_x, right_y]
                        chara.assignPosition(Assign_position_list[chara.characterName][0], Assign_position_list[chara.characterName][1]) 
                        temp_action = Assign_action_list[chara.characterName]
                        temp_action = self.parameter.checkList(temp_action)
                        adjust_x = self.parameter.actionPool.ActionPool[temp_action].action_x_adjust
                        adjust_y = self.parameter.actionPool.ActionPool[temp_action].action_y_adjust
                        chara.adjustPosition(adjust_x, adjust_y, panel.composition)
                        Assign_position_list[chara.characterName] = [chara.compositionPosition[0][0], chara.compositionPosition[0][1]]

                        print("new action: ", chara.action, "new position: ", chara.compositionPosition)

                    
                    # print("Current Action: ", chara.action)
                    # next_action = random.choice(list(self.parameter.actionNet[chara.action].keys()))
                    print(chara, " ^^^^^^^^^^^^^^\n ", result_action_list, "\n", result_weifht_list)

                    next_action = random.choices(result_action_list, weights=result_weifht_list, k=1)   

                    if chara.characterName not in sequence.scorePath:
                        sequence.scorePath[chara.characterName] = []
                        temp_action = chara.action
                        temp_action = self.parameter.checkList(temp_action)
                        base_score = self.parameter.actionSentimentLevel[temp_action][0]
                        # modify_score = self.parameter.actionSentimentLevel[][0]
                        sequence.scorePath[chara.characterName].append(base_score)
                        
                        sequence.actionPath[chara.characterName] = []
                        sequence.actionPath[chara.characterName].append(temp_action)
                    else:

                        temp_action = chara.action
                        temp_action = self.parameter.checkList(temp_action)
                        modify_score = self.parameter.actionSentimentLevel[temp_action][0] + sequence.scorePath[chara.characterName][panel_index -1]
                        sequence.scorePath[chara.characterName].append(modify_score)
                        sequence.actionPath[chara.characterName] = []
                        sequence.actionPath[chara.characterName].append(temp_action)                        

                    if chara.characterName not in Assign_action_list:
                        # print("System: keep current action, just update position")
                        Assign_action_list[chara.characterName] = next_action
                    else:
                        Assign_action_list[chara.characterName] = next_action

                panel_index = panel_index + 1
            
            print("********************************")
            print("Character Score Path: ", sequence.scorePath)
            print("Character Action Path: ", sequence.actionPath)
            print("********************************")

        return sequence

    
    def getPossibleActionList(self, current_action):
        actionLists = {}
        actionLists[0] = {}
        actionLists[1] = {}
        actionLists[-1] = {}

        next_possible_actions = self.parameter.actionNet[current_action].keys()

        for poss_action in next_possible_actions:
            score = self.parameter.actionSentimentLevel[poss_action][0]
            if score > 0:
                if poss_action not in actionLists[1]:
                    actionLists[1][poss_action] = score
                    actionLists[0][poss_action] = score

                # actionLists[1]
            elif score < 0:
                if poss_action not in actionLists[-1]:
                    actionLists[-1][poss_action] = score
                    actionLists[0][poss_action] = score


            else:
                if poss_action not in actionLists[1]:
                    actionLists[1][poss_action] = score
                if poss_action not in actionLists[-1]:
                    actionLists[-1][poss_action] = score
                if poss_action not in actionLists[0]:
                    actionLists[0][poss_action] = score


        return actionLists
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
        
        sequence = self.adjustAction(sequence)       
    
    def otherApply(self, sequence):
        # print("Error: the panel has alradey been generated without ", self.layerName, ".")
        sequence = self.adjustAction(sequence)