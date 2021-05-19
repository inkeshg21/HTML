
#Coding Challenge 3, hangman.py
# Name: Inkesh Gharti 
# Student No: NP03CS4S210006

# Hangman Game

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string
import os


WORDLIST_FILENAME = "words.txt"

# Responses to in-game events
# Use the format function to fill in the spaces
responses = [
    "I am thinking of a word that is {0} letters long",
    "Congratulations, you won!",
    "Your total score for this game is: {0}",
    "Sorry, you ran out of guesses. The word was: {0}",
    "You have {0} guesses left.",
    "Available letters: {0}",
    "Good guess: {0}",
    "Oops! That letter is not in my word: {0}",
    "Oops! You've already guessed that letter: {0}",
]
def choose_random_word(wordlist):
    """
    Chooses a random word from those available in the wordlist
    
    Args:
        all_words (list): list of available words (strings)
    
    Returns:
        a word from the wordlist at random
    """
    #random.choice will give the randome letter form the wordlist file
    return random.choice(wordlist).lower()



# end of helper code
# -----------------------------------




def load_words():
    """
    Generate a list of valid words. Words are strings of lowercase letters.

    Returns:
        A list of valid words.
        
    """
    # TODO: Fill in your code here
    # Load the list of words into the variable wordlist
    # Accessible from anywhere in the program
    # TODO: uncomment the below line once
    # you have implemented the load_words() function
     
    print("Loading word list from file...")
    
    #File: file
    File = open("C:/Users/Toshiba/OneDrive/Desktop/intro programm/python assig/Coding challenge/words.txt", 'r')
    #line: string
    line = File.read()
    # wordlist: list of strings
    wordlist = line.split()
    print(len(wordlist), "words loaded.")
    print("Welcome to Hangman Ultimate Edition")
    return wordlist
# will make the wordlist global or make avilable to all functions.
wordlist = load_words()


def is_word_guessed(word, letters_guessed):
    """
    Determine whether the word has been guessed

    Args:
        word (str): the word the user is guessing
        letters_guessed (list): the letters guessed so far
    
    Returns: 
        boolean, True if all the letters of word are in letters_guessed; False otherwise
    """
    # TODO: Fill in your the code here
    #assining the  variable count with 0 value
    count = 0
    # letters directly move or dive in word holding the value of word
    for letters in word:
        # Determine whether the word has been guessed by statment if letters is in letters_guessed
        if letters in letters_guessed:
            #letters_guessed till know
            count += 1
    #True if all the letters of word are in letters_guessed
    if count == len(word):
        return True
    #False otherwise
    else:
        return False


def get_guessed_word(word, letters_guessed):
    """
    Determines the current guessed word, with underscores

    Args:
        word (str): the word the user is guessing
        letters_guessed (list): which letters have been guessed so far
    
    Returns: 
        string, comprised of letters, underscores (_), and spaces that represents which letters have been guessed so far.
    """
    # TODO: Fill in your code here
    # To show the user which is empty
    string1 = ""
    #pasing key in word(list)
    for key in word:
        #when key in guessed word then it will show the word replacing _ dash.
        #letters guessed till know
        if key in letters_guessed:
            string1 += key        
        else:
            #will desplay the word (_ _ _ _) in this manner in 1st loop
            #if found the word in guessed letter then it will be (r_ _ _)
            string1 += "_ "
    #return the word with replacement
    return string1


def get_remaining_letters(letters_guessed):
    """
    Determine the letters that have not been guessed
    
    Args:
        letters_guessed: list (of strings), which letters have been guessed
    
    Returns: 
        String, comprised of letters that haven't been guessed yet.
    """
    # TODO: Fill in your code here
    
    count = 0
    #string.ascii_lowercase will give the list form a-z with lowercase alphabets
    s=[]
    s= list(string.ascii_lowercase)
    string1 = ""
    #letter will directly dive into s values 
    for letter in s:
        #letters_guessed: list (of strings), which letters have been guessed
        if letter in letters_guessed:
            # count +=1
            #count=0+1=1
            count += 1
        #will 
        else:
            string1 += letter
    #String, comprised of letters that haven't been guessed yet.
    return string1

def get_score():
    #open the word file and read all
    #for dispaly
    print("Player name \t\t\t Score")
    print("_____________________________________________")

    if not os.path.isfile("C:/Users/Toshiba/OneDrive/Desktop/intro programm/python assig/Coding challenge/Saved_data.txt"):
        message=("Score Doesn't exist")
        return message
    else:
        All_score=open("C:/Users/Toshiba/OneDrive/Desktop/intro programm/python assig/Coding challenge/Saved_data.txt",'r')
        #assine all the thing of  flie to variable show
        show=All_score.read()
        #display what file contain
        print(show)
        #close the file
        All_score.close()
def save_score(name,Total_score):
    #open the file with update 
    All_score=open("C:/Users/Toshiba/OneDrive/Desktop/intro programm/python assig/Coding challenge/Saved_data.txt", "a")
    #give new line in file
    All_score.write("\n")
    #update the name in file
    All_score.write(name)
    #space after name
    All_score.write("\t\t\t\t")
    #update the Total score in file
    All_score.write(str(Total_score))
    #close the file
    All_score.close()
    
    


def hangman(word):
    """
    Runs an interactive game of Hangman.

    Args:
        word: string, the word to guess.
    """
    
    
    exit1=input("Do you want to Play (p) view the leaderboard (l) or quit (q): ") 
    if exit1=='p':
        exit1=1
    elif exit1=='l':
        get_score()
        hangman(word)
    else:
        exit1=0
    #will give random word for each game
    word=random.choice(wordlist)
    length=len(word)
    while(exit1==1):
                      
        if exit1!='q':
            
            name=input("enter your name")
            print("I am thinking of a word that is {0} letters long.".format(length))
            #give the player chance (random word length*2). eg randome words =2  then the chances are for user to guess the word in 4 times.
            total_chances=chances = 2 *len(word)
            #letter_guessed list contain the guessed word by user. 
            letters_guessed = []
            while (chances != 0):
                print("-----------")
                # if word entered by gamer m canot find in guseesed_word fuction then it will continue asking the user
                if word != get_guessed_word(word, letters_guessed):
                    #display the chances for gamer
                    print("You have {0} guesses left.".format(chances))
                    # will display the guessed latters in display
                    print("Available letters: {0}".format(get_remaining_letters(letters_guessed)))
                    #It will ask the user to guess the latter
                    guess = input("Please guess a letter: ")
                    #converting the guessed word in lowercase and word is assigne to guessInLowerCase
                    guessInLowerCase = guess.lower()
                    # Display the user that he/she has guessed the word already
                    if guessInLowerCase in letters_guessed:
                        print("Oops! You've already guessed that letter: {0}".format(get_guessed_word(word, letters_guessed)))
                    # Display the message to user that he/she has guessed the wrong word and reduce the chances by 1.  
                    elif guessInLowerCase not in word:
                        print("Oops! That letter is not in my word: {0}".format(get_guessed_word(word, letters_guessed)))
                        chances -= 1
                    #Display the message to user that he/she has guessed the write word.
                    else:
                        letters_guessed.append(guessInLowerCase)
                        print("Good guess: {0}".format(get_guessed_word(word, letters_guessed)))
                        
                    #The guessed letter will be added to the letters_guessed list
                    letters_guessed.append(guessInLowerCase)
                #If the random word matched to the letters_guessed then it will display the gamer has won the game 
                elif word == get_guessed_word(word, letters_guessed):
                    print("Congratulations, you won!")
                    #Give the points for gamer
                    Total_score=total_chances+chances
                    #Displaying the score
                    print("Your total score for this game is: {0}".format((Total_score)))
                    #Asking the player if hewant to save there score? if y 
                    Save=input("would you like to save data enter y if not enter n ")
                    if Save=='y' or 'yes':
                        save_score(name,Total_score)
                    
                    #break will end the game
                    break
            #If gamer doesn't guess the write word in given chance. Then it will display the gamer withsoryy message and the word he/she cannot guess.
            else:
                print("-----------")
                #give the gamer the word he doesn't able to guess as he was give chances.
                print("Sorry, you ran out of guesses. The word was: {0}.".format(word))
        #call the hangman again
        hangman(word)
        #if user enter except p then game will end here
        if(exit1!='p'):
            break
 
        
        




# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the last lines to test
# (hint: you might want to pick your own
# word while you're doing your own testing)


# -----------------------------------

# Driver function for the program
if __name__ == "__main__":
    # Uncomment the line below once you have finished testing.
    word = choose_random_word(wordlist)
    # Uncomment the line below once you have implemented the hangman function.
    hangman(word)
    #Display message if player exit the game
    print("Thanks for playing, goodbye!")
