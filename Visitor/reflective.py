class Expression:
    ...

class DoubleExpression(Expression):
    def __init__(self, value):
        self.value = value


class AdditionExpression(Expression):
    def __init__(self, left, right):
        self.right = right
        self.left = left


class ExpressionPrinter:
    @staticmethod
    def print(e, buffer: list):
        if isinstance(e, DoubleExpression):
            buffer.append(str(e.value))
        elif isinstance(e, AdditionExpression):
            buffer.append('(')
            ExpressionPrinter.print(e.left, buffer)
            buffer.append('+')
            ExpressionPrinter.print(e.right, buffer)
            buffer.append(')')

Expression.print = lambda e,b: ExpressionPrinter.print(e, b)
if __name__ == '__main__':
    # 1 + (2+3)
    e = AdditionExpression(
        DoubleExpression(1),
        AdditionExpression(
            DoubleExpression(2),
            DoubleExpression(3)
        )
    )
    buffer = []
    e.print(buffer)
    # ExpressionPrinter.print(e, buffer)
    print(''.join(buffer), '=', )
