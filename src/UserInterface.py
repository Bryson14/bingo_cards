import Deck
import Menu


class UserInterface:
    def __init__(self):
        self.__cardSize = 0
        self.__deckSize = 0
        self.__maxNumber = 0

    def run(self):
        """Present the main menu to the user and repeatedly prompt for a valid command"""
        print("Welcome to the Bingo! Deck Generator\n")
        menu = Menu.Menu("Main")
        menu.addOption("C", "Create a new deck")
        
        keepGoing = True
        while keepGoing:
            command = menu.show()
            if command == "C":
                self.__createDeck()
            elif command == "X":
                keepGoing = False

    def __createDeck(self):
        """Command to create a new Deck"""

        correctSize = correctCount = correctMax = False
        while not correctSize:
            cardSize = int(input("What N*N dimension of card do you want? "))
            if isinstance(cardSize, int) and 1 < cardSize:
                correctSize = True
                self.__cardSize = cardSize
            else:
                print("Enter a valid card size greater than 1. ")

        while not correctCount:
            cardCount = int(input("How many cards do you want in your deck? "))
            if isinstance(cardCount, int) and 0 < cardCount:
                correctCount = True
                self.__deckSize = cardCount
            else:
                print("Enter a valid amount of cards greater than 0. ")
        while not correctMax:
            maxNumber = int(input("What should be the max number between {} and {}. "
                            .format(2 * cardSize * cardSize, 4 * cardSize * cardSize)))
            if 2 * cardSize * cardSize <= maxNumber <= 4 * cardSize * cardSize:
                self.__maxNumber = maxNumber
                correctMax = True
            else:
                pass

        self.__m_currentDeck = Deck.Deck(cardSize, cardCount, maxNumber)
        self.__deckMenu()

    def __deckMenu(self):
        """Present the deck menu to user until a valid selection is chosen"""
        menu = Menu.Menu("Deck")
        menu.addOption("P", "Print a card to the screen")
        menu.addOption("D", "Display the whole deck to the screen")
        menu.addOption("S", "Save the whole deck to a file")

        keepGoing = True
        while keepGoing:
            command = menu.show()
            if command == "P":
                self.__printCard()
            elif command == "D":
                self.__m_currentDeck.print()
            elif command == "S":
                self.__saveDeck()
            elif command == "X":
                keepGoing = False

    def __getNumberInput(self, message, indx, cardCount)->int:
        if indx < cardCount:
            return indx

    def __getStringInput(self, message):
        fileName = input(message)
        return fileName

    def __printCard(self):
        """Command to print a single card"""
        cardToPrint = self.__getNumberInput("Id of card to print", 1, self.__m_currentDeck.getCardCount())
        if cardToPrint > 0:
            print()
            self.__m_currentDeck.print(idx=cardToPrint)

    def __saveDeck(self):
        """Command to save a deck to a file"""
        fileName = self.__getStringInput("Enter output file name: ")
        if fileName != "":
            outputStream = open(fileName, 'w')
            self.__m_currentDeck.print(outputStream)
            outputStream.close()
            print("Done!")
