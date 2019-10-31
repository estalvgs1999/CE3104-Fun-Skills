# ------------------------------------------------------------
# File: Operations.py
# Developed by: Erick Barrantes, Jessica Espinoza
# Project: FunSkills-Compiler
# version: 1
#
# Last modified 19 /10 /19
# Description: Grammar for mathematical operations
#
# TEC 2019 | CE3104 - Lenguajes, Compiladores e Interpretes
# -------------------------------------------------------------

from Compiler.src.datastructures.TreeNode import TreeNode

variables = {}

precedence = (
    ('nonassoc', 'LESSTHAN', 'GREATERTHAN'),  # Nonassociative operators
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'NEGATIVE'),  # Unary minus operator
)


# Basic operations
def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]


def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]


def p_term_times(p):
    'term : term MULT factor'
    p[0] = p[1] * p[3]


def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]


def p_expression_negative(p):
    'expression : MINUS term %prec NEGATIVE'
    p[0] = -p[2]


# Basic atomic expressions

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]


def p_term_factor(p):
    'term : factor'
    p[0] = p[1]


def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]


def p_factor_ID(p):
    'factor : ID'
    p[0] = variables[p[1]][-1]


def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]


def p_empty(p):
    "empty :"
    pass


# Error rule for syntax errors
def p_error(p):
    print("Syntax error")
