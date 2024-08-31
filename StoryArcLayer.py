from Parameters import *
from Layer import *

class StoryArcLayer(Layer):

    def testMethod(self):
        print('Create: ', self.layerName)

    def apply(self, sequence):
        print("Add ", self.layerName, " to Generator")