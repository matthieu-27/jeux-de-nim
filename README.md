# Jeu de Nim

Une implémentation simple du jeu de Nim. Marienbad a venir.

## Description

Le jeu de Nim est un jeu ou les joueurs prennent tour à tour des allumettes d'un ou plusieurs tas (variante de Marienbad).
Le joueur qui prend la dernière allumette perd la partie.

## Comportement du bot

Le bot utilise la strategie *5 - n* ou *n* est le nombre joué par l'humain au tour précedent.

## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/matthieu-27/jeux-de-nim.git

2. Lancez le fichier via python 3:
   ```bash
   python nim_games.py

3. Choisissez un mode de jeu parmit humain contre humain ou humain contre bot

## Structure du programme

MAX_MATCHES = 21

MIN = 1

MAX = 5

````
def get_player(turn_number):

Returns player string relative to turn_number

Parameters
turn_number: The turn number integer

Returns
The player nickname
````
````
def check_matches(match_number, player_number):

Game logic for Nim game

Parameters
match_number: number of matches
player_number: choosen player number

Returns
True if we can take matches, False if matches at 0
````
````
def display_humans(match_number, turn_number):

Display a game in a Human versus Human format
````

````
def computer_5_minus_n(played_number, turn_number):

Returns 5 minus played_number integer incrementing turn_number
````

````
def check_and_increment(match_number, turn_number, played_number):

Main game logic, checks if next move is playable, returns False otherwise
````

````
def ask_player_input(turn_number):

Asks and returns user input incrementing turn_number
````
