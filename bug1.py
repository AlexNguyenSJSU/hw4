# TODO: there's code missing in one or more lines below
class Base:
    def __init__(self, x, y, size):
        # TODO: will need to fill this in
        self.x = x
        self.y = y
        self.size = size

    def draw(self):
        return ""

class Circle(Base):  # Missing the name of Parent Class
    def __init__(self, x, y, size):  # Missing 'self' keyword in the constructor
        super().__init__(x, y, size)

    def draw(self):
        return f"""
({self.x}, {self.y})
{self.size}
            , - ~ ~ ~ - ,
        , '               ' ,
      ,                       ,
    ,                           ,
   ,                             ,
   ,                             ,
   ,                             ,
    ,                           ,
      ,                       ,
        ,                  , '
          '  - , _ _ _ , '
                   """

class Square(Base):
    def __init__(self, x, y, size):  # Missing 1 parameter x
        super().__init__(x, y, size)

    def draw(self):    # Missing 'self' keyword in draw method
        return f"""
({self.x}, {self.y})
{self.size}
--------------------
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
--------------------
"""

# All of the code below is correct
def draw_any_shape(myShape):
    print(myShape.draw())

def main():
    s = Square(1,2,3)
    draw_any_shape(s)
    c = Circle(2,2,1)
    draw_any_shape(c)

main()
