import random
list_of_words = ["maroc" , "algerie" , "tunisie" , "egypt" , "libie" , "mouritanie"  , "yemen" , "iraq"]
def word_game(words):
    picked_word = random.choice(words)
    #nkhrb9o l'ordre dialha 
    str(picked_word)
    
    return picked_word

result = word_game(list_of_words)
print(result)
    