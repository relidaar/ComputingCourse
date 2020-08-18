# Mini-project #6 - Blackjack

import random
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")

# initialize some useful global variables
in_play = False
outcome = ""
wins = 0
losses = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos, hidden=False):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))

        if hidden:
            canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_SIZE,
                              [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        else:
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]],
                              CARD_SIZE)


# define hand class
class Hand:
    def __init__(self):
        self.cards = []
        self.hidden = []

    def __str__(self):
        s = "Hand contains"
        for card in self.cards:
            s += ' %s' % (card)
        return s

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        ranks = [c.get_rank() for c in self.cards]
        result = sum([VALUES[r] for r in ranks])

        if 'A' in ranks and result + 10 <= 21:
            result += 10
        return result

    def hide_card(self, i):
        self.hidden.append(i - 1)

    def open_all(self):
        self.hidden = []

    def draw(self, canvas, pos):
        x = pos[0]
        for i, card in enumerate(self.cards):
            if i in self.hidden:
                card.draw(canvas, (x, pos[1]), True)
            else:
                card.draw(canvas, (x, pos[1]))
            x += CARD_SIZE[0] + CARD_SIZE[0] // 3


# define deck class
class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                card = Card(suit, rank)
                self.cards.append(card)

    def shuffle(self):
        # shuffle the deck
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

    def __str__(self):
        s = "Deck contains"
        for card in self.cards:
            s += ' %s' % (card)
        return s


# define event handlers for buttons
def deal():
    global outcome, in_play, deck, player, dealer, wins, losses
    if in_play:
        outcome = "You lost"
        losses += 1

    deck = Deck()
    deck.shuffle()

    player = Hand()
    dealer = Hand()

    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())

    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    dealer.hide_card(1)

    outcome = ''
    in_play = True


def hit():
    global player, deck, in_play, score, outcome, losses
    if not in_play:
        return

    player.add_card(deck.deal_card())

    if player.get_value() > 21:
        outcome = 'You have busted'
        in_play = False
        losses += 1
        dealer.open_all()


def stand():
    global player, dealer, deck, in_play, score, outcome, wins, losses
    if not in_play:
        return

    while dealer.get_value() < 17:
        dealer.add_card(deck.deal_card())

    player_value = player.get_value()
    dealer_value = dealer.get_value()

    if dealer_value > 21:
        outcome = 'Dealer have busted'
        wins += 1
    elif player_value > dealer_value:
        outcome = 'You won'
        wins += 1
    else:
        outcome = 'You lost'
        losses += 1

    in_play = False
    dealer.open_all()


# draw handler
def draw(canvas):
    canvas.draw_text("Blackjack", (200, 50), 40, "white")
    msg = "Hit or stand?" if in_play else "New deal?"
    canvas.draw_text(msg, (50, 100), 30, "white")

    canvas.draw_text('Wins: ' + str(wins), (300, 100), 30, "white")
    canvas.draw_text('Losses: ' + str(losses), (450, 100), 30, "white")
    canvas.draw_text(outcome, (300, 150), 30, "white")

    canvas.draw_text("Dealer", (50, 200), 30, "white")
    dealer.draw(canvas, (50, 220))

    canvas.draw_text("Player", (50, 400), 30, "white")
    player.draw(canvas, (50, 420))


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

# create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit", hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
deal()
frame.start()

# remember to review the gradic rubric