# ------------------------------------------------------------
# File: Semantic.py
# Developed by: Erick Barrantes, Jessica Espinoza
# Project: FunSkills-Compiler
# version: 1
#
# Last modified 1 /11 /19
# Description:
#
# TEC 2019 | CE3104 - Lenguajes, Compiladores e Interpretes
# -------------------------------------------------------------


def symbolAnalysis(st):
    for value in st.values():
        type = value[0]
        for index in range(1, len(value)):
            result = isinstance(value[index], eval(type))
            print(result)
            print(index)
    return result