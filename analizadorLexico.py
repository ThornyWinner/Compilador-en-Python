import ply.lex as lex
import re
import codecs
import os
import sys
from tabulate import tabulate

reservadas = ['BEGIN', 'END', 'IF', 'THEN', 'WHILE', 'DO', 'CALL', 'CONST',
            'VAR', 'PROCEDURE', 'OUT', 'IN', 'ELSE', 'ODD']

tokens = reservadas + ['ID', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 
                        'ASSIGN', 'NE', 'LT', 'LTE', 'GT', 'GTE',
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
    'PLUS': 16,
    'MINUS': 17,
    'TIMES': 18,
    'DIVIDE': 19,
    'ODD': 20,
    'ASSIGN': 21,
    'NE': 22,
    'LT': 23,
    'LTE': 24,
    'GT': 25,
    'GTE': 26,
    'LPARENT': 27,
    'RPARENT': 28,
    'COMMA': 29,
    'SEMICOLON': 30,
    'DOT': 31,
    'UPDATE': 32,
}

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in reservadas:
        t.value = t.value.upper()
        t.type = t.value
    else:
        t.type = 'ID'
        t.value = t.value  # Mantiene el valor del identificador
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
#def buscarFicheros(directorio):
#    ficheros = []
#    numArchivo = ''
#    respuesta = False
#    cont = 1

#    for base, dirs, files in os.walk(directorio):
#        ficheros.append(files)

#    for file in files:
#        print(str(cont) + ". " + file)
#        cont = cont + 1

#    while respuesta == False:
#        numArchivo = input('\nNumero del test: ')
#        for file in files:
#            if file == files[int(numArchivo) - 1]:
#                respuesta = True
#                break

#    print("Has escogido \"%s\" \n" % files[int(numArchivo) - 1])

#    return files[int(numArchivo) - 1]

#directorio = '/Users/hecto/OneDrive/Escritorio/ITS/8vo Semestre/(11-12) Lenguajes y Autómatas II/Compilador en Python/test/'
#archivo = buscarFicheros(directorio)
#test = directorio + archivo
#fp = codecs.open(test, "r", "utf-8")
#cadena = fp.read()
#fp.close()

analizador = lex.lex()

#analizador.input(cadena)

#token_list = []

# Tokenize
#for token in analizador:
#    token_type = token.type
#    token_value = lexeme_to_token.get(token_type, None)
#    if token_value is None:
#        print(f"Token desconocido: {token}\n")
#    else:
#        token_list.append((token_value, token.lineno, token.lexpos, token.type, token.value))

# Imprimir en forma de tabla
#print(tabulate(token_list, headers=["Número de token", "Línea", "Columna", "Tipo de token", "Lexema"]))