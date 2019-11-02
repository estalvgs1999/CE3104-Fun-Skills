# ------------------------------------------------------------
# File: json_generator.py
# Developed by: Esteban Alvarado Vargas
# Project: FunSkills-[Compiler]
# version: 1.0
# last edited by: Esteban Alvarado:: 1/11/19 22.30
#
# Description: This code is responsible for reading and
#              modifying the json file of game settings.
#
# TEC 2019 | CE3104 - Lenguajes, Compiladores e Interpretes
# ------------------------------------------------------------

import json

directory_file = '/home/esteban/Documentos/TEC/2S 2019/Lenguajes-Compiladores-Intérpretes/2. Compiladores/2. Proyecto/CE3104-Fun-Skills/Compiler/'
config_path =  directory_file + 'src/tmp_file/config.json'

# @brief - It is responsible for reading the configuration
#          json and returns it as a dictionary.
def get_json():
    with open(config_path, 'r') as json_file:
        config_json = json.load(json_file)
    return config_json

# @brief - Write the new dictionary with the new configuration in the json
# @param new_json_dict
def save_json(new_setup):
    with open(config_path, 'w') as json_file:
        json.dump(new_setup, json_file)


def set_game1(json_dict,value):
    game = json_dict['game1']
    game['a'] = value

def set_game2(json_dict,value):
    game = json_dict['game2']
    game['b'] = value

def set_game3(json_dict,value):
    game = json_dict['game3']
    game['c'] = value

def set_game4(json_dict,value):
    game = json_dict['game4']
    game['d'] = value
