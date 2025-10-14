#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Jeu de nim variante simple
"""
import random

MAX_MATCHES = 21
MIN = 1
MAX = 5


def get_player(turn_number):
    """
    Returns player string relative to `turn_number`
    :param turn_number: The turn number integer
    :return: The player nickname
    """
    return player_one if turn_number % 2 == 0 else player_two


def check_matches(match_number, player_number):
    """
    Game logic for Nim game
    :param match_number: number of matches
    :param player_number: choosen player number
    :return: True if we can take matches, False if matches at 0
    """
    if match_number - player_number >= 1:
        return True
    return False


def display_humans(match_number, turn_number):
    """
    Display a game in a Human versus Human format
    """
    int_str = int(input(f"Tour {turn_number}: Combien d'allumettes voulez vous {get_player(turn_number)}?\n"))
    if int_str in range(MIN, MAX):
        if check_matches(match_number, int_str):
            match_number -= int_str
            turn_number += 1
        else:
            print(f"Il reste{match_number} allumettes. C'est terminé {get_player(turn_number)}")
            exit()
    else:
        print(f"Entrez un chiffre entre {MIN} et {MAX} svp")
    display_humans(match_number, turn_number)


def computer_5_minus_n(played_number, turn_number):
    computer_take = 5 - played_number
    turn_number += 1
    return computer_take, turn_number


def check_and_increment(match_number, turn_number, played_number):
    if played_number in range(MIN, MAX):
        if check_matches(match_number, played_number):
            print(f"{get_player(turn_number-1)} a pris {played_number} allumettes")
            return True
        else:
            print(f"Il reste {match_number} allumettes, la partie est terminée {get_player(turn_number-1)}")
            return False
    else:
        print(f"Veuillez entrez un chiffre entre {MIN} et {MAX}.")
        ask_player_input(turn_number)
    return False


def ask_player_input(turn_number):
    int_str = int(input(f"Tour {turn_number}: Combien d'allumettes voulez vous {player_one}?\n"))
    turn_number += 1
    return int_str, turn_number


if __name__ == '__main__':
    player_one, player_two = str(input("Nom du joueur 1 et 2 (séparés par -) ?\n")).split('-')
    game_mode = int(input("Mode de jeu: 1 - Humain vs Humain | 2 - Humain vs Ordinateur"))
    turn, last_pick = 0, 0
    game_over = False
    match_number = 21

    while not game_over:
        if not game_over and turn == 0:
            match_number = 21
        if game_mode == 1:
            display_humans(match_number, turn)
        if game_mode == 2:
            if turn % 2 == 0:
                last_pick, turn = ask_player_input(turn)
                if not check_and_increment(match_number, turn, last_pick):
                    game_over = True
                match_number -= last_pick
            else:
                computer_number, turn = computer_5_minus_n(last_pick, turn)
                if not check_and_increment(match_number, turn, computer_number):
                    game_over = True
                match_number -= computer_number

        if game_over:
            break