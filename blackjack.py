from Cards import *
import random


class Blackjack:
    def __init__(self, decks):
        self.dealerTotal = 0
        self.dealerAlternate = 0

        self.playerTotal1 = 0
        self.playerTotal1Alt = 0

        self.playerTotal2 = 0
        self.playerTotal2Alt = 0

        self.no_of_decks = decks
        self.reserve_deck = generate_deck(self.no_of_decks)
        self.deck = self.reserve_deck
        self.player_deck1 = []
        self.player_deck2 = []
        self.dealer_deck = []
        self.split = False
        self.player1_bust = False
        self.player2_bust = False
        self.dealer_bust = False

    def hit(self, deck=1):
        new_card = random.choice(self.deck)
        # new_card = self.deck[3]
        self.deck.remove(new_card)
        if not self.split:
            self.player_deck1.append(new_card)
        else:
            if deck == 1:
                self.player_deck1.append(new_card)
            else:
                self.player_deck2.append(new_card)
        self.count_all()
        if deck == 1:
            if self.playerTotal1 > 21 and self.playerTotal1Alt > 21:
                return 1
        else:
            if self.playerTotal2 > 21 and self.playerTotal2Alt > 21:
                return 1
        return 0

    def dealer_hit(self):
        new_card = random.choice(self.deck)
        self.dealer_deck.append(new_card)
        self.deck.remove(new_card)
        self.count_all()

    def count_all(self):
        pd1 = 0
        pd2 = 0
        d = 0

        self.reset_total()

        for x_ in self.player_deck1:
            if x_.card_name == 'Ace':
                pd1 += 1
            self.playerTotal1 += x_.value[0]

        for x_ in self.player_deck2:
            if x_.card_name == 'Ace':
                pd2 += 1
            self.playerTotal2 += x_.value[0]

        for x_ in self.dealer_deck:
            if x_.card_name == 'Ace':
                d += 1
            self.dealerTotal += x_.value[0]

        self.playerTotal1Alt = self.playerTotal1 + (pd1 * 10)
        self.playerTotal2Alt = self.playerTotal2 + (pd2 * 10)
        self.dealerAlternate = self.dealerTotal + (d * 10)

        if self.playerTotal1 > 21 and self.playerTotal1Alt > 21:
            self.player1_bust = True
        elif self.dealerTotal > 21 and self.dealerAlternate > 21:
            self.dealer_bust = True
        if self.split:
            if self.playerTotal2 > 21 and self.playerTotal2Alt > 21:
                self.player2_bust = True

    def reset_total(self):
        self.dealerTotal = 0
        self.dealerAlternate = 0

        self.playerTotal1 = 0
        self.playerTotal1Alt = 0

        self.playerTotal2 = 0
        self.playerTotal2Alt = 0

    def reset_hand(self):
        self.reset_total()
        # self.deck = self.reserve_deck
        self.player_deck1 = []
        self.player_deck2 = []
        self.dealer_deck = []
        self.split = False
        self.player1_bust = False
        self.player2_bust = False
        self.dealer_bust = False

    def reset_all(self):
        self.reset_hand()
        self.deck = self.reserve_deck

    def dealer_play(self):
        stop = False
        while not stop:
            self.count_all()
            if self.dealerAlternate != 21:
                if self.dealerTotal <= 16:
                    self.dealer_hit()
                else:
                    stop = True
            else:
                stop = True
        if self.split:
            return [self.summary1(), self.summary2()]
        else:
            return [self.summary1()]

    def setup(self):
        for _ in range(2):
            self.hit()
            self.dealer_hit()
        self.count_all()
        if self.player_deck1[0].card_name == self.player_deck1[1].card_name:
            return 1    # Returns 1 if split is possible
        else:
            return 0    # Returns 0 if split not possible

    def split_cards(self):
        self.split = True
        self.player_deck2.append(self.player_deck1[1])
        self.player_deck1.pop()

    def stand(self):
        return self.dealer_play()

    def summary1(self):
        if self.player1_bust:
            return 1
        elif self.dealer_bust:
            return 0
        self.dealerTotal = self.g21(self.dealerTotal)
        self.dealerAlternate = self.g21(self.dealerAlternate)

        self.playerTotal1 = self.g21(self.playerTotal1)
        self.playerTotal1Alt = self.g21(self.playerTotal1Alt)

        if self.dealerTotal >= self.playerTotal1 and self.dealerTotal >= self.playerTotal1Alt:
            return 1
        elif self.dealerAlternate >= self.playerTotal1 and self.dealerAlternate >= self.playerTotal1Alt:
            return 1
        else:
            return 0

    def summary2(self):
        if self.player2_bust:
            return 1
        elif self.dealer_bust:
            return 0
        self.playerTotal2 = self.g21(self.playerTotal2)
        self.playerTotal2Alt = self.g21(self.playerTotal2Alt)
        if self.dealerTotal >= self.playerTotal2 and self.dealerTotal >= self.playerTotal2Alt:
            return 1
        elif self.dealerAlternate >= self.playerTotal2 and self.dealerAlternate >= self.playerTotal2Alt:
            return 1
        else:
            return 0

    @staticmethod
    def g21(z):
        if z > 21:
            return -99
        else:
            return z


if __name__ == '__main__':
    b1 = Blackjack(1)
    k = b1.setup()
    if k == 1:
        b1.split_cards()
    # b1.hit()
    print(b1.dealer_play())
    print(b1.player1_bust, b1.player2_bust, b1.dealer_bust)

    print(k, "Dealer: ", b1.dealer_deck)
    print("Player: ", b1.player_deck1)
    print("Player2: ", b1.player_deck2)
    print("Player Score:", b1.playerTotal1, b1.playerTotal1Alt)
    print("Player2 Score:", b1.playerTotal2, b1.playerTotal2Alt)
    print("Dealer Score:", b1.dealerTotal, b1.dealerAlternate)
