import random
def play_game():
    goal =random.randint(1,100)
    # The goal of this game is to guess the secret number as quickly as possible
    name= input("Enter your name to start the game\n\n")
    user_guess = int(input("Guess Any number between 1 to 100\n\n"))
    steps = 0
    while user_guess != goal:
        if (user_guess < goal):
            user_guess = int(input("Gohigher in your guess\n"))
            steps +=1
        else:
            user_guess = int(input("Go lower in your guess\n"))
            steps +=1

    print("Congratulations!!{} you have guessed the secret number Correctly\n ".format(name))
    print("you took total of {} atempts to correctly guess the number\n".format(steps))
play_game()
choice = input("Enter 1 to play again any other input to quit \n\n")
while choice == '1':
    play_game()
print ("Thanks for playing")