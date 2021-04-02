class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_calc(self, mass_one_sq, height):
        return self._width * self._length * mass_one_sq * height


mass = Road(20, 5000)
mass_road = mass.mass_calc(25, 5)
print(f'Mass of all road: {mass_road:,.2f} kg or {mass_road / 1000:,.2f} tonnes.')
