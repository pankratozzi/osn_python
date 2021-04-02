class Stationery:
    def __init__(self, title='Default'):
        self.title = title

    def draw(self):
        print('Enable drawing!')

    def draw_caps(self, symbol=''):
        try:
            self.drawing(symbol)
        except AttributeError:
            print('Use pen, pencil or handle')


class Pen(Stationery):
    def __init__(self, title='Pen'):
        Stationery.__init__(self, title)

    def draw(self):
        print('Drawing with %s.' % self.title)

    def drawing(self, symbol):
        print(('%s' % symbol) * 15, end='')
        self.draw()


class Pencil(Stationery):
    def __init__(self, title='Pencil'):
        super().__init__(title)

    def draw(self):
        print('Drawing with %s.' % self.title)

    def drawing(self, symbol):
        print(('%s' % symbol) * 15, end='')
        self.draw()


class Handle(Stationery):
    def __init__(self, title='Handle'):
        super().__init__(title)

    def draw(self):
        print('Drawing with %s.' % self.title)

    def drawing(self, symbol):
        print(('%s' % symbol) * 15, end='')
        self.draw()


class Eraser(Stationery):
    def __init__(self, title='Eraser'):
        Stationery.__init__(self, title)

    def __call__(self, func):
        def wrapper(*objects):
            print('Start erasing!')
            func(*objects)
            print('All clear!')

        return wrapper


@Eraser()
def erase(*objs):
    for x in objs[:-1]:
        print('%s erased by %s' % (x.title, objs[-1].title))


stat = Stationery()
pen = Pen('Blue Pen')
pencil = Pencil('Black Pencil')
handle = Handle('Red Handle')
eraser = Eraser()

for obj in (stat, pen, pencil, handle):
    obj.draw()

erase(pen, pencil, handle, eraser)
pen.draw_caps('=')
pencil.draw_caps('-')
handle.draw_caps('#')
erase(pen, pencil, handle, eraser)
