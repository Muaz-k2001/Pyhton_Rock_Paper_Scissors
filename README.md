# Python_Rock_Paper_Scissors

A model was created from https://teachablemachine.withgoogle.com/ for each option possible in a rock-paper-scissors game. This model is going to be used in a game which will be coded using python. The following README file documents the progress made by the creator of the game at each milestone, and will end with the conclusions of what the creator understood from and felt about the project.

The manual_rps.py file was created as a rock paper scissors game which doesn't yet use the camera. Instead, it relies on the user typing out their choice. In this file there are four functions:
  - **get_computer_choice()** which makes the computer pick a random choice out of the three options
  - **get_user_choice()** which takes the user's input, and repeatedly asks again if the inpput isn't either rock, paper or scissors.
  - **get_winner()** which checks the user input relative to the computer choice according to the classic rock, paper, scissors rules to decide who won
  - **play()** which ties together and runs the previous functions and prints the outcome of get_winner()
