from abc import ABC, abstractmethod
from Parameters import *

# A Sample class with init method
class Layer(ABC):
   
    # init method or constructor 
    def __init__(self, layerName):
        # [x, y]
        self.layerName = layerName
        self.parameter = ""

        # register the layer
        # self.parameter.appendLayer(layerName, self)
   
    # Sample Method 
    def addParameter(self, parameter:Parameters):
        self.parameter = parameter

    def testMethod(self):
        print('Layer: ', self.layerName)

    def apply(self, seuqence):
        
        pass
        return seuqence
