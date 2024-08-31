from abc import ABC, abstractmethod
from Parameters import *

# A Sample class with init method
class Layer(ABC):
   
    # init method or constructor 
    def __init__(self, layerName, parameter:Parameters):
        # [x, y]
        self.layerName = layerName
        self.parameter = parameter
   
    # Sample Method 
    def testMethod(self):
        print('Layer: ', self.layerName)

    def apply(self, seuqence):
        
        pass
        return seuqence
