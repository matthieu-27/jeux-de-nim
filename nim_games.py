#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Jeu de nim variante simple
"""
MAX_MATCHES, MIN, MAX = 21, 1, 5
MARIENBAD = [7, 5, 3, 1]


def get_player(_turn_number):
    """
    Returns player string relative to `turn_number`
    :param _turn_number: The turn number integer
    :return: The player nickname
    """
    return player_one if _turn_number % 2 == 0 else player_two


def check_matches(_match_number, _player_number):
    """
    Game logic for Nim game
    :param _match_number: number of matches
    :param _player_number: choosen player number
    :return: True if we can take matches, False if matches at 0
    """
    if _match_number - _player_number >= 1:
        return True
    return False


def check_matches_marienbad(_marienbad, _player_number, _pile_number):
    """
    Game logic for Nim game (Marienbad)
    :param _marienbad: number of matches (Marienbad)
    :param _player_number: choosen player number
    :return: True if we can take matches, False if matches at 0
    """
    if _marienbad[_pile_number] - _player_number >= 1:
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
            print(f"Il reste {match_number} allumettes. C'est terminé {get_player(turn_number)}")
            exit()
    else:
        print(f"Entrez un chiffre entre {MIN} et {MAX} svp")
    display_humans(match_number, turn_number)


def display_humans_marienbad(_marienbad, _turn_number):
    """
    Display a game in a Human versus Human format (Marienbad)
    """
    pile_str = int(input(f"Quel tas choisissez vous {get_player(_turn_number)}?"))
    int_str = int(input(f"Tour {_turn_number}: Combien d'allumettes voulez vous ?\n"))
    if int_str in range(MIN, MAX):
        if check_matches_marienbad(_marienbad, int_str, pile_str):
            _marienbad[pile_str] = _marienbad[pile_str] - int_str
            _turn_number += 1
        else:
            print(f"Il reste {_marienbad[pile_str]} allumettes. C'est terminé {get_player(_turn_number)}")
            exit()
    else:
        print(f"Entrez un chiffre entre {MIN} et {MAX} svp")
    _turn_number += 1
    display_marienbad(_marienbad, _turn_number)


def computer_5_minus_n(_played_number, _turn_number):
    """
    Returns 5 minus `played_number` integer incrementing `turn_number`
    """
    computer_take = 5 - _played_number
    _turn_number += 1
    return computer_take, _turn_number


def display_marienbad(_marienbad, _turn_number, _count):
    _str = ''
    for n in marienbad:
        _str += f" |  - Tas numéro {_marienbad.index(n) + 1}" if n == len(marienbad) else " | "
    print(f"Tour numéro {_turn_number}\n" if count == 1 else "")
    _count += 1
    print(_str)



def compute_marienbad(_marienbad, _played_number, _turn_number):
    _pick, _pile = 0, 0
    if _marienbad[3] == 1:
        _pile = 3
        _pick = 1
        _turn_number += 1
    elif _marienbad[2] <= 3:
        _pile = 2
        _pick = max(_marienbad[_pile])
        _turn_number += 1
    elif _marienbad[1] <=5:
        _pile = 1
        _pick = computer_5_minus_n(_played_number, _turn_number)
    elif _marienbad[0] <= 7:
        _pile = 0
        _pick = computer_5_minus_n(_played_number, _turn_number)
    return _pick, _pile, _turn_number


def is_legal_move(_match_number, _turn_number, _played_number):
    """
    Main game logic, checks if next move is playable, returns False otherwise
    """
    if _played_number in range(MIN, MAX):
        if check_matches(_match_number, _played_number):
            print(f"{get_player(_turn_number - 1)} a pris {_played_number} allumettes")
            return True
        else:
            print(f"Il reste {_match_number} allumettes, la partie est terminée {get_player(_turn_number - 1)}")
            return False
    else:
        print(f"Veuillez entrez un chiffre entre {MIN} et {MAX}.")
        ask_player_input(_turn_number)
    return False


def ask_player_input(_turn_number):
    """
    Asks and returns user input incrementing `turn_number`
    """
    int_str = int(input(f"Tour {_turn_number}: Combien d'allumettes voulez vous {player_one}?\n"))
    _turn_number += 1
    return int_str, _turn_number


def ask_player_input_marienbad(_turn_number):
    pile_str = int(input(f"Quel tas choisissez vous {get_player(_turn_number)}?"))
    int_str = int(input(f"Tour {_turn_number}: Combien d'allumettes voulez vous {get_player(_turn_number)}?\n"))
    _turn_number += 1
    return int_str, pile_str - 1, turn


def is_legal_move_marienbad(_marienbad, _played_number, _pile_number, _turn_number):
    if _played_number in range(MIN, MAX):
        if check_matches(_marienbad[_pile_number], _played_number):
            print(f"{get_player(_turn_number - 1)} a pris {_played_number} allumettes")
            return True
        else:
            print(f"Il reste {_marienbad[_pile_number]} allumettes, la partie est terminée {get_player(_turn_number - 1)}")
            return False
    else:
        print(f"Veuillez entrez un chiffre entre {MIN} et {MAX}.")
        ask_player_input_marienbad(_turn_number)
    return False


if __name__ == '__main__':
    player_one, player_two = str(input("Nom du joueur 1 et 2 (séparés par ,) ?\n")).split(',')
    game_mode = int(input("Mode de jeu: 1 - Humain vs Humain | 2 - Humain vs ordinateur | "
                          "3 - Humain vs ordinateur (Marienbad) | 4 - Humain vs humain (Marienbad)\n"))
    turn, last_pick = 0, 0
    game_over = False
    match_number = MAX_MATCHES
    marienbad = MARIENBAD.copy()

    while not game_over:
        if not game_over and turn == 0:
            match_number = 21
        if game_mode == 1:
            display_humans(match_number, turn)
        if game_mode == 2:
            if turn % 2 == 0:
                last_pick, turn = ask_player_input(turn)
                if not is_legal_move(match_number, turn, last_pick):
                    game_over = True
                match_number -= last_pick
            else:
                computer_number, turn = computer_5_minus_n(last_pick, turn)
                if not is_legal_move(match_number, turn, computer_number):
                    game_over = True
                match_number -= computer_number
        if game_mode == 4:
            count = 1
            display_marienbad(marienbad, turn, count)
        if game_mode == 3:
            count = 1
            for match in marienbad:
                str = ""
                for num in range(match):
                    str += f" | -- Tas numéro {count}" if num + 1 == len(range(match)) else " | "
                count += 1
                print(f"{str}")
            if turn % 2 == 0:
                last_pick, pile, turn = ask_player_input_marienbad(turn)
                if not is_legal_move_marienbad(marienbad, last_pick, pile, turn):
                    game_over = True
                marienbad[pile] = marienbad[pile] - last_pick
            else:
                computer_pick, pile, turn = compute_marienbad(last_pick, turn)
                if not is_legal_move_marienbad(marienbad, computer_pick, pile, turn):
                    game_over = True
                var = marienbad[pile] - computer_pick
        if game_over:
            break