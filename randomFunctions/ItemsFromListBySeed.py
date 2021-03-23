import random
from randomFunctions.ItemsFromList import ItemsFromList


class ItemsFromListBySeed(ItemsFromList):
    def __init__(self, array, n, seed):
        super().__init__(array, n)
        self.seed = seed
        random.seed(self.seed)
        super().generateChoices()