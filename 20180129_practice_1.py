class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get(self):
        return self.x, self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def __str__(self):
        return "<{}, {}>".format(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

vec1 = Vector2D(1, 2)
vec2 = Vector2D(1, 2)
vec3 = Vector2D(2, 3)
print(vec1.get_x())
print(vec1.x)

print(vec1)
print(vec1 == vec2)
print(vec1 + vec2 + vec3)