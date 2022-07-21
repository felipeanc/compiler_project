from Token import TKS
from Analyzer import lex

prox_token = TKS.NONE

def procedure_ini():
  if prox_token == TKS.PROGRAMA:
    prox_token = lex()
    if prox_token == TKS.ID:
      prox_token = lex()
      procedure_bloco()
    else:
      print("Error: id expected")
  else:
    print("Error: 'programa' expected")

def procedure_bloco():
  if prox_token == TKS.BEGIN:
    prox_token = lex()
    procedure_variaveis()
    procedure_cmd()
    if prox_token == TKS.END:
      prox_token = lex()
    else:
      print("Error: 'end' expected")
  else:
    print("Error: 'begin' expected")

def procedure_variaveis():
  if prox_token == TKS.TYPE:
    prox_token = lex()
    if prox_token == TKS.DD:
      prox_token = lex()
      if prox_token == TKS.ID:
        prox_token = lex()
        procedure_variaveis1Linha()
        if prox_token != TKS.CD:
          print("Error: ; expected")
      else:
        print("Error: id expected")
    else:
      print("Error: id expected")

def procedure_variaveis1Linha():
  while prox_token == ',':
    prox_token = lex()
    if prox_token == TKS.ID:
      prox_token = lex()
      procedure_variaveis1Linha()
    else:
      print("Error: id expected")

def procedure_cmd():
  if prox_token == TKS.IF:
    prox_token = lex()
    if prox_token == TKS.LPAR:
      procedure_expr()
      if prox_token == TKS.RPAR:
        prox_token = lex()
        if prox_token == TKS.THEN:
          procedure_bloco()
          procedure_cmd1Linha()
        else:
          print("Error: 'then' expected")
      else:
          print("Error: ) expected")
    else:
          print("Error: ( expected")
  elif prox_token == TKS.ID:
    prox_token = lex()
    if prox_token == TKS.EQ:
      procedure_expr()
      prox_token = lex()
      if prox_token != TKS.CD:
          print("Error: ; expected")
    else:
      print("Error: '=' expected")
  elif prox_token == TKS.WHILE:
    prox_token = lex()
    if prox_token == TKS.LPAR:
      procedure_expr()
      if prox_token == TKS.RPAR:
        prox_token = lex()
        if prox_token == TKS.DO:
          procedure_bloco()
        else:
          print("Error: 'do' expected")
      else:
          print("Error: ) expected")
    else:
          print("Error: ( expected")
  elif prox_token == TKS.REPEAT:
    procedure_bloco()
    if prox_token == TKS.WHILE:
      prox_token = lex() 
      if prox_token == TKS.LPAR:
        procedure_expr() 
        if prox_token != TKS.RPAR:
          print("Error: ) expected")
      else:
        print("Error: ( expected")
    else:
      print("Error: 'while' expected")


def procedure_expr():
  procedure_termo()
  procedure_expr2Linha()

def procedure_termo():
  procedure_fator()
  procedure_termo2Linha()

def procedure_fator():
  if prox_token == TKS.NUM:
    procedure_fator1Linha()
  else:
    print("Error: num expected")

def procedure_cmd1Linha():
  while prox_token == TKS.ELSE:
    prox_token = lex()
    procedure_bloco()

def procedure_expr1Linha():
  if prox_token == TKS.RELOP:
    prox_token = lex()
    procedure_expr()
  elif prox_token == TKS.SUM:
    prox_token = lex()
    procedure_expr()
  elif prox_token == TKS.DIF:
    prox_token = lex()
    procedure_expr()
  else:
    print("Error: relop | + | - expected")

def procedure_termo1Linha():
  if prox_token == TKS.MULT:
    prox_token = lex()
    procedure_fator()
  elif prox_token == TKS.DIV:
    prox_token = lex()
    procedure_fator()
  elif prox_token == TKS.EXP:
    prox_token = lex()
    procedure_fator()
  else:
    print("Error: * | / | ^ expected")

def procedure_termo2Linha():
  while prox_token in [TKS.MULT, TKS.DIV, TKS.EXP]:
    procedure_termo1Linha()

def procedure_expr2Linha():
  while prox_token in [TKS.RELOP, TKS.SUM, TKS.DIF]:
    procedure_expr1Linha()

def procedure_fator1Linha():
  procedure_termo2Linha()
  while prox_token in [TKS.RELOP, TKS.SUM, TKS.DIF]:
    procedure_fator1Linha()