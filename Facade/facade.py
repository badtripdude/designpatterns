class Buffer:
    def __init__(self, width=30, height=20):
        self.height = height
        self.width = width
        self.buffer = [' '] * (width * height)

    def __getitem__(self, item):
        return self.buffer.__getitem__(item)

    def write(self, text):
        self.buffer += text


class Viewport:
    def __init__(self, buffer=Buffer()):
        self.buffer = buffer
        self.offset = 0

    def get_char_at(self, index):
        return self.buffer[index + self.offset]

    def append(self, text):
        self.buffer.write(text)


class Console:  # Facade
    def __init__(self):
        b = Buffer()
        self.cur_viewport = Viewport(b)
        self.buffers = [b]
        self.cur_viewports = [self.cur_viewport]

    def write(self, text):
        self.cur_viewport.buffer.write(text)

    def get_char_at(self, index):
        return self.cur_viewport.get_char_at(index)


if __name__ == '__main__':
    c = Console()
    c.write('hello')  # High-level api
    ch = c.get_char_at(0)  # using low-level api
