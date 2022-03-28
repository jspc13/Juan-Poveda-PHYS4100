import numpy as np

rng = np.random.default_rng(12345) #creates the generator
cards = rng.choice(13, 5, replace=False) #randomly pick 5 numbers between 0 and 12 without repeiting
cards = cards + 1 #since cards go from 1 to 13, add 1 to the previous array
suits = rng.integers(0, 4, 5) #pikc 5 random integers between 0 and 3
suits_w_symbols = {0:u'\u2661', 1:u'\u2662', 2: u'\u2663', 3:u'\u2664'} # creates a dictionary assings a unicode

for i in range(len(cards)): #picks the ith index of cards (in str form) and the ith index of suits
    print(str(cards[i]) + suits_w_symbols[suits[i]]) # depending on the results of the int division of the
    # ith index of suits, it assigns the corresponding value of the dictionary
    #cards in string in order to be able to add them with the value of the dictionary


    