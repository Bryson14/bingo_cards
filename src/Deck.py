import sys
import Card
import NumberSet


class Deck:
    def __init__(self, cardSize, cardCount, numberMax):
        self.__cardCount = int(cardCount)
        self.__numset = NumberSet.NumberSet(numberMax)
        self.__m_cards = []
        for i in range(len(cardCount)):
            card = Card.Card(i, cardSize, self.__numset)
            self.__m_cards.append(card)
            
    def getCardCount(self):
        return self.__cardCount

    def getCard(self, n):
        """Return card N from the deck"""
        card = None
        n -= 1
        if 0 <= n < self.__cardCount:
            card = self.__m_cards[n]
        return card;


    def print(self, file=sys.stdout, idx=None):
        """void function: Print cards from the Deck

        If an index is given, print only that card.
        Otherwise, print each card in the Deck
        """
        if idx is None:
            for idx in range(1, self.__m_cardCount + 1):
                c = self.getCard(idx)
                c.print(file)
            print('', file=file)
        else:
            self.getCard(idx).print(file)

