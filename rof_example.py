"""
~~~~~~~~~~~~CARD VALUES~~~~~~~~~~~~
ACE: WATERFALL!!!! - Everyone drinks until the person who picked the card stops.
Two: You - You can choose someone to take a drink.
Three: Me - You must take a drink.
Four: Whores - All girls drink.
Five: Thumbs - Card picker places their thumbs somewhere, everyone else puts their
      thumb in the same place. Last to do so takes a drink.
Six: Dicks - All boys take a drink.
Seven: Heaven - Point to the sky, last person takes a drink.
Eight: Date - Choose someone, whenever you drink, they drink.
Nine: Rhyme - Pick a word, next person rhymes, then the next and so on. If you mess
      up you drink.
Ten: Category - Pick a category, everyone says something from that category. If you
     mess up, you drink.
Jack: Make a Rule - Everyone follows the rule, if they don't, they drink.
Queen: Question master - Keep asking question, if they answer you then they drink,
       if they tell you to fuck off, you drink.
King: Community drink - For Kings 1 to 3, pour a little of your drink into the community
      pot, whoever gets the last king adds to the pots then drinks it all.
"""
import random

# Lists & Variables
hearts = ['♥Ace♥', '♥Two♥', '♥Three♥', '♥Four♥', '♥Five♥', '♥Six♥', '♥Seven♥', '♥Eight♥', '♥Nine♥', '♥Ten♥', '♥Jack♥', '♥Queen♥', '♥King♥']
diamonds = ['♦Ace♦', '♦Two♦', '♦Three♦', '♦Four♦', '♦Five♦', '♦Six♦', '♦Seven♦', '♦Eight♦', '♦Nine♦', '♦Ten♦', '♦Jack♦', '♦Queen♦', '♦King♦']
spades = ['♠Ace♠', '♠Two♠', '♠Three♠', '♠Four♠', '♠Five♠', '♠Six♠', '♠Seven♠', '♠Eight♠', '♠Nine♠', '♠Ten♠', '♠Jack♠', '♠Queen♠', '♠King♠']
clubs = ['♣Ace♣', '♣Two♣', '♣Three♣', '♣Four♣', '♣Five♣', '♣Six♣', '♣Seven♣', '♣Eight♣', '♣Nine♣', '♣Ten♣', '♣Jack♣', '♣Queen♣', '♣King♣']
deck = hearts + diamonds + spades + clubs


# Program

def draw_card():
    drawn_card = random.choice(deck)
    deck.remove(drawn_card)
    print(drawn_card)
    input('Press enter to draw the next card.')


exit = False
d = len(deck)
while not exit:
    if d == 0:
        print('You have finished the game.')
        exit = True
    else:
        draw_card()
        d = d - 1
