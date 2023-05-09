# Black_Jack
This is a Python program that simulates a game of Blackjack. It uses the command line interface and the user plays against the computer. The program uses basic game rules and functions to calculate scores and determine the winner.




Blackjack Game
This is a simple command-line game of Blackjack, built using Python. The objective of the game is to have a hand value of 21 or as close to 21 as possible without going over (busting).

Game Rules
The player starts with two random cards, and so does the dealer.
The player can choose to hit (draw another card) or stand (stop drawing cards).
Aces can be worth 1 or 11 points, face cards are worth 10 points, and all other cards are worth their face value.
The dealer must keep drawing cards until their hand value is at least 17.
If the player goes over 21, they bust and automatically lose.
If the dealer goes over 21, the player automatically wins.
If the player has a higher hand value than the dealer without going over 21, they win.
If the player and dealer have the same hand value, it's a draw.
How to Play
To play the game, simply run the blackjack.py file in a Python environment. The game will prompt you to enter 'Y' or 'N' to start or end the game, respectively. Follow the on-screen instructions to play each round of the game.

Technologies Used
This game was built using Python 3.9.6 and includes the following modules:

random for shuffling and drawing cards randomly
replit for clearing the console screen
art for ASCII art logo
