class Rectangle:


    '''Simple polygon.
    Doctest:
    
    >>> p1 = Polygon()
    >>> p1.add_vertice((30, 28))
    >>> p1.add_vertice((30, 33))
    >>> p1.add_vertice((50, 30))
    >>> p1.calc_area()
    50.0
    
    >>> p2 = Polygon()
    >>> p2.add_vertice((20, 30))
    >>> p2.add_vertice((20, 50))
    >>> p2.add_vertice((40, 35))
    >>> p2.add_vertice((60, 50))
    >>> p2.add_vertice((60, 20))
    >>> p2.add_vertice((50, 5))
    >>> p2.add_vertice((20, 30))
    >>> p2.calc_area()
    1050.0
    '''
    def __init__(self):
        '''Class constructor.
        '''
        self._vertices = []

    def add_vertice(self, pt):
        '''Add vertice/point (x, y) the list of vertices of the polygon.
        Keyword arguments:
        pt -- Point in polygon format (x, y)
        
        '''
        self._vertices.append(pt)
        
    def remove_vertice(self, pt):
        '''Remove vertice/point (x, y) the list of vertices of the polygon.
        Keyword arguments:
        pt -- Point in polygon format (x, y)
        
        '''
        try:
            self._vertice.remove(pt)
        except KeyError:
            pass

    def calc_area(self):
        '''Calculate the area of the polygon and returns.
        
        http://mathworld.wolfram.com/PolygonArea.html
        '''
        vertices = self._vertices[:]
        vertices.append(vertices[0])
        
        k = 0
        for i in xrange(len(vertices) - 1):
            k += (vertices[i][1] * vertices[i+1][0]) - \
                (vertices[i][0] * vertices[i+1][1])
        area = k / 2.0
        return area
        
def doctest():
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    doctest()



# class Square:
  