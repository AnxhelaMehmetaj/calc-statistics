import random
from Random_Func.randomNumber import randNum


class NumberBySeed(randNum):
    def __init__(self, start, end, seed):
        super().__init__(start, end)
        random.seed(seed)
        super(NumberBySeed, self).generateValue()