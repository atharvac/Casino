import pygame


CARDS = ['AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'KH', 'QH',
         'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'KD', 'QD',
         'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'KS', 'QS',
         'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'KC', 'QC',
         ]

FACES = {'A': [1, 11], 'K': [10], 'J': [10], 'Q': [10]}

SUITS = {'H': 'Hearts', 'D': 'Diamonds', 'S': 'Spades', 'C': 'Clubs'}

NAMES = {'A': 'Ace', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven',
         '8': 'Eight', '9': 'Nine', '10': 'Ten', 'J': 'Jack', 'Q': 'Queen', 'K': 'King'
         }


class Cards:
    def __init__(self, name, deck_id):
        self.id = name
        self.value = []
        self.suit = ''
        self.deck_id = deck_id
        self.card_name = ''

    def __str__(self):
        return self.card_name+" of "+self.suit

    def __repr__(self):
        return self.card_name+" of "+self.suit

    def load_card(self):
        return pygame.image.load(f"newPNG/{self.id}.png").convert()

    def set_val(self):
        if len(self.id) == 2:
            if self.id[0] not in FACES:
                self.value.append(int(self.id[0]))
                self.suit = SUITS[self.id[1]]
                self.card_name = NAMES[self.id[0]]
            else:
                self.value = FACES[self.id[0]]
                self.suit = SUITS[self.id[1]]
                self.card_name = NAMES[self.id[0]]
        else:
            self.value.append(10)
            self.suit = SUITS[self.id[2]]
            self.card_name = NAMES[self.id[:2]]


def generate_deck(number_of_decks):
    cards_list = []
    for i in range(number_of_decks):
        for card in CARDS:
            cards_list.append(Cards(card, i))

    for card in cards_list:
        card.set_val()

    return cards_list


if __name__ == '__main__':
    print(__name__)
    new = generate_deck(1)
    k = 17
    for x in new:
        x.set_val()
    print(f"Value:{new[k].value}  suit:{new[k].suit}  id:{new[k].id}  deck:{new[k].deck_id}  card:{new[k].card_name}")
    print(new[k])
