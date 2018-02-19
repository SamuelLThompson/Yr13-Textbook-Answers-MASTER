import random

class Card:
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["null", "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return (self.ranks[self.rank] + " of " + self.suits[self.suit])

    def cmp(self, other):               # Compares two cards (self and another), checks suits first as priority, returns 1 if self is ranked higher and -1 if the inverse is true
        if self.suit > other.suit:      # Check the suits
            return 1
        if self.suit < other.suit:
            return -1

        if self.rank > other.rank:
            if other.rank == 1:
                return -1 #other is Ace (and self is not)
            else:
                return 1
        if self.rank < other.rank:
            if self.rank == 1:
                return 1 #self is Ace (and other is not)
            else:
                return -1

        return 0                        # If everything ends up being the same, it's a tie


    def __eq__(self, other):            # Overrides the evaluation operators (<, >, ==, <=, >=, !=) and uses the value resulting from cmp(self, other) to determine the actual evaluation.
        return self.cmp(other) == 0

    def __le__(self, other):
        return self.cmp(other) <= 0

    def __ge__(self, other):
        return self.cmp(other) >= 0

    def __gt__(self, other):
        return self.cmp(other) > 0

    def __lt__(self, other):
        return self.cmp(other) < 0

    def __ne__(self, other):
        return self.cmp(other) != 0



class Deck:
    def __init__(self):
        self.cards = []                                 # Creates empty arrray for the cards
        for suit in range(4):                           # Generates a full, ordered deck of cards by going through the list that is defined within the card class in a nested loop
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))     # Appends each card it creates. This infact means that the deck ends up in reverse order

    def print_deck(self):
        for card in self.cards:
            print(card)

    def __str__(self):                          # Prints cards out nicely in order with every card on a new line
        s = ""                                  # Starts with a blank string
        for i in range(len(self.cards)):        # Goes through card array
            s = s + str(self.cards[i]) + "\n"   # Assigns the card of index i to s and then adds a new line marker "\n"
        return s                                # This infact means that when s is returned and printed, it is all one massive string, even though it appears on different lines.

    def shuffle(self):                  # Shuffles deck using the random module
        rng = random.Random()           # Create a random generator
        rng.shuffle(self.cards)         # Use its shuffle method to shuffle the list

    def remove(self, card):             # Removes a card from the deck, taking a card as a parameter
        if card in self.cards:          # loop to go through deck array looking for that card
            self.cards.remove(card)     # Removes that card
            return True                 # Returns True if that card was in the deck
        else:
            return False                # Returns false if it didn't find that card in the deck

    def pop(self):                      # "Pops" last element in out list (deals from the bottom of the deck)
        return self.cards.pop()

    def is_empty(self):                 # Checks if the list is empty, returns true if it is
        return self.cards == []

    def deal(self, hands, num_cards=999):
        num_hands = len(hands)
        for i in range(num_cards):
            if self.is_empty():
                break                    # Break if out of cards
            card = self.pop()            # Take the top card
            hand = hands[i % num_hands]  # Whose turn is next?
            hand.add(card)               # Add the card to the hand


class Hand(Deck):
    def __init__(self, name=""):
        self.cards = []
        self.name = name

    def add(self, card):
        self.cards.append(card)

    def __str__(self):
        s = "Hand " + self.name
        if self.is_empty():
            s += " is empty\n"
        else:
            s += " contains\n"
        return s + Deck.__str__(self)

class CardGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

class OldMaidHand(Hand):
    def remove_matches(self):
        count = 0
        original_cards = self.cards[:]
        for card in original_cards:
            match = Card(3 - card.suit, card.rank)
            if match in self.cards:
                self.cards.remove(card)
                self.cards.remove(match)
                print("Hand {0}: {1} matches {2}"
                        .format(self.name, card, match))
                count += 1
        return count

class OldMaidGame(CardGame):
    def play(self, names):
        # Remove Queen of Clubs
        self.deck.remove(Card(0,12))

        # Make a hand for each player
        self.hands = []
        for name in names:
            self.hands.append(OldMaidHand(name))

        # Deal the cards
        self.deck.deal(self.hands)
        print("---------- Cards have been dealt")
        self.print_hands()

        # Remove initial matches
        matches = self.remove_all_matches()
        print("---------- Matches discarded, play begins")
        self.print_hands()

        # Play until all 50 cards are matched
        turn = 0
        num_hands = len(self.hands)
        while matches < 25:
            matches += self.play_one_turn(turn)
            turn = (turn + 1) % num_hands

        print("---------- Game is Over")
        self.print_hands()

    def remove_all_matches(self):
        count = 0
        for hand in self.hands:
            count += hand.remove_matches()
        return count

    def play_one_turn(self, i):
        if self.hands[i].is_empty():
            return 0
        neighbor = self.find_neighbor(i)
        picked_card = self.hands[neighbor].pop()
        self.hands[i].add(picked_card)
        print("Hand", self.hands[i].name, "picked", picked_card)
        count = self.hands[i].remove_matches()
        self.hands[i].shuffle()
        return count

    def find_neighbor(self, i):
        num_hands = len(self.hands)
        for next in range(1,num_hands):
            neighbor = (i + next) % num_hands
            if not self.hands[neighbor].is_empty():
                return neighbor

    # EXERCISE 1 -------------------------------------------------------------------------------------------------------

    def print_hands(self):
        for hand in self.hands:
            print(hand)

    # ------------------------------------------------------------------------------------------------------------------

# NOT SURE ABOUT EXERCISE 2 AND 3. SEEMS LIKE THERE MIGHT BE SOME PREREQUISITE TASK IN ANOTHER CHAPTER THAT I HAVE NOT DONE,
# MIGHT ATTEMPT IT AT A LATER DATE SINCE I ALREADY FEEL PRETTY CONFIDENT WITH INHERITANCE.
