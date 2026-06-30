from numpy import random 


    ##################################################################

def generateNumber():
        
    x = random.randint(100) # generates random number from 0-100
        
    return x

    ##################################################################

def getUserInput():

        while True:

            try:

                number = int(input("Guess Number (0-100)"))

                return number
            
            except ValueError:

                print("Enter a number")
                


    #################################################################

def checkAnswer(x):

        attempts = 5 # Attempts the user has

        while attempts > 0: #Only loops if user still has > 0 attempts

            number = getUserInput() # Gets user input into checkAnswer function
            
            if number < 1 or number > 100:
                print("Enter a number 1-100")
                continue

            elif number < x:
                print("Too Low!") 


            elif number > x:
                print("Too High!")
    

            else:
                print("Correct!") # If user guesses correct game stops
                print("You took", attempts, " guesses!")

                     


            print("Attempts left: ", attempts) # If wrong, attempts go down if too low and high
            attempts -= 1 

        print("Game over, answer: ", x) # if attempts are no longer > 0, it is game over


    #################################################################

randomNumber = generateNumber()
checkAnswer(randomNumber)

