from SymbolTable import *
from Token import *

class Analyzer:
  source_file:str

  def __init__(self, path:str) -> None:
    self.source_file = path

  def reader(self):
      with open(self.source_file) as f:
          while True:
              char = f.read(1)
              if len(char) == 1:
                  yield char
              else:
                  return

  #loop do analisador
  def begin(self):
    self.source_code = open(self.source_file, "r")
    self.digitos = [str(x) for x in range(10)] # [0-9]
    self.letra_ = [chr(x) for x in range(65, 91)] # [A-Z]
    self.letra_ += [chr(x) for x in range(97, 123)] # [a-z]
    self.letra_ += '_'

  def stop(self):
    self.source_code.close()

  def lex(self):
    state = 0
    c = self.source_code.read(1)
    pos = 0
    line = 0
    col = 0
    lookahead = False #flag pra identificar se fez lookahead ou não

    st = SymbolTable()
    while(True):
        s = str(state)
        if not lookahead and not s.startswith('f'): 
          try:
            c = self.source_code.read(1) #se não fez lookahead, e não está em um estado final, lê next char
          except StopIteration:
            print("End of file")
            break
        else:
          lookahead = False
        col += 1
        if c == '\n':
          line += 1
          col = 0

        if col > 100:
          break
        
        match s:
          case '0': #estado 0 inicial
            ini_col = col
            if c == '<':
              state = 1
            elif c == '>':
              state = 2
            elif c == '=':
              state = 'f1'
            elif c == '~':
              state = 3
            elif c == ':':
              state = 4
            elif c in self.digitos:
              state = 5
            elif c == 'b':
              state = 7
            elif c == 'c':
              state = 8
            elif c == 'd':
              state = 9
            elif c == 'e':
              state = 10
            elif c == 'f':
              state = 11
            elif c == 'i':
              state = 12
            elif c == 'p':
              state = 13
            elif c == 'r':
              state - 14
            elif c == 't':
              state = 15
            elif c == 'w':
              state = 16
            elif c in self.letra_:
              state = 6
            elif c == '(':
              state = 'f4'
            elif c == ')':
              state = 'f5'
            elif c == '+':
              state = 'f6'
            elif c == '-':
              state = 'f7'
            elif c == '*':
              state = 'f8'
            elif c == '/':
              state = 'f9'
            elif c == '^':
              state = 'f10'
            elif c == '[':
              state = 17
            elif c in ['\t', '\r', '\n', ' ', ',']:
              state = 18
            elif c == '\'':
              state = 19
            elif c == ';':
              state = 'f35'

          ########################### RELOP ###########################
          case '1':
            if c == '=': 
              state = 'f11'
            elif c != '=':
              state = 'f12'
          
          case '2':
            if c == '=': 
              state = 'f13'
            elif c != '=': #fez lookahead
              state = 'f14'
          
          case '3':
            if c == '=': 
              state = 0
              token = Token(TKS.RELOP, TKS.NE, line, ini_col)
              print(token)
            else:
              print(f'Error l:{line} c:{ini_col}')
              break
          ########################### RELOP ###########################

          ########################### RELOP ###########################


          ########################### ATTR ###########################
          case '4':
            if c == '=': 
              state = 'f16'
            else:
              state = 'f34'
              break
          ########################### ATTR ###########################

          ######################### NUMERO #########################
          case '5':
            if c in self.digitos:
              state = 5
            elif c == '.':
              state = 61
            elif not c in self.digitos and c != '.' and c != 'E':
              state = 'f2'
          
          case '61':
            if c in self.digitos:
              state = 61
            elif c == 'E':
              state = 62
            elif not c in self.digitos and c != 'E':
              state = 'f32'
          
          case '62':
            if c in self.digitos or c in ['+', '-']:
              state = 63
          
          case '63':
            if c in self.digitos:
              state = 63
            else:
              state = 'f33'
          ######################### NUMERO #########################

          ######################### ID #########################
          case '6':
            if c in self.digitos or c in self.letra_:
              state = 21
            elif not c in self.digitos and not c in self.letra_:
              state = 'f3'
          
          case '21':
            if c in self.digitos or c in self.letra_:
              state = 21
            else:
              state = 'f3'
          ######################### ID #########################

          ######################### BEGIN #########################
          case '7':
            if c == 'e':
              state = 22
            elif c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f3'

          case '22':
            if c == 'g':
              state = 23
            elif c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f3'
          
          case '23':
            if c == 'i':
              state = 24
            elif c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f3'
          
          case '24':
            if c == 'n':
              state = 25
            elif c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f3'
          
          case '25':
            if c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f20'
          ######################### BEGIN #########################

          ######################### CHAR #########################
          case '8':
            if c == 'h':
              state = 26
            elif c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f3'

          case '26':
            if c == 'a':
              state = 27
            elif c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f3'
          
          case '27':
            if c == 'r':
              state = 28
            elif c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f3'
          
          case '28':
            if c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f21'
          ######################### CHAR #########################

          ######################### DO #########################
          case '9':
            if c == 'o':
              state = 29
            elif c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f3'
          
          case '29':
            if c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f22'
          ######################### DO #########################

          #END/ELSE CASE
          case '10':
            if c == 'n':
              state = 30
            elif c == 'l':
              state = 32
            elif c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f3'

          ######################### END #########################
          case '30':
            if c == 'd':
              state = 31
            elif c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f3'
          
          case '31':
            if c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f23'
          ######################### END #########################

          ######################### ELSE #########################
          case '32':
            if c == 's':
              state = 33
            elif c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f3'
          
          case '33':
            if c == 'e':
              state = 34
            elif c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f3'
          
          case '34':
            if c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f24'
          ######################### ELSE #########################

          ######################### FLOAT #########################
          case '11':
            if c == 'l':
              state = 35
            elif c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f3'
          
          case '35':
            if c == 'o':
              state = 36
            elif c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f3'

          case '36':
            if c == 'a':
              state = 37
            elif c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f3'
          
          case '37':
            if c == 't':
              state = 38
            elif c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f3'
          
          case '38':
            if c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f25'
          ######################### FLOAT #########################

          #IF/INT CASE
          case '12':
            if c == 'n':
              state = 59
            elif c == 'f':
              state = 39
            elif c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f3'

          ######################### INT #########################
          case '59':
            if c == 't':
              state = 60
            elif c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f3'
          
          case '60':
            if c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f31'
          ######################### INT #########################

          ######################### IF #########################      
          case '39':
            if c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f26'
          ######################### IF #########################

          ######################### PROGRAMA #########################      
          case '13':
            if c == 'r':
              state = 40
            elif c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f3'
          
          case '40':
            if c == 'o':
              state = 41
            elif c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f3'

          case '41':
            if c == 'g':
              state = 42
            elif c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f3'
          
          case '42':
            if c == 'r':
              state = 43
            elif c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f3'
          
          case '43':
            if c == 'a':
              state = 44
            elif c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f3'

          case '44':
            if c == 'm':
              state = 45
            elif c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f3'

          case '45':
            if c == 'a':
              state = 46
            elif c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f3'

          case '46':
            if c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f27'
          ######################### PROGRAMA #########################

          ######################### REPEAT #########################      
          case '14':
            if c == 'e':
              state = 47
            elif c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f3'
          
          case '47':
            if c == 'p':
              state = 48
            elif c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f3'

          case '48':
            if c == 'e':
              state = 49
            elif c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f3'
          
          case '49':
            if c == 'a':
              state = 50
            elif c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f3'

          case '50':
            if c == 't':
              state = 51
            elif c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f3'

          case '51':
            if c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f28'
          ######################### REPEAT #########################

          ######################### THEN #########################      
          case '15':
            if c == 'h':
              state = 52
            elif c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f3'
          
          case '52':
            if c == 'e':
              state = 53
            elif c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f3'

          case '53':
            if c == 'n':
              state = 54
            elif c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f3'

          case '54':
            if c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f29'
          ######################### THEN #########################
          
          ######################### WHILE #########################      
          case '16':
            if c == 'h':
              state = 55
            elif c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f3'
          
          case '55':
            if c == 'i':
              state = 56
            elif c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f3'

          case '56':
            if c == 'l':
              state = 57
            elif c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f3'

          case '57':
            if c == 'e':
              state = 58
            elif c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f3'

          case '58':
            if c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f30'
          ######################### WHILE #########################

          ######################### COMMENT #########################      
          case '17':
            if c != ']':
              state = 17
            else:
              state = 'f17'
          ######################### COMMENT #########################

          ######################### WS #########################      
          case '18':
            if c in ['\n', '\t', '\r', ' ', ',']:
              state = 18
            else:
              state = 'f18'

          case '54':
            if c in self.digitos or c in self.letra_:
              state = 6
            else:
              state = 'f29'
          ######################### WS #########################

          ######################### LITERAL #########################      
          case '19':
            if c != '\'':
              state = 20
            else:
              print(f'Error, empty literal is not accepted l:{line} c:{ini_col}')
              break

          case '20':
            if c == '\'':
              state = 'f19'
          ######################### LITERAL #########################

          ########################### FINAL STATES ###########################
          case 'f1':
            state = 0
            token = Token(TKS.RELOP, TKS.EQ, line, ini_col)
            print(token)
            return TKS.EQ
          
          #todo setInt(), tabela de simbolos
          case 'f2':
            state = 0
            token = Token(TKS.NUM, TKS.NONE, line, ini_col)
            st.insert(token)
            print(token)
            return TKS.NUM
          
          #todo setID(), tabela de simbolos
          case 'f3':
            state = 0
            lookahead = True
            self.source_code.seek(-1, 1)
            token = Token(TKS.ID, TKS.NONE, line, ini_col)
            st.insert(token)
            print(token)
            return TKS.ID

          case 'f4':
            state = 0
            token = Token(TKS.LPAR, TKS.NONE, line, ini_col)
            print(token)
            return TKS.LPAR

          case 'f5':
            state = 0
            token = Token(TKS.RPAR, TKS.NONE, line, ini_col)
            print(token)
            return TKS.RPAR

          case 'f6':
            state = 0
            token = Token(TKS.SUM, TKS.NONE, line, ini_col)
            print(token)
            return TKS.SUM

          case 'f7':
            state = 0
            token = Token(TKS.DIF, TKS.NONE, line, ini_col)
            print(token)
            return TKS.DIF

          case 'f8':
            state = 0
            token = Token(TKS.MULT, TKS.NONE, line, ini_col)
            print(token)
            return TKS.MULT
          
          case 'f9':
            state = 0
            token = Token(TKS.DIV, TKS.NONE, line, ini_col)
            print(token)
            return TKS.DIV

          case 'f10':
            state = 0
            token = Token(TKS.EXP, TKS.NONE, line, ini_col)
            print(token)
            return TKS.EXP

          case 'f11':
            state = 0
            token = Token(TKS.RELOP, TKS.LE, line, ini_col)
            print(token)
            return TKS.RELOP            
          
          case 'f12':
            state = 0
            lookahead = True
            self.source_code.seek(-1, 1)
            token = Token(TKS.RELOP, TKS.LT, line, ini_col)
            print(token)
            return TKS.RELOP 
          
          case 'f13':
            state = 0
            token = Token(TKS.RELOP, TKS.GE, line, ini_col)
            print(token)
            return TKS.RELOP 
          
          case 'f14':
            state = 0
            lookahead = True
            self.source_code.seek(-1, 1)
            token = Token(TKS.RELOP, TKS.GT, line, ini_col)
            print(token)
            return TKS.RELOP 

          case 'f15':
            state = 0
            token = Token(TKS.RELOP, TKS.NE, line, ini_col)
            print(token)
            return TKS.RELOP 
          
          case 'f16':
            state = 0
            token = Token(TKS.ATTR, TKS.NONE, line, ini_col)
            print(token)
            return TKS.ATTR

          case 'f17':
            state = 0

          case 'f18':
            state = 0
            lookahead = True
            self.source_code.seek(-1, 1)
          
          case 'f19':
            state = 0
            lookahead = True
            self.source_code.seek(-1, 1)
            token = Token(TKS.LITERAL, TKS.NONE, line, ini_col)
            print(token)
            return TKS.LITERAL 

          case 'f20':
            state = 0
            lookahead = True
            self.source_code.seek(-1, 1)
            token = Token(TKS.BEGIN, TKS.NONE, line, ini_col)
            print(token)
            return TKS.BEGIN
          
          case 'f21':
            state = 0
            lookahead = True
            self.source_code.seek(-1, 1)
            token = Token(TKS.TYPE, TKS.CHAR, line, ini_col)
            print(token)
            return TKS.TYPE
          
          case 'f22':
            state = 0
            lookahead = True
            self.source_code.seek(-1, 1)
            token = Token(TKS.DO, TKS.NONE, line, ini_col)
            print(token)
            return TKS.DO
          
          case 'f23':
            state = 0
            lookahead = True
            self.source_code.seek(-1, 1)
            token = Token(TKS.END, TKS.NONE, line, ini_col)
            print(token)
            return TKS.END

          case 'f24':
            state = 0
            lookahead = True
            self.source_code.seek(-1, 1)
            token = Token(TKS.ELSE, TKS.NONE, line, ini_col)
            print(token)
            return TKS.ELSE

          case 'f25':
            state = 0
            lookahead = True
            self.source_code.seek(-1, 1)
            token = Token(TKS.TYPE, TKS.FLOAT, line, ini_col)
            print(token)
            return TKS.TYPE

          case 'f26':
            state = 0
            lookahead = True
            self.source_code.seek(-1, 1)
            token = Token(TKS.IF, TKS.NONE, line, ini_col)
            print(token)
            return TKS.IF

          case 'f27':
            state = 0
            lookahead = True
            self.source_code.seek(-1, 1)
            token = Token(TKS.PROGRAMA, TKS.NONE, line, ini_col)
            print(token)
            return TKS.PROGRAMA

          case 'f28':
            state = 0
            lookahead = True
            self.source_code.seek(-1, 1)
            token = Token(TKS.REPEAT, TKS.NONE, line, ini_col)
            print(token)
            return TKS.REPEAT

          case 'f29':
            state = 0
            lookahead = True
            self.source_code.seek(-1, 1)
            token = Token(TKS.THEN, TKS.NONE, line, ini_col)
            print(token)
            return TKS.THEN

          case 'f30':
            state = 0
            lookahead = True
            self.source_code.seek(-1, 1)
            token = Token(TKS.WHILE, TKS.NONE, line, ini_col)
            print(token)
            return TKS.WHILE

          case 'f31':
            state = 0
            lookahead = True
            self.source_code.seek(-1, 1)
            token = Token(TKS.TYPE, TKS.INT, line, ini_col)
            print(token)
            return TKS.TYPE
          
          #todo setFrac(), tabela de simbolos
          case 'f32':
            state = 0
            token = Token(TKS.FNUM, TKS.NONE, line, ini_col)
            st.insert(token)
            print(token)
            return TKS.FNUM
          
          #todo setExp(), tabela de simbolos
          case 'f33':
            state = 0
            token = Token(TKS.FNUM, TKS.NONE, line, ini_col)
            st.insert(token)
            print(token)
            return TKS.TYPE
          
          case 'f34':
            state = 0
            lookahead = True
            self.source_code.seek(-1, 1)
            token = Token(TKS.DD, TKS.NONE, line, ini_col)
            st.insert(token)
            print(token)
            return TKS.DD
          
          case 'f35':
            state = 0
            token = Token(TKS.CD, TKS.NONE, line, ini_col)
            st.insert(token)
            print(token)
            return TKS.CD