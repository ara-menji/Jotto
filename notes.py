def get_jotto_word(word_choice):
    jotto_word_length = str(3)
    jotto_word_list=[str("fox"),str("hot"),str("try"),str("cry"),str("way")]
    jotto_word=jotto_word_list[random.randint(0,(len(jotto_word_list)-1))]
    jotto_word_set=set(jotto_word)
    
guess = str(raw_input("Enter a word with " + str(jotto_word_length) + " letters: "))
guess_set=set(guess)

common=guess_set&jotto_word_set
uncommon=guess_set^jotto_word_set

if len(guess_set) == 3:
    print("Your word has " + str(len(common)) + " common characters.")
    if jotto_word==guess:
        print("Congratulations, you have won. The word was " + str(jotto_word))
    else:
        print("Sorry, you have not won. You may try again.")
else:
    print "Sorry, you need to enter a word consisting of 3 different characters."
