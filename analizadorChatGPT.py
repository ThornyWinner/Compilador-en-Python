import ply.lex as lex
import re
import codecs
import os
import sys
from tabulate import tabulate

reservadas = ['BEGIN', 'END', 'IF', 'THEN', 'WHILE', 'DO', 'CALL', 'CONST',
            'VAR', 'PROCEDURE', 'OUT', 'IN', 'ELSE']

tokens = reservadas + ['ID', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
                        'ODD', 'ASSIGN', 'NE', 'LT', 'LTE', 'GT', 'GTE',
                        'LPARENT', 'RPARENT', 'COMMA', 'SEMICOLON',
                        'DOT', 'UPDATE'
                        ]

t_ignore = ' \t\n'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ODD = r'ODD'
t_ASSIGN = r'='
t_NE = r'<>'
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_COMMA = r','
t_SEMICOLON = r';'
t_DOT = r'\.'
t_UPDATE = r':='

# Definir un diccionario para almacenar los números de token asignados a cada lexema
# Alterando unicamente los operadores y operandos del diccionario funciona pero es mala práctica
lexeme_to_token = {
    'BEGIN': 1,
    'END': 2,
    'IF': 3,
    'THEN': 4,
    'WHILE': 5,
    'DO': 6,
    'CALL': 7,
    'CONST': 8,
    'VAR': 9,
    'PROCEDURE': 10,
    'OUT': 11,
    'IN': 12,
    'ELSE': 13,
    'ID': 14,
    'NUMBER': 15,
    '+': 16,
    '-': 17,
    '*': 18,
    '/': 19,
    'ODD': 20,
    '=': 21,
    '<>': 22,
    '<': 23,
    '<=': 24,
    '>': 25,
    '>=': 26,
    '(': 27,
    ')': 28,
    ',': 29,
    ';': 30,
    '.': 31,
    ':=': 32,
}

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in reservadas:
        t.value = t.value.upper()
        t.type = t.value
    else:
        t.type = 'ID'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    t.type = 'NUMBER'
    return t

def t_newline(t):
    r'\r?\n+'
    t.lexer.lineno += len(t.value)

def t_COMMENT(t):
    r'\#.*'
    pass

def t_error(t):
    print("caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

# Crear el analizador léxico
analizador = lex.lex()

# Selección de archivo de lenguaje de prueba
def buscarFicheros(directorio):
    ficheros = []
    numArchivo = ''
    respuesta = False
    cont = 1

    for base, dirs, files in os.walk(directorio):
        ficheros.append(files)

    for file in files:
        print(str(cont) + ". " + file)
        cont = cont + 1

    while respuesta == False:
        numArchivo = input('\nNumero del test: ')
        for file in files:
            if file == files[int(numArchivo) - 1]:
                respuesta = True
                break

    print("Has escogido \"%s\" \n" % files[int(numArchivo) - 1])

    return files[int(numArchivo) - 1]

directorio = '/Users/hecto/OneDrive/Escritorio/ITS/8vo Semestre/(11-12) Lenguajes y Autómatas II/Compilador en Python/test/'
archivo = buscarFicheros(directorio)
test = directorio + archivo
fp = codecs.open(test, "r", "utf-8")
cadena = fp.read()
fp.close()

analizador = lex.lex()

analizador.input(cadena)

# Lista para almacenar los tokens
token_list = []

# Tokenize
for token in analizador:
    token_value = lexeme_to_token.get(token.value)
    if token_value is None:
        print(f"Token desconocido: {token}")
    token_list.append((token_value, token.lineno, token.lexpos, token.type, token.value))

# Imprimir en forma de tabla
print(tabulate(token_list, headers=["Número de token", "Línea", "Columna", "Tipo de token", "Lexema"]))