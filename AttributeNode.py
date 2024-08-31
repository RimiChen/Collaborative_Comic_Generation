### import library

from Parameters import *

# restrict used class
from typing import List, TypeVar, Generic

T = TypeVar("T", bound="AttributeNode")

### For testing RestrictedList, to restrict the element type of attribut list
class AnotherClass:
    pass

class RestrictedList(Generic[T]):
    def __init__(self):
        self._list: List[T] = []

    def append(self, item: T):
        if not isinstance(item, AttributeNode):
            raise TypeError(f"Only instances of \" {AttributeNode.__name__} \" are allowed")
        self._list.append(item)

    def __getitem__(self, index) -> T:
        return self._list[index]

    def __len__(self) -> int:
        return len(self._list)


class AttributeNode():
    def __init__(self, node_type, parameter:Parameters):
        ### restrict the element type in attribute list 
        self.attribute_list = RestrictedList[AttributeNode]()
        self.node_type = node_type

        # self.restrict_list = ["sequence", "panel", "character", "scene", "action", "number", "info"]


        ### get an identical ID
        new_id = parameter.generateID()
        while new_id in parameter.registeredID:
            new_id = parameter.generateID()
        # get a non-registered ID
        parameter.registeredID.append(new_id)
        self.attribute_id = new_id
        # told user that the node is created
        print("Create Node: type: ", node_type," id: ", self.attribute_id)

    ### Sample Method 
    # def append_restrict_list(self, new_type: str):
    #     self.restrict_list.append(new_type)
    # def generateID(self, max_number):
    #     id = random.randint(1, max_number)        
    #     return id

    def testMethod(self):
        print('Layer: ', self.layerName)

    # the main function
    def apply(self):
        pass





