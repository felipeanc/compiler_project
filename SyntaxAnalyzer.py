from Analyzer import Analyzer
from Token import TKS

class SyntaxAnalyzer(Analyzer):

  prox_token = None

  def procedure_ini(self):
    print("[syntax] Procedure ini")
    self.prox_token = super(SyntaxAnalyzer, self).lex()
    if self.prox_token == TKS.PROGRAMA:
      self.prox_token = super(SyntaxAnalyzer, self).lex()
      if self.prox_token == TKS.ID:
        self.prox_token = super(SyntaxAnalyzer, self).lex()
        self.procedure_bloco()
      else:
        print("Error: 'begin' expected")
    else:
      print("Error: 'programa' expected")

    if self.prox_token == TKS.EOF:
      print("Entrada aceita")
    else:
      print("Entrada rejeitada")

  def procedure_bloco(self):
    print("[syntax] Procedure bloco")
    if self.prox_token == TKS.BEGIN:
      self.prox_token = super(SyntaxAnalyzer, self).lex()
      self.procedure_variaveis()
      self.procedure_cmd()
      if self.prox_token == TKS.END:
        self.prox_token = super(SyntaxAnalyzer, self).lex()
      else:
        print("Error: 'end' expected")
    else:
      print("Error: 'begin' expected")

  def procedure_variaveis(self):
    print("[syntax] Procedure variaveis")
    if self.prox_token == TKS.TYPE:
      self.prox_token = super(SyntaxAnalyzer, self).lex()
      if self.prox_token == TKS.DD:
        self.prox_token = super(SyntaxAnalyzer, self).lex()
        if self.prox_token == TKS.ID:
          self.prox_token = super(SyntaxAnalyzer, self).lex()
          self.procedure_variaveis1Linha()
          if self.prox_token != TKS.CD:
            print("Error: ; expected")
          else:
            self.prox_token = super(SyntaxAnalyzer, self).lex()
            self.procedure_variaveis()
        else:
          print("Error: id expected")
      else:
        print("Error: ':' expected")

  def procedure_variaveis1Linha(self):
    print("[syntax] Procedure variaveis1Linha")
    while self.prox_token == TKS.COMMA:
      self.prox_token = super(SyntaxAnalyzer, self).lex()
      if self.prox_token == TKS.ID:
        self.prox_token = super(SyntaxAnalyzer, self).lex()
        self.procedure_variaveis1Linha()
      else:
        print("Error: id expected")

  def procedure_cmd(self):
    print("[syntax] Procedure cmd")
    if self.prox_token == TKS.IF:
      self.prox_token = super(SyntaxAnalyzer, self).lex()
      if self.prox_token == TKS.LPAR:
        self.procedure_expr()
        print("VOLTEI DO EXPR DEPOIS DO IF ", self.prox_token)
        self.prox_token = super(SyntaxAnalyzer, self).lex()
        if self.prox_token == TKS.RPAR:
          self.prox_token = super(SyntaxAnalyzer, self).lex()
          if self.prox_token == TKS.THEN:
            self.prox_token = super(SyntaxAnalyzer, self).lex()
            self.procedure_bloco()
            self.procedure_cmd1Linha()
            self.procedure_cmd()
          else:
            print("Error: 'then' expected")
        else:
            print("Error: ) expected")
      else:
            print("Error: ( expected")

    elif self.prox_token == TKS.ID:
      self.prox_token = super(SyntaxAnalyzer, self).lex()
      if self.prox_token == TKS.ATTR:
        print("ANTES DO EXPR ", self.prox_token)
        self.procedure_expr()
        print("VOLTEI DO EXPR ", self.prox_token)
        if self.prox_token == TKS.CD:
          self.prox_token = super(SyntaxAnalyzer, self).lex()
          self.procedure_cmd()
        else:
          self.prox_token = super(SyntaxAnalyzer, self).lex()
          print("DPS DO EXPR ", self.prox_token)
          if self.prox_token != TKS.CD:
              print("Error: ; expected")
          else:
            self.prox_token = super(SyntaxAnalyzer, self).lex()
            self.procedure_cmd()
      else:
        print("Error: ':=' expected")

    elif self.prox_token == TKS.WHILE:
      self.prox_token = super(SyntaxAnalyzer, self).lex()
      if self.prox_token == TKS.LPAR:
        self.procedure_expr()
        print("VOLTEI DO EXPR DENTRO DO WHILE", self.prox_token)
        self.prox_token = super(SyntaxAnalyzer, self).lex()
        if self.prox_token == TKS.RPAR:
          self.prox_token = super(SyntaxAnalyzer, self).lex()
          if self.prox_token == TKS.DO:
            self.prox_token = super(SyntaxAnalyzer, self).lex()
            self.procedure_bloco()
            self.procedure_cmd()
          else:
            print("Error: 'do' expected")
        else:
            print("Error: ) expected")
      else:
            print("Error: ( expected")

    elif self.prox_token == TKS.REPEAT:
      self.prox_token = super(SyntaxAnalyzer, self).lex() 
      self.procedure_bloco()
      if self.prox_token == TKS.WHILE:
        self.prox_token = super(SyntaxAnalyzer, self).lex() 
        if self.prox_token == TKS.LPAR:
          print("TESTE ANTES DO EXPR EM REPEAT, ", self.prox_token)
          self.procedure_expr()
          self.prox_token = super(SyntaxAnalyzer, self).lex() 
          if self.prox_token != TKS.RPAR:
            print("Error: ) expected")
          else:
            self.prox_token = super(SyntaxAnalyzer, self).lex() 
            self.procedure_cmd()
        else:
          print("Error: ( expected")
      else:
        print("Error: 'while' expected")


  def procedure_expr(self):
    print("[syntax] Procedure expr")
    self.procedure_termo()
    self.procedure_expr2Linha()

  def procedure_termo(self):
    print("[syntax] Procedure termo")
    self.procedure_fator()
    self.procedure_termo2Linha()

  #CHAMA PROX TOKEN
  def procedure_fator(self):
    print("[syntax] Procedure fator")
    self.prox_token = super(SyntaxAnalyzer, self).lex()
    if self.prox_token == TKS.NUM or self.prox_token == TKS.ID:
      self.prox_token = super(SyntaxAnalyzer, self).lex()
      self.procedure_fator1Linha()
    else:
      print("Error: num expected")

  #CHAMA PROX TOKEN
  def procedure_cmd1Linha(self):
    print("[syntax] Procedure cmd1Linha")
    while self.prox_token == TKS.ELSE:
      self.prox_token = super(SyntaxAnalyzer, self).lex()
      self.procedure_bloco()

  #CHAMA PROX TOKEN
  def procedure_expr1Linha(self):
    print("[syntax] Procedure expr1Linha")
    if self.prox_token == TKS.RELOP:
      self.prox_token = super(SyntaxAnalyzer, self).lex()
      self.procedure_expr()
    elif self.prox_token == TKS.SUM:
      self.prox_token = super(SyntaxAnalyzer, self).lex()
      self.procedure_expr()
    elif self.prox_token == TKS.DIF:
      self.prox_token = super(SyntaxAnalyzer, self).lex()
      self.procedure_expr()
    else:
      print("Error: relop | + | - expected")

  #CHAMA PROX TOKEN
  def procedure_termo1Linha(self):
    print("[syntax] Procedure termo1Linha")
    if self.prox_token == TKS.MULT:
      self.prox_token = super(SyntaxAnalyzer, self).lex()
      self.procedure_fator()
    elif self.prox_token == TKS.DIV:
      self.prox_token = super(SyntaxAnalyzer, self).lex()
      self.procedure_fator()
    elif self.prox_token == TKS.EXP:
      self.prox_token = super(SyntaxAnalyzer, self).lex()
      self.procedure_fator()
    else:
      print("Error: * | / | ^ expected")


  #NÃO CHAMA PROX TOKEN
  def procedure_termo2Linha(self):
    print("[syntax] Procedure termo2Linha")
    while self.prox_token in [TKS.MULT, TKS.DIV, TKS.EXP]:
      self.prox_token = super(SyntaxAnalyzer, self).lex()
      self.procedure_termo1Linha()

  #NÃO CHAMA PROX TOKEN
  def procedure_expr2Linha(self):
    print("[syntax] Procedure expr2Linha")
    while self.prox_token in [TKS.RELOP, TKS.SUM, TKS.DIF]:
      self.prox_token = super(SyntaxAnalyzer, self).lex()
      self.procedure_expr1Linha()

  #CHAMA PROX TOKEN
  def procedure_fator1Linha(self):
    print("[syntax] Procedure fator1Linha")
    self.procedure_termo2Linha()
    while self.prox_token in [TKS.RELOP, TKS.SUM, TKS.DIF]:
      self.prox_token = super(SyntaxAnalyzer, self).lex()
      self.procedure_fator1Linha()