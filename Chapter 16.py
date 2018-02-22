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

    def pointTest(self, point):
        fallsInRectangle = True

        if point.x > self.width:
            fallsInRectangle = False
        elif point.x == self.width:
            fallsInRectangle = False
        elif point.x < self.corner.x:
            fallsInRectangle = False
        elif point.y > self.height:
            fallsInRectangle = False
        elif point.y == self.height:
            fallsInRectangle = False
        elif point.y < self.corner.y:
            fallsInRectangle = False

        print("Does point fall inside rectangle? ", fallsInRectangle)

# EXERCISE 5 ---------------------------------------------------------------------------------------------------------

    def pointTestTwo(self, point):

        if point.x > self.width:
            self.collision = False
        elif point.x == self.width:
            self.collision = False
        elif point.x < self.corner.x:
            self.collision = False
        elif point.y > self.height:
            self.collision = False
        elif point.y == self.height:
            self.collision = False
        elif point.y < self.corner.y:
            self.collision = False
        else:
            self.collision = True

    def collisionDetection(self, b2):
        b1corners = []
        b2corners = []

        c1 = Point((self.corner.x + self.width), self.corner.y)
        c2 = Point(self.corner.x, (self.corner.y + self.height))
        c3 = Point((self.corner.x + self.width), (self.corner.y + self.height))
        b1corners.append(self.corner)
        b1corners.append(c1)
        b1corners.append(c2)
        b1corners.append(c3)

        c1 = Point((b2.corner.x + b2.width), b2.corner.y)
        c2 = Point(b2.corner.x, (b2.corner.y + b2.height))
        c3 = Point((b2.corner.x + b2.width), (b2.corner.y + b2.height))
        b2corners.append(b2.corner)
        b2corners.append(c1)
        b2corners.append(c2)
        b2corners.append(c3)

        print(b1corners)
        print(b2corners)

        for i in range(4):
            self.pointTestTwo(b2corners[i])
            if self.collision == True:
                print("Collision Detected")
                break
            else:
                print("No Collision")

        for i in range(4):
            b2.pointTestTwo(b1corners[i])
            if b2.collision == True:
                print("Collision Detected")
                break
            else:
                print("No Collision")

b1 = Rectangle(Point(0, 0), 10, 20, False)
b2 = Rectangle(Point(5, 5), 10, 20, False)
print("box: ", b1)
print("box2: ", b2)
#p = Point(3, 4)
#q = Point(10, 0)
#r = Point(-30, 40)
#s = Point(5, 40)

#box.area()
#box.perimeter()
#box.flip()
#print("box: ", box)
#box.pointTest(p)
#box.pointTest(q)
#box.pointTest(r)
#box.pointTest(s)

b1.collisionDetection(b2)
