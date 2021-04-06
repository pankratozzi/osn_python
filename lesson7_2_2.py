from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, title):
        self.title = title

    @abstractmethod
    def count_col(self):
        pass


class Suit(Clothes):

    def __init__(self, title, height):
        Clothes.__init__(self, title)
        self.height = height

    def count_col(self):
        return round((2 * self.height + 0.3), 2)

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height > 170:
            self.__height = 170
        elif height < 5:
            self.__height = 5
        else:
            self.__height = height


class Coat(Clothes):

    def __init__(self, title, size_s):
        Clothes.__init__(self, title)
        self.size_s = size_s

    def count_col(self):
        return round((self.size_s / 6.5 + 0.5), 2)

    @property
    def size_s(self):
        return self.__size_s

    @size_s.setter
    def size_s(self, size_s):
        if size_s > 70:
            self.__size_s = 70
        elif size_s < 5:
            self.__size_s = 5
        else:
            self.__size_s = size_s


class Counter(Clothes):

    def __init__(self, title):
        Clothes.__init__(self, title)

    def __call__(self, func):
        def wrapper(*args):
            print('Start calculating...')
            sum_gen = func(*args)
            print('Textile to fabric: %.2f' % sum(sum_gen))

        return wrapper

    def count_col(self):
        pass


@Counter(title='Counter')
def count_col(*objects):
    for x in objects:
        yield x.count_col()


class CounterAlt(Coat, Suit):

    def __init__(self, title):
        Clothes.__init__(self, title)
        self.outer = []
        self.sum_cl = 0

    def count_col_alt(self, height, size_s):
        self.height = height
        self.size_s = size_s
        return Coat.count_col(self) + Suit.count_col(self)

    def count_col(self, *args):
        for x in args:
            self.sum_cl += x.count_col()
            self.outer.append(x.title)
        return self.sum_cl, self.outer


coat = Coat('Coat', 80)
suit = Suit('Suit', 200)
count_col(coat, suit)
cnt_alt = CounterAlt('SumCounter')
sum_cl, outer = cnt_alt.count_col(coat, suit)
print('Textile for %s and %s: %.2f' % (outer[0], outer[1], sum_cl))
print('Textile for Suit and Coat: %.2f' % cnt_alt.count_col_alt(200, 80))
