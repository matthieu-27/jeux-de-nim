#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Jeu de nim variante simple
"""

MAX_MATCHES = 21
MIN = 1
MAX = 4


def get_player(turn):
    return first_player_str if turn % 2 == 0 else second_player_str


def check_matches(match_number, player_number):
    if match_number - player_number >= 1:
        return True
    return False


def display(match_number, turn_number):
    int_str = int(input(f"Tour {turn_number}: Combien d'allumettes voulez vous {get_player(turn_number)}?\n"))
    if int_str in range(MIN, MAX+1):
        if check_matches(match_number, int_str):
            match_number -= int_str
            turn_number += 1
        else:
            print(f"Perdu {get_player(turn_number)}")
            exit()
    else:
        print(f"Entre un chiffre entre {MIN} et {MAX} svp")
    display(match_number, turn_number)



if __name__ == '__main__':
    first_player_str = str(input("Nom du joueur 1 ?\n"))
    second_player_str = str(input("Nom du joueur 2 ?\n"))

    matches = MAX_MATCHES
    turn = 0

    while matches > 0:
        display(matches, turn)


