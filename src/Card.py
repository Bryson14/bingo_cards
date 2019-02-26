import sys
import NumberSet


class Card:
    def __init__(self, idnum, size, numberSet):
        if isinstance(idnum, int):
            self.__idnum = idnum
        else:
            print("--Invalid ID Number--")

        if isinstance(size, int):
            self.__size = size
        else:
            print("--Invalid Size Type--")

        self.__numberSet = numberSet

    def getId(self):
        return self.__idnum

    def getSize(self):
        return self.__size

    def print(self, file=sys.stdout):
        """void function:
        Prints a card to the screen or to an open file object"""
        pass
