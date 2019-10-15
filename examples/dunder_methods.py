class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __getitem__(self, i):
        return (self.x, self.y, self.z)[i]

    def __setitem__(self, index, value):
        return setattr(self, ('x', 'y', 'z')[i], value)

    def __str__(self):
        return str((self.x, self.y, self.z))

    def __len__(self):
        return 3

    def __add__(self, other):
         return Vector(*map(sum, zip(self, other)))
