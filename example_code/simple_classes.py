'''A very elementary set of classes and objects for one of the week 3 quiz
    questions.'''


class A:
    def __init__(self, b):
        self.b = b

    def c(self):
        return float(self.b)


d = A
e = A(2)
f = e.c()
g = e.c
