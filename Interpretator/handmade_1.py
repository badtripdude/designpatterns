# Лексический анализ
from enum import Enum, auto


class Token:
    class Type(Enum):
        INTEGER = auto()
        PLUS = auto()
        MINUS = auto()
        LPAREN = auto()
        RPAREN = auto()

    def __init__(self, type, text):
        self.text = text
        self.type = type

    def __str__(self):
        return f'`{self.text}`'


def lex(input_):
    result = []
    i = 0
    while i < len(input_):
        if input_[i] == '+':
            result.append(Token(Token.Type.PLUS, '+'))
        elif input_[i] == '-':
            result.append(Token(Token.Type.MINUS, '-'))
        elif input_[i] == '(':
            result.append(Token(Token.Type.LPAREN, '('))
        elif input_[i] == ')':
            result.append(Token(Token.Type.RPAREN, ')'))
        else:
            digits = [input_[i]]
            for j in range(i + 1, len(input_)):
                if input_[j].isdigit():
                    digits.append(input_[j])
                    i += 1
                else:
                    result.append(Token(Token.Type.INTEGER,
                                        ''.join(digits)))
                    break
        i += 1
    return result


def calc(input_):
    tokens = lex(input_)
    print(' '.join(map(str, tokens)))


if __name__ == '__main__':
    calc('(12+4)-(12+1)')
