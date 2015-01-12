class VectorGraph(object):
    def __init__(self, rindex=100):
        self.rindex = rindex

    def draw(self):
        ''' for move '''
        pass

    def put(self):
        ''' for move '''
        pass        

    def delete(self):
        pass

    def select(self):
        pass

    def unselect(self):
        pass

    def resize(self):
        pass

class Text(VectorGraph):
    def __init__(self, id, font, color, size):
        super(Text, self).__init__()
        self.id = id
        self.font = font
        self.color = color
        self.size = size

class Shape(VectorGraph):
    def __init__(self, id, mathematical_expression, color, size):
        super(Shape, self).__init__()
        # mathematical_expression will be used to draw the picture
        self.mathematical_expression = mathematical_expression

class Circle(Shape):
    pass 
class Line(Shape):
    pass 
class Rectangle(Shape):
    pass 
