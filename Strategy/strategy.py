from abc import ABC
from enum import Enum, auto


class ListStrategy(ABC):
    def start(self, buffer):
        ...

    def end(self, buffer):
        ...

    def add_list_item(self, buffer, item):
        ...


class OutputFormat(Enum):
    MARKDOWN = auto()
    HTML = auto()


class MarkDownListStrategy(ListStrategy):
    def add_list_item(self, buffer, item):
        buffer.append(f' * {item}\n')


class HtmlListStrategy(ListStrategy):
    def start(self, buffer):
        buffer.append('<ul>\n')

    def end(self, buffer):
        buffer.append('</ul>\n')

    def add_list_item(self, buffer, item):
        buffer.append(f" <li>{item}</li>\n")


class TextProcessor:
    def __init__(self, list_strategy=HtmlListStrategy()):
        self.list_strategy = list_strategy
        self.buffer = []

    def append_list(self, items):
        ls = self.list_strategy
        ls.start(self.buffer)
        _ = [ls.add_list_item(self.buffer, item) for item in items]
        ls.end(self.buffer)

    def set_output_format(self, format):
        if format == OutputFormat.MARKDOWN:
            self.list_strategy = MarkDownListStrategy()
        elif format == OutputFormat.HTML:
            self.list_strategy = HtmlListStrategy()

    def clear(self):
        self.buffer.clear()

    def __str__(self):
        return ''.join(self.buffer)


if __name__ == '__main__':
    items = ['foo', 'bar', 'baz']
    tp = TextProcessor()
    tp.set_output_format(OutputFormat.MARKDOWN)
    tp.append_list(items)
    print(tp)

    tp.clear()
    tp.set_output_format(OutputFormat.HTML)
    tp.append_list(items)
    print(tp)