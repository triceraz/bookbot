import matplotlib.pyplot as plt
from stats import *

def decision():
    plot = input("Would you like some plots as well?: ")
    if plot.lower() == "yes":
        return True
    elif plot.lower() == "no":
        return False
    else:
        print("Say yes or no")
        return decision()

def plotting(text):
    words_length = count_words_length(text)
    x = list(words_length.keys())
    y = list(words_length.values())
    plt.bar(x,y)
    plt.xlabel("Word Length")
    plt.ylabel("Number of Words")
    plt.title("Word Length Distribution")
    plt.show()    
