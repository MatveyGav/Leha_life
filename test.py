class Sparrow:
    c = 0
    def __init__(self, c):
        self.a = 5
        self.b = 6
        self.c = c

    def fly(self):
        self.a -= 1

q = [Sparrow(), Sparrow(), Sparrow()]
jack = Sparrow(12)

q.fly()
q.fly()
print(q.a)