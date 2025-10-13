#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Jeu de nim variante simple
"""

MAX_MATCHES = 21
MIN = 1
MAX = 5




def get_player(turn_number):
    """
    Returns player string relative to `turn_number`
    :param turn_number: The turn number integer
    :return: The player nickname
    """
    return first_player_str if turn_number % 2 == 0 else second_player_str


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
            print(f"Perdu {get_player(turn_number)}")
            exit()
    else:
        print(f"Entrez un chiffre entre {MIN} et {MAX} svp")
    display_humans(match_number, turn_number)


def display_computer(match_number, turn_number):
    """
    Display a game in a Human versus Computer format
    """
    global last_one
    if get_player(turn_number) == first_player_str:
        int_str = int(input(f"Tour {turn_number}: Combien d'allumettes voulez vous {first_player_str}?\n"))
        last_one = int_str
        if int_str in range(MIN, MAX):
            if check_matches(match_number, int_str):
                match_number -= int_str
                turn_number += 1
            else:
                print("Perdu")
                exit()
        else:
            print(f"Entrez un chiffre entre {MIN} et {MAX} svp")
    else:
        calc_int = 5 - last_one
        if check_matches(match_number, calc_int):
            match_number -= calc_int
            turn_number +=1
            print(f"Ordi a pris {calc_int}")
        else:
            print("Gagné")
            exit()
    display_computer(match_number, turn_number)



if __name__ == '__main__':
    first_player_str = str(input("Nom du joueur 1 ?\n"))
    second_player_str = str(input("Nom du joueur 2 ?\n"))

    matches = MAX_MATCHES
    turn = 0
    last_one = 0

    while matches > 0:
        display_computer(matches, turn)


