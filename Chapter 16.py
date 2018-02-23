class Point: # Adding a comment
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at the origin """
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def DistanceFromOrigin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def halfway(self, target):
        """ Return the halfway point between myself and the target """
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)

class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h, c):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h
        self.collision = c

    def __str__(self):
        return  "({0}, {1}, {2})".format(self.corner, self.width, self.height)

    def grow(self, delta_width, delta_height):
        """ Grow (or shrink) this object by the deltas """
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        """ Move this object by the deltas """
        self.corner.x += dx
        self.corner.y += dy

# EXERCISE 1 ---------------------------------------------------------------------------------------------------------

    def area(self):
        areaOfRectangle = self.width*self.height
        print("Area of rectangle = ", areaOfRectangle)

# EXERCISE 2 ---------------------------------------------------------------------------------------------------------

    def perimeter(self):
        perimeterOfRectangle = 2*self.width + 2*self.height
        print("Perimeter of rectangle = ", perimeterOfRectangle)

# EXERCISE 3 ---------------------------------------------------------------------------------------------------------

    def flip(self):
        temp = self.height
        self.height = self.width
        self.width = temp

# EXERCISE 4 ---------------------------------------------------------------------------------------------------------

    def point_check(self,posn):
        x=(posn.x)
        y=(posn.y)
        if x > (self.corner.x)  or x < (self.corner.x):
            print('Outside')
        else:
            print('Inside')
        if y > (self.corner.y)  or y < (self.corner.y):
            print('Outside')
        else:
            print('Inside')
# Exercise 5 ----------------------------------------------------
    def colission_check(self,posn):
        x=(posn.x)
        y=(posn.y)
        if x > (self.corner.x + self.width) and y > (self.corner.y + self.height):
            print('no collision')
        if x < (self.corner.x + self.width) and y < (self.corner.y + self.height):
            print('no collision')

    def same_coordinates(self, p1, p2):
        return (p1.x == p2.x) and (p1.y == p2.y)

    def __str__(self):
        return  "({0}, {1}, {2})".format(self.corner, self.width, self.height)

box = Rectangle(Point(0, 0), 100, 200)
bomb = Rectangle(Point(100, 80), 5, 10)
print("box: ", box)
print("bomb: ", bomb)
box.grow(25,-10)
bomb.grow(-10,10)
print("box: ", box)
print("bomb: ", bomb)
box.move(25,-10)
bomb.move(-10,10)
print("box: ", box)
print("bomb: ", bomb)
second_box=copy.copy(box)
second_bomb=copy.deepcopy(bomb)
box.area()
box.point_check(Point(0,10))
