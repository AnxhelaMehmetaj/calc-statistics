from randomFunctions.ItemFromList import ItemFromList


class ItemsFromList(ItemFromList):
    def __init__(self, array, n):
        super().__init__(array)
        self.items = []
        self.n = n
        self.generateChoices()

    def generateChoices(self):
        if self.n > len(self.array):
            self.items = "ERROR: n is greater then array size"
        else:
            for i in range(self.n):
                super().generateChoice()
                # want to append randomly chosen value from
                # array and remove that value from the
                # list so we don't choose it again
                self.items.append(super().getValue())
                self.array.remove(super().getValue())

    def getValue(self):
        return self.items