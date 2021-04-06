from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, title='Clothes'):
        self.title = title

    @property
    def rate(self):
        param_sum = self.param_cl() + self.param_h()
        return param_sum

    @abstractmethod
    def param_cl(self):
        pass

    @abstractmethod
    def param_h(self):
        pass


class ClothesProp(Clothes):

    def __init__(self, size_c, height, title='Clothes'):
        super().__init__(title)
        self.size_c = size_c
        self.height = height

    @property
    def size_c(self):
        return self.__size_c

    @size_c.setter
    def size_c(self, size_c):
        if size_c > 70:
            self.__size_c = 70
        elif size_c < 5:
            self.__size_c = 5
        else:
            self.__size_c = size_c

    def param_cl(self):
        return round(self.size_c / 6.5 + 0.5, 2)

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height > 170:
            self.__height = 170
        elif height < 5:
            self.__size_c = 5
        else:
            self.__height = height

    def param_h(self):
        return round(2 * self.height + 0.3, 2)


coat_suit = ClothesProp(80, 200)
print('It takes %.2f textile to fabric.' % coat_suit.rate)
