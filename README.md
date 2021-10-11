# 🐍 Welcome to Pythons and Ladders!

💻 This project is the backend of Snakes and Ladders classic boardgame, developed in Python.
The logic of the game is developed as object oriented.

This game is intented to be platform agnostic, so it can be run on multiple devices.

📁 In the structure of the game you will find the main folder: SnakesAndLadders and the test folder, TestSnakesAndLadders. The main folder is divided according to elements of the game, such as the board, the players, the dice...

🧑‍🤝‍🧑 This is a multiplayer game, so you will have to type in a console input the number of the players that will play. Players will have numbers from 0 to infinite (but we don't recommend you to play with infinite friends, it could take some time to finish the game...)

🎲 In each turn you will have to press enter in order to roll the dice. Then, the terminal will show you the position of each player, the result of the dice and the turn they are playing.

📋 Rules of the game: our version, Pythons and Ladders, is inspired in the classic game, Snakes and Ladders. It is very easy to play: each player rolls the dice and they move across the squares of the board according to the dice result.
But... be careful with the pythons! If there is a head of a python in the square that a player reaches, she or he will have to move down across the python tail to a different square. Otherwise, if you reach the bottom of a ladder, you can climb to the top of it! Don't worry, the game will do it automatically so you don't have to think so much or count, just enjoy!

🏆 If you are the winner, the game will stop and you will find a congratulations message. To play again, run the game following the instructions below.

🔍 You can find the instructions to run the game and tests below:

## Start virtual env

```
pipenv shell
```

## Run tests

```
python -m pytest TestSnakesAndLadders/*
```

## Run game

```
python main.py
```
