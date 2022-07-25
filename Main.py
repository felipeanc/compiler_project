from Analyzer import Analyzer
from SyntaxAnalyzer import SyntaxAnalyzer

source_code = "source.txt"
teste = "teste.txt"
#analyzer = Analyzer(source_code)
#analyzer.begin()

# while prox_token != None:
#   print(prox_token)
#   prox_token = analyzer.lex()

syntax = SyntaxAnalyzer(source_code)
syntax.procedure_ini()
#analyzer.stop()