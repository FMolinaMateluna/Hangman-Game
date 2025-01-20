import random

#For start the game, this fuction print a welcome for the game and chooses a aleatory word from the list, and return it.
def new_word ():
    list_game = ['EDUCATION', 'ACCOUNT', 'ADVANTAGE', 'BRILLIANT', 'ORDINARY', 'BATHROOM', 
            'SECRETARY', 'AMBULANCE', 'HELICOPTER', 'ASPARAGUS', 'WATERMELON', 'PREPOSITIONS' ]
    words_game = random.choice(list_game)
    print ('\n' + '﹊' * 20 + '\n')
    print (' Hello! ٩(◕‿◕)۶ Welcome to "Hangman"')
    print ('')
    print ( f'The word have {len(words_game)} letters, good lucky!!')
    print ('\n' + '﹎' * 20 + '\n')
    return (words_game)

'''For the logic of game, this fuction take a word from new_word fuction.
Bucle while: finish when the user complet 7 attempst o when guess the secret word '''

def play_game (words_game):
    correct_letter = ['_'] * len(words_game) 
    incorrect_letter = []
    attempst = 0 
    while attempst < 8 and '_' in correct_letter:
        user_letter = input('🍀 Choose a letter: ').upper() #The user input a aleatory letter
        if user_letter in words_game:
            if user_letter not in correct_letter:
                for index, letter in enumerate(words_game):
                    if letter == user_letter:
                        correct_letter[index] = user_letter
                print ('The letter is correct!')
                print ()
            else:
                print('You already guessed that letter!')
                print ()
                
        else:
            if user_letter not in incorrect_letter:
                attempst += 1
                incorrect_letter.append(user_letter)
                print ('The letter is incorrect, try again!')
                print (f'You have {(7 - attempst)} attempst now ')
                print ()
            else:
                print ('You already choose that letter!')
                print ()

        print (f'Word Secret: {correct_letter}')
        print ()   
        print (f'Incorrect letters: {incorrect_letter}')
        print ('\n' + '-' * 20 + '\n')

        win_game = list(set(words_game) - set(correct_letter))
        if len(win_game) == 0:
            print(f'Congratulations! You guessed the word! {words_game} 😎🏆')
        if attempst == 6:
            print('You don´t have more attempst, Game over! 😭')
            break

word = new_word()
play_game(word)