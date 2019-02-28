import sys
import NumberSet


class Card:
    def __init__(self, idnum, size, num_set):
        if isinstance(idnum, int):
            self.__idnum = idnum
        else:
            print("--Invalid ID Number--")

        if isinstance(size, int):
            self.__size = size
        else:
            print("--Invalid Size Type--")
        self.__numberSet = num_set
        self.__numberSet.randomize()

    def getId(self):
        return self.__idnum

    def getSize(self):
        return self.__size

    def __print_divider(self, file):
        for i in range(self.__size):
            print("+-----", end="", file=file)
        print("+", file=file)

    def __print_data(self, file):
        for i in range(self.__size):
            print("|{:^5}".format(self.__numberSet.getNext()), end="", file=file)  # {:^n} is center align
        print("|", file=file)

    def __print_free_row(self, file):
        for i in range(self.__size):
            if self.__size // 2 == i:
                print("|{:^5}".format("FREE"), end="", file=file)
            else:
                print("|{:^5}".format(self.__numberSet.getNext()), end="", file=file)
        print("|", file=file)

    def print(self, file=sys.stdout):

        if self.__size % 2 == 0:
            for i in range(self.__size):
                self.__print_divider(file)
                self.__print_data(file)
            self.__print_divider(file)
        else:
            for i in range(self.__size):
                self.__print_divider(file)
                if self.__size // 2 == i:
                    self.__print_free_row(file)
                    pass
                else:
                    self.__print_data(file)
            self.__print_divider(file)

        self.__numberSet.reset_index()
