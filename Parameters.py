import random



class Parameters:
    def __init__(self, window_w, window_h, menu_w, default_sequence_length):
        ### basic parameters for user interface
        self.max_id = 65535*2
        
        self.taskQueue = []

        self.window_w = window_w
        self.window_h = window_h        

        self.panel_w = window_w - 3 * menu_w
        self.panel_h = window_h / 4

        self.menu_w = menu_w

        self.default_sequence_length = default_sequence_length
        
        ### register ID
        self.registeredID = []

        ### register attribute nodes
        self.attribute_type_register = []
        
        ### register layer modules
        # TODO: restrict the element of layer list to Layer class
        self.layer_register = {}
        self.module_name = []

        ### register AI models
        self.model_register = {}
        self.model_name = []

    ### register AI models
    def addModel(self, model_name):
        if model_name not in self.model_name:
            self.model_name.append(model_name)        

    def importModelClass(self):
        model_module = {}
        # layers = {}
        for model in self.model_name:
            mod = __import__(model, fromlist=["*"])
            model_module[model] = getattr(mod, model)
            self.model_register[model] = model_module[model](model)
            self.model_register[model].testMethod() 


    ### register layers
    def addModule(self, module_name):
        if module_name not in self.module_name:
            self.module_name.append(module_name)

    def importModules(self):
        layer_module = {}
        # layers = {}
        for module in self.module_name:
            mod = __import__(module, fromlist=["*"])
            layer_module[module] = getattr(mod, module)
            self.layer_register[module] = layer_module[module](module)
            self.layer_register[module].testMethod()

    ### add visual sets
    #parameter.addVisuals(FOLDER_PATH)
    def addVisuals(self, set_name, folder_path):
        print("Add visual sets")

    ### process attribute node ids
    # generate a ranomd id within the max_id range
    def generateID(self):
        id = random.randint(1, self.max_id)        
        return id
    # change max id
    def setMaxID(self, number):
        self.max_id = number