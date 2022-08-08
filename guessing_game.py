import streamlit as st
import random

user_guess = 0
steps = 0
name = 'Default'

def user_input_name():
    try:
        name= st.text_input("Enter your name to start the game\n\n")
        user_guess = int(st.text_input("Guess Any number between 1 to 100\n\n"))
    except:
        pass

def go_higher():
    try:
        user_guess = int(st.text_input("Gohigher in your guess\n"))
        steps +=1
    except:
        pass
def go_lower():
    try:
        user_guess = int(st.text_input("Go Lower in your guess\n"))
        steps +=1
    except:
        pass
def winner():
    st.write("Congratulations!!{} you have guessed the secret number Correctly\n ".format(name))
    st.write("you took total of {} atempts to correctly guess the number\n".format(steps))

def play_again():
    try:
        choice = st.text_input("Enter 1 to play again any other input to quit \n\n")
        while (choice == '1'):
            play_game()
        st.write ("Thanks for playing")
    except:
        pass
    
def play_game():
    goal =random.randint(1,100)
    # The goal of this game is to guess the secret number as quickly as possible
    steps = 0
    user_input_name()
    while user_guess != goal:    
        
            if (user_guess < goal):
                go_higher()
                
            else:
                go_lower()
    winner()  
    play_again()          

        
    
play_game()

