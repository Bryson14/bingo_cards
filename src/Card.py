import sys
import NumberSet


class Card:
    def __init__(self, idnum, size, number_max):
        if isinstance(idnum, int):
            self.__idnum = idnum
        else:
            print("--Invalid ID Number--")

        if isinstance(size, int):
            self.__size = size
        else:
            print("--Invalid Size Type--")
        self.__numberSet = NumberSet.NumberSet(number_max)
        self.__numberSet.randomize()

    def getId(self):
        return self.__idnum

    def getSize(self):
        return self.__size

    def __print_divider(self):
        for i in range(self.__size):
            print("+-----", end="")
        print("+")

    def __print_data(self):
        for i in range(self.__size):
            print("| {}".format(self.__numberSet.getNext()), end="")
        print(" |")

    def print(self, file=sys.stdout):
        if file == sys.stdout:
            for i in range(self.__size):
                self.__print_divider()
                self.__print_data()
        else:
            pass


