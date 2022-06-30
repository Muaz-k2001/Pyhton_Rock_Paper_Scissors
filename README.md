# Python_Rock_Paper_Scissors

A model was created from https://teachablemachine.withgoogle.com/ for each option possible in a rock-paper-scissors game. This model is going to be used in a game which will be coded using python. The following README file documents the progress I made along the way.

##The base game
The manual_rps.py file was created as a rock paper scissors game which doesn't yet use the camera. Instead, it relies on the user typing out their choice. In this file there are four functions:
  - **get_computer_choice()** which makes the computer pick a random choice out of the three options
  - **get_user_choice()** which takes the user's input, and repeatedly asks again if the input isn't either rock, paper or scissors.
  - **get_winner()** which checks the user input relative to the computer choice according to the classic rock, paper, scissors rules to decide who won
  - **play()** which ties together and runs the previous functions and prints the outcome of get_winner()

##Camera input
The camera_rps.py file replaces the user input with camera input. The get_user_choice() function was replaced by the **get_prediction()** function in which the camera input is coded. The code shows probabilities in a numpy array of the possible choices the user is displaying to the camera. The highest probability is used to predict what the user's desired input is.

##Countdown
There is a countdown feature added to direct the user to display their hand as would be done in a real game. This uses the time.time() function as opposed to the sleep() function due to the requirement of continuous camera input which the sleep() function inhibits.

##First to 3
Also there is a first to 3 wins system after which the game ends and the winner is decided. The play function contains a while loop which runs the entire game when the value of self.end is False, and at 3 wins this value is changed to True to end the game.
