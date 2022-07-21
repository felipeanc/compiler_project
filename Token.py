from dataclasses import dataclass
from enum import Enum, auto

class TKS(Enum):
    NONE = -1
    PROGRAMA = auto()
    BEGIN = auto()
    END = auto()
    ID = auto()
    TYPE = auto()
    CHAR = auto()
    INT = auto()
    FLOAT = auto()
    NUM = auto()
    FNUM = auto()
    LITERAL = auto()
    ATTR = auto() # := 
    RELOP = auto()
    LE = auto() # <=
    LT = auto() # <
    GE = auto() # >=
    GT = auto() # >
    EQ = auto() # =
    NE = auto() # ~=
    SUM = auto()
    DIF = auto()
    MULT = auto()
    DIV = auto()
    EXP = auto()
    IF = auto()
    THEN = auto()
    ELSE = auto()
    REPEAT = auto()
    WHILE = auto()
    DO = auto()
    LPAR = auto() # LPAR (
    RPAR = auto() # RPAR )
    DD = auto() # double dot :
    #TODO IMPLEMENTAR TOKEN ;

@dataclass(init=True)
class Token:
    """Classe para representação de tokens da nossa linguagem"""
    """Tokens serão representados na forma <Token.name, Token.Attribute>"""
    name: int
    attribute: int
    line: int
    col: int

    def __repr__(self) -> str:
        return f'Token <{TKS(self.name).name}, {TKS(self.attribute).name}> l:{self.line} c:{self.col}'

if __name__ == "__Token__":
  tk1 = Token(TKS.RELOP, TKS.LE, 4, 10)
  print(tk1)