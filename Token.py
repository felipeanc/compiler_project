from dataclasses import dataclass
from enum import Enum, auto

class TKS(Enum):
    PROGRAMA = auto()
    BEGIN = auto()
    END = auto()
    TYPE = auto()
    RELOP = auto()
    IF = auto()
    THEN = auto()
    ELSE = auto()
    LPAR = auto() # LPAR (
    RPAR = auto() # RPAR )
    



#Token<RELOP, RELOP.GT>
class RELOP(Enum):
    LT = 1
    LE = 2
    GT = 3
    GE = 4

@dataclass(init=True)
class Token:
    """Classe para representação de tokens da nossa linguagem"""
    """Tokens serão representados na forma <Token.name, Token.Attribute>"""
    name: int
    attribute: int
    line: int
    col: int

    def __repr__(self) -> str:
        return f'Token <{TKS(self.name).name}, {self.attribute}> l:{self.line} c:{self.col}'

tk1 = Token(TKS.RELOP, 0, 4, 10)
for tks in TKS:
    print(tks.name, tks.value)
print(tk1)