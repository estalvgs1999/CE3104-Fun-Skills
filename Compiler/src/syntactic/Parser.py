# ------------------------------------------------------------
# File: Parser.py
# Developed by: Erick Barrantes, Jessica Espinoza
# Project: FunSkills-Compiler
# version: 1
#
# Last modified 19 /10 /19
# Description: Grammar for main structures
#
# TEC 2019 | CE3104 - Lenguajes, Compiladores e Interpretes
# -------------------------------------------------------------

import ply.yacc as yacc

from Compiler.src.syntactic.Statements import *

# Get the token map from the lexer.
from Compiler.src.lexer.Lexer import tokens


astRoot = TreeNode("structure")
start = 'structure'


# Main structure for program
def p_structure(p):
    '''structure : COMMENT\
    BEGIN\
    MAIN LBRACE\
    statements\
    RBRACE\
    GAME LBRACE\
    statements\
    RBRACE\
    GAME LBRACE\
    statements\
    RBRACE\
    GAME LBRACE\
    statements\
    RBRACE\
    GAME LBRACE\
    statements\
    RBRACE\
    END SEMICOLON'''

    mainNode = TreeNode(p[3])
    mainNode.add_child(p[5])

    g1Node = TreeNode(p[7])
    g1Node.add_child(p[9])

    g2Node = TreeNode(p[11])
    g2Node.add_child(p[13])

    g3Node = TreeNode(p[15])
    g3Node.add_child(p[17])

    g4Node = TreeNode(p[19])
    g4Node.add_child(p[21])

    astRoot.add_children([mainNode, g1Node, g2Node, g3Node, g4Node])


# Build the parser
def parse(lex):
    parser = yacc.yacc()
    result = parser.parse(lexer=lex)
    print(result)
    print(variables)