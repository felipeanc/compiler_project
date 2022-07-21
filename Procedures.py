from Token import TKS

prox_token = TKS.NONE

def procedure_ini():
  if prox_token == TKS.PROGRAMA:
    prox_token = lex(w)
    if prox_token == TKS.ID:
      prox_token = lex(w)
      procedure_bloco()
    else:
      print("Error: id expected")
  else:
    print("Error: 'programa' expected")

def procedure_bloco():
  if prox_token == TKS.BEGIN:
    prox_token = lex(w)
    procedure_variaveis()
    procedure_cmd()
    if prox_token == TKS.END:
      prox_token = lex(w)
    else:
      print("Error: 'end' expected")
  else:
    print("Error: 'begin' expected")

def procedure_variaveis():
  if prox_token == TKS.TYPE:
    prox_token = lex(w)
    if prox_token == TKS.DD:
      prox_token = lex(w)
      if prox_token == TKS.ID:
        prox_token = lex(w)
        procedure_variaveis1Linha()
        if prox_token = lex(w):
          #TODO TOKEN PONTO E VIRGULA, RESTO DO PROCEDIMENTO
      else:
        print("Error: id expected")
    else:
      print("Error: id expected")