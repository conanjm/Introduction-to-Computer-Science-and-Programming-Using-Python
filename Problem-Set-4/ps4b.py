from ps4a import *
import time

#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # Create a new variable to store the maximum score seen so far (initially 0)
    bestScore = 0

    # Create a new variable to store the best word seen so far (initially None)  
    bestWord = None

    # For each word in the wordList
    for word in wordList:

        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)

        if isValidWord(word, hand, wordList):

            # Find out how much making that word is worth
            score = getWordScore(word, n)
            # If the score for that word is higher than your best score
            if score > bestScore:
                # Update your best score, and best word accordingly
                bestScore = score
                bestWord = word

    # return the best word you found.
    return bestWord



#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    totalScore = 0
    while calculateHandlen(hand) > 0:
        print 'Current Hand:'+displayHand(hand)
        word = compChooseWord(hand, wordList, n)
        if word == None:
            break
        earned = getWordScore(word, n)
        totalScore += earned
        print '\"'+word+'\" earned', earned, 'points.',
        print 'Total:', totalScore, 'points'
        hand = updateHand(hand, word)


    print 'Total score:', totalScore, 'points.'
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    hand = {}
    choice = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game:')
    while choice != 'e':
        if choice == 'r':
            if not hand:
                print 'You have not played a hand yet. Please play a new hand first!'
                choice = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game:')
            else:
                choice2 = raw_input('Enter u to have yourself play, c to have the computer play:')
                while choice2 not in ['u', 'c']:
                    print 'Invalid command.'
                    choice2 = raw_input('Enter u to have yourself play, c to have the computer play:')
                if choice2 == 'u':
                    playHand(hand, wordList, HAND_SIZE)
                elif choice2 == "c":
                    compPlayHand(hand,wordList,HAND_SIZE)
                choice = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game:')
        elif choice == 'n':
            hand = dealHand(HAND_SIZE)
            choice2 = raw_input('Enter u to have yourself play, c to have the computer play:')
            while choice2 not in ['u', 'c']:
                print 'Invalid command.'
                choice2 = raw_input('Enter u to have yourself play, c to have the computer play:')
            if choice2 == 'u':
                playHand(hand, wordList, HAND_SIZE)
            elif choice2 == 'c':
                compPlayHand(hand, wordList, HAND_SIZE)
            else:
                print 'Invalid command.'
            choice = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game:')
        elif choice == 'e':
            break
        else:
            print 'Invalid command.'
            choice = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game:')
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


