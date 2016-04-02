#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  2016_python.py
#  
#  Student Dmitry Makarov <vensder@gmail.com>

import math


class Point:
    '''
    Базовый класс "точка", которая имеет две координаты
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Shape:
    '''
    Базовый класс "фигура"
    '''
    def __init__(self, width, color):
        self.width = width
        self.color = color


class Triangle(Shape):
    '''
    Класс "треугольник" (наследник фигуры)
    '''
    def __init__(self, width, color, p1, p2, p3):
        super().__init__(width, color)
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3


class Rectangle(Shape):
    '''
    Класс "прямоугольник" (наследник фигуры)
    '''
    def __init__(self, width, color, p1, p2, p3, p4):
        super().__init__(width, color)
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4


class Circle(Shape):
    '''
    Класс круг (дополнительно считаем площадь, на всякий случай,
    и проверяем, что радиус больше нуля)
    '''
    def __init__(self, width, color, p0, r):
        super().__init__(width, color)
        self.p0 = p0
        self.r = r
        
    def area(self):
        return math.pi * self.r ** 2
    
    @property    
    def r(self):
        return self._r
    
    @r.setter
    def r(self,r):
        if r < 0:
            raise ValueError('Radius should be nonnegative')
        self._r = r


# Let's create the object Triangle
t1 = Triangle(1,'blue', Point(0,0), Point(1,1), Point(1,0))

# Let's create the object Rectangle
r1 = Rectangle(1,'red', Point(0,0), Point(0,1), Point(2,1), Point(2,0))

# Let's create the Circle:
c1 = Circle(2, 'green', Point(1,1), 1)


# Let's print width line, color and coord of our first triangle
print('Triangle:')
print('Width: {}, color: {}'.format(t1.width, t1.color)) 
print('First point coordinate: ({},{})'.format(t1.p1.x, t1.p1.y))
print('Second point coordinate:({},{})'.format(t1.p2.x, t1.p2.y))
print('Next point coordinate:({},{})'.format(t1.p3.x, t1.p3.y))
print('\n')

print('Rectangle:')
# Let's print width line, color and coord of our Rectangle
print('Width: {}, color: {}'.format(r1.width, r1.color)) 
print('First point coordinate: ({},{})'.format(r1.p1.x, r1.p1.y))
print('Second point coordinate:({},{})'.format(r1.p2.x, r1.p2.y))
print('Next point coordinate:({},{})'.format(r1.p3.x, r1.p3.y))
print('Next point coordinate:({},{})'.format(r1.p4.x, r1.p4.y))
print('\n')


print('Circle')
print('Width: {}, color: {}'.format(c1.width, c1.color)) 
print('Center: ({},{}), radius: {}'.format(c1.p0.x, c1.p0.y, c1.r)) 
print('Area of the Circle:', c1.area())

