class Bitmap:  # представим, что это огромный класс и мы не хотим его как-то менять -> и нарушать OCP
    def __init__(self, filename):
        self.filename = filename
        print(f'Loading the image from {self.filename}')

    def draw(self):
        print(f'Drawing image {self.filename}')


class LazyBitMap:  # создаем класс, чтобы не редактировать BitMap, тк нарушит OCP
    def __init__(self, filename):
        self.filename = filename
        self._bitmap = None

    def draw(self):
        if not self._bitmap:
            self._bitmap = Bitmap(self.filename)
        self._bitmap.draw()


def draw_image(image):
    print('About to draw image')
    image.draw()
    print('Done drawing image')


if __name__ == '__main__':
    bmp = LazyBitMap('Proxy.png')
    # draw_image(bmp)
