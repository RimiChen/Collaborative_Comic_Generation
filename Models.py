from Parameters import *


class Models:
    def __init__(self, parameter: Parameters):
        print("Initialize the model contaniner, for multiple AI models")
        self.parameter = parameter
        self.model_queue = {}

    ### add all registered model into list
    def addAllModels(self):
        for model in self.parameter.model_register:
            self.model_queue[model] = self.parameter.model_register[model]
    ### execute the task queue
    def executeModelTests(self):
        for model in self.model_queue:
            # apply layer modifications to comic sequence
            model.testMethod()


