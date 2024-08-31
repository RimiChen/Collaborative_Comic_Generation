from Layer import *

class EyePath(Layer):

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
    
    def adjustPanelPosition(self, seuqence):
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

            new_panel = Panel([top_x, top_y],[center_x, center_y], "", "", characterList, 1)
            
            sequence.appendToSequence(new_panel)

            panel_index = panel_index + 1        
        
        sequence = self.adjustPanelPosition(sequence)
    
    def otherApply(self, sequence):
        # print("Error: the panel has alradey been generated without ", self.layerName, ".")
        sequence = self.adjustPanelPosition(sequence)