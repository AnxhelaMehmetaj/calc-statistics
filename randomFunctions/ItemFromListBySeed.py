import random
from randomFunctions.ItemFromList import ItemFromList


class ItemsFromList(ItemFromList):
    def __init__(self, array, seed):
        super().__init__(array)
        self.genItems = []
        random.seed(seed)
        super().generateChoice()