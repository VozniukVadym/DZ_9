class Paralelogram():
    def __init__(self, width, length):
        self.width=width
        self.length=length
    def get_area(self):
        self.s=self.width*self.length
        return self.s
ploga=Paralelogram(10,2)
class Square(Paralelogram):
    def get_area(self):
        self.s=self.width**2
        return self.s
print(ploga.get_area())
print(Square.get_area(ploga))