from Parameters import *
from Layer import *

class PanelRelationLayer(Layer):

    def testMethod(self):
        print('Create: ', self.layerName)

    def apply(self, sequence):
        print("Add ", self.layerName, " to Generator")
