from numpy import random 


def game():

##################################################################

    def generateNumber():

        x = random.randint(100) # generates random number from 0-100
        print(x)
        return x

##################################################################

    def getUserInput():

            while True:

                try:
                    print(" ")
                    number = int(input("Guess Number (0-100): "))

                    return number
                
                except ValueError:

                    print("Enter a number")
                    


#################################################################

    def checkAnswer(x):

        attempts = 0 # Attempts the user has

        while attempts < 5: #Only loops if user still has > 0 attempts

                number = getUserInput() # Gets user input into checkAnswer function
                
                if number < 1 or number > 100:
                    print("Enter a number 1-100")
                    continue

                elif number < x:
                    print("Too Low!") 


                elif number > x:
                    print("Too High!")
        

                else:
                    attempts += 1 

                    print("Correct!") # If user guesses correct game stops

                    print("You took", attempts ,"guess(es)!")

                    print("Would you like to play again?")

                    userOption = int(input("Yes: 1, No: 2: "))
                    if userOption == 1:
                        game()
                    else:
                        print("goodbye!")
                        break

                        

                attempts += 1 
                print("Attempts", attempts, "/5") # If wrong, attempts go down if too low and high

        print("Game over, answer: ", x) # if attempts are no longer > 0, it is game over

        print("Would you like to play again?")

        userOption = int(input("Yes: 1, No: 2: "))

        if userOption == 1:
            game()
        else:
            print("goodbye!")

    randomNumber = generateNumber()
    checkAnswer(randomNumber)

game()


    


#################################################################

    



