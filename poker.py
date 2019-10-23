from Cards import *


class PokerTable:
    MINIMUM_BLIND = 100
    CARDS_ON_DECK = []
    INITIAL_BALANCE = 5000

    def __init__(self, players=2, decks=1):
        self.NUM_PLAYERS = players
        self.NUM_DECKS = decks
        self.player_list = []
        for i in range(self.NUM_PLAYERS):
            self.player_list.append(Players(self.INITIAL_BALANCE))
        self.token = 0
        self.dealer = Dealer(self)


class Players:
    folded = False
    player_hand = []

    def __init__(self, initial_balance):
        self.balance = initial_balance


class Dealer:
    def __init__(self, table):
        self.play_table = table
        pass

    @staticmethod
    def isRoyalFlush():
        return True

    @staticmethod
    def isStraightFlush():
        return True

    @staticmethod
    def isFourOAK():
        return True

    @staticmethod
    def isFullhouse():
        return True

    @staticmethod
    def isFlush():
        return True

    @staticmethod
    def isStraight():
        return True

    @staticmethod
    def isThreeOAK():
        return True

    @staticmethod
    def isTwoPair():
        return True

    @staticmethod
    def isPair():
        return True

