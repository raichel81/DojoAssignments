class Card(object):
    def __init__(self,color,suit,value,string): #suit is heart,value is 3, string is "q" or "3" in the card 
        self.suit = suit
        self.value = value
        self.string = string 
        self.color = color
    
class Deck(object):
    def __init__(self):
        self.cards = []
        self.makecards()
    def makecards(self):
        strings=["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
        suits = {"spade":"black" , "club":"black" , "heart": "red" , "diamond": "red"}
        for suit in suits:
            for index in range(0,len(strings)):
                color = suits[suit]
                value = index+1
                string = strings[index]
                card = Card(color,suit,value,string)
                self.cards.append(Card)
    makecards()

def deal_card(self):
    return self.cards.pop()
deal_card()

class player(object):
    def __init__(self,name,hand):
        self.name = name
        self.hand = hand
        def draw_card(self, deck):
            self.hand.append(deck.deal_card())
