import random

class NumberSet():
    def __init__(self, size):
        self.__size = size
        self.__number_set = []
        for i in range(len(self.__size)):
            self.__number_set.append(i + 1)
        self.__next_index = 0

    def getSize(self):
        return self.__size

    def get(self, index):
        return self.__number_set[index]

    def randomize(self):
        random.shuffle(self.__number_set)

    def getNext(self):
        self.__next_index += 1
        if self.__next_index < len(self.__number_set):
            return self.__number_set[self.__next_index]
        else:
            return None
