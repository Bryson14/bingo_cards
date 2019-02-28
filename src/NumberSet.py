import random

class NumberSet():
    def __init__(self, size):
        self.__size = size
        self.__number_set = []
        for i in range(self.__size):
            self.__number_set.append(i + 1)
        self.__next_index = 0

    def getSize(self):
        return self.__size

    def get(self, index):
        return self.__number_set[index]

    def randomize(self):
        random.shuffle(self.__number_set)

    def getNext(self):
        if self.__next_index < len(self.__number_set):
            num = self.__number_set[self.__next_index]
            self.__next_index += 1
            return num
        else:
            self.__next_index += 1
            return None
