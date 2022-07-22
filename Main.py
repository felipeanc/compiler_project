from Analyzer import Analyzer
from Procedures import *

source_code = "source.txt"
analyzer = Analyzer(source_code)
analyzer.begin()

prox_token = analyzer.lex()
print(prox_token)
while prox_token != None:
  prox_token = analyzer.lex()
  #print(prox_token)
#procedure_ini()

analyzer.stop()