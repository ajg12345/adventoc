""" Problem Prompt
you are riding on a camel with an elf
he wants to play a version of a game, A LOT like poker

take the input list of hands and bids. 
each hand produces a ranking, with bad/weird rules to implement tie breakers
each ranking has a value, for N cards, N is the greatest ranking and 1 is the least
calculate the total amount won, which is the sum of the product of each bid and its rank
"""
from pathlib import Path
from functools import total_ordering
from pprint import pprint

@total_ordering
class Card():
    def __init__(self, s:str):
        self.card_dict = {'A':13, 'K':12, 'Q':11, 'J':10, 'T':9, \
                          '9':8, '8':7, '7':6, '6':5, '5':4, '4':3, '3':2, '2':1}
        self.s = s
        self.svalue = self.card_dict[s]
    
    def __eq__(self, other):
        return self.svalue == other.svalue

    def __lt__(self, other):
        return self.svalue < other.svalue

@total_ordering
class Hand():
    def __init__(self, cards: list[Card], bid: int):
        self.cards = cards
        self.cards_str = ''.join([c.s for c in cards])
        self.cards_sorted = sorted(cards)[::-1]
        self.bid = bid
    
    # to be used as back up when comparing or sorting within a group
    def __gt__(self, other):
        for i in range(len(self.cards)):
            if self.cards[i].svalue == other.cards[i].svalue:
                continue
            elif self.cards[i].svalue > other.cards[i].svalue:
                return True
            else:
                return False
    
    def __eq__(self, other):
        for i in range(len(self.cards)):
            if self.cards[i].svalue != other.cards[i].svalue:
                return False
        return True


class FiveOfAKindGroup():
    def __init__(self):
        self.hand_list = list()
    
    def is_member(self, hand: Hand):
        cards = hand.cards
        return cards[0] == cards[1] == cards[2] == cards[3] == cards[4]
    
class FourOfAKind():
    def __init__(self):
        self.hand_list = list()
    
    def is_member(self, hand: Hand):
        cards = hand.cards_sorted
        return (cards[1] == cards[2] == cards[3] == cards[4]) or \
                (cards[1] == cards[2] == cards[3] == cards[0]) 
    
class FullHouseGroup():
    def __init__(self):
        self.hand_list = list()
    
    def is_member(self, hand: Hand):
        cards = hand.cards_sorted
        return ((cards[0] == cards[1] == cards[2]) and (cards[3] == cards[4])) or \
            ((cards[0] == cards[1]) and (cards[2] == cards[3] == cards[4]))

        
class ThreeOfAKindGroup():
    def __init__(self):
        self.hand_list = list()
    
    def is_member(self, hand: Hand):
        cards = hand.cards_sorted
        return ((cards[0] == cards[1] == cards[2]) and (cards[3] != cards[4])) or \
            ((cards[1] == cards[2] == cards[3]) and (cards[0] != cards[4])) or \
            ((cards[2] == cards[3] == cards[4]) and (cards[0] != cards[1]))

class TwoPairGroup():
    def __init__(self):
        self.hand_list = list()
    
    def is_member(self, hand: Hand):
        cards = hand.cards_sorted
        pair_count = 0
        for i in range(len(cards)-1):
            if cards[i] == cards[i+1]:
                pair_count += 1 
        return pair_count == 2

class OnePairGroup():
    def __init__(self):
        self.hand_list = list()
    
    def is_member(self, hand: Hand):
        cards = hand.cards_sorted
        pair_count = 0
        for i in range(len(cards)-1):
            if cards[i] == cards[i+1]:
                pair_count += 1 
        return pair_count == 1
    

class HighCardGroup():
    def __init__(self, ):
        self.hand_list = list()
    

def load_cards(line: str) -> Hand:
    hand, bid = line.split()
    cards = [Card(card) for card in hand]
    return Hand(cards, int(bid))

if __name__ == "__main__":
    
    input_filename = Path().absolute() / "2023" / "Day7" / "hands_bids.txt"

    myFiveOfAKind = FiveOfAKindGroup()
    myFourOfAKind = FourOfAKind()
    myFullHouse = FullHouseGroup()
    myThreeOfAKind = ThreeOfAKindGroup()
    myTwoPair = TwoPairGroup()
    myOnePair = OnePairGroup()
    myHighCard = HighCardGroup()

    hands = list()
    for line in input_filename.open():
        hands.append(load_cards(line))
    # iterate through each hand and decide which group it is in
    for hand in hands:
        if myFiveOfAKind.is_member(hand):
            myFiveOfAKind.hand_list.append(hand)

        elif myFourOfAKind.is_member(hand):
            myFourOfAKind.hand_list.append(hand)

        elif myFullHouse.is_member(hand):
            myFullHouse.hand_list.append(hand)

        elif myThreeOfAKind.is_member(hand):
            myThreeOfAKind.hand_list.append(hand)

        elif myTwoPair.is_member(hand):
            myTwoPair.hand_list.append(hand)

        elif myOnePair.is_member(hand):
            myOnePair.hand_list.append(hand)

        else:
            myHighCard.hand_list.append(hand)

    # extend all of the groups hands into a list in order
    hand_groups = [
        myFiveOfAKind,
        myFourOfAKind,
        myFullHouse,
        myThreeOfAKind,
        myTwoPair,
        myOnePair,
        myHighCard]
    # iterate through each group and decide what the ingroup ranking is
    for group in hand_groups:
        group.hand_list.sort()

    #combine all sorted groups of hands into a large sorted list of all hands
    sorted_hands = []
    for group in hand_groups:
        sorted_hands.extend(group.hand_list[::-1])

    #debug
    for hand in sorted_hands:
        print(hand.cards_str)
    # then iterate through that list of all hands and calculate running total of bids
    total_win_amount = 0
    for i in range(len(sorted_hands)):
        rank = len(sorted_hands) - i
        win_amount = rank * sorted_hands[i].bid
        total_win_amount += win_amount
    
    print('total_win_amount ' + str(total_win_amount))
    # assert total_win_amount == 6440
