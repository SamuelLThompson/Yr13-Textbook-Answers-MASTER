import turtle

def koch(t, order, size):
        if order == 0:
            t.forward(size)
        else:
            for angle in [60, -120, 60, 0]:
                koch(t, order-1, size/3)
                t.left(angle)

                
# EXERCISE 1 ------------------------------------------------------------------

def koch_improved():
        for i in range(3):
            koch(t, 2, 400)
            t.right(120)

                
# EXERCISE 2 ------------------------------------------------------------------

def cesaro10(t, order, size, a, b, c, d):
        if order == 0:
            t.forward(size)
        else:
            for angle in [a, b, c, d]:
                cesaro10(t, order-1, size/2,  a, b, c, d)
                t.left(angle)

#angle = int(input("Input an angle for the size of the tear: "))

#b = 180 - angle
#a = 360 - ((180 - angle)/2)
#c = a
#d = 0

#angles = [a, b, c, d]

#order = int(input("Input an order for the fractal: "))

#for i in range(4):
#    cesaro10(t, order, 200, a, b, c, d)
#    t.right(90)


# EXERCISE 3 ------------------------------------------------------------------

def draw_sierpinski(length, depth):
    if depth==0:
        for i in range(0,3):
            t.fd(length)
            t.left(120)

    else:
        draw_sierpinski(length/2,depth-1)
        t.fd(length/2)
        draw_sierpinski(length/2,depth-1)
        t.bk(length/2)
        t.left(60)
        t.fd(length/2)
        t.right(60)
        draw_sierpinski(length/2,depth-1)
        t.left(60)
        t.bk(length/2)
        t.right(60)
        
        
# EXERCISE 4 ------------------------------------------------------------------
        
def colored_sierpinski(length, depth):
    t.pencolor('red')
    draw_sierpinski(length, depth)
    t.fd(length)
    t.pencolor('blue')
    draw_sierpinski(length, depth)
    t.pencolor('red')
    t.bk(length)
    t.left(60)
    t.fd(length)
    t.right(60)
    t.pencolor('yellow')
    draw_sierpinski(length, depth)


window = turtle.Screen()
t = turtle.Turtle()
colored_sierpinski(100,2)
window.exitonclick()


# EXERCISE 5 ------------------------------------------------------------------

def recursive_min(nxs):
    """
      Find the minimum in a recursive structure of lists
      within other lists.
      Precondition: No lists or sublists are empty.
    """
    smallest = None
    first_time = True
    for e in nxs:
        if type(e) == type([]):
            val = recursive_min(e)
        else:
            val = e

        if first_time or val < smallest:
            smallest = val
            first_time = False

    print(smallest)

# recursive_min([[[-13, 7], 90], 2, [1, 100], 8, 6])


# EXERCISE 6 ------------------------------------------------------------------

def count(x, nxs):
    total = 0
    counts = 0
    for e in nxs:
        if type(e) == type([]):
            val = count(x, e)
        else:
            val = e

        if val == x:
            counts += 1
        else:
            total = total + counts

    print(total)

#count(2, [2, 9, [2, 1, 13, 2], 8, [2, 6]])


# EXERCISE 7 <ISSUES> ------------------------------------------------------------------

def flatten(nxs):
    if nxs == []:
        return nxs
    if isinstance(nxs[0], list):                            # The list is passed as an argument to a recursive function to flatten the list
        return flatten(nxs[0]) + flatten(nxs[1:])           # the function is recursively called with the sublists as the parameters until the entire list is flattened.
    return nxs[:1] + flatten(nxs[1:])
nxs = ([["this",["a",["thing"],"a"],"is"],["a","easy"]])    # I tested all of the given nested lists, but I can only work one test at a time.
print("Flattened list is: ",flatten(nxs))                   # The flattened list is passed through the function and printed.

# EXERCISE 8 ------------------------------------------------------------------

def fib(n):
    if n == 1:
        fib_seq = [1]
        print(fib_seq)
    elif n == 2:
        fib_seq = [1, 1]
        print(fib_seq)

    else:
        fib_seq = [1, 1]
        for i in range(2, n):
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        print(fib_seq)

#fib(1)
#fib(2)
#fib(10)


# EXERCISE 9 ------------------------------------------------------------------

import sys

def recursion_depth(number):
    print("{0}, ".format(number), end="")
    recursion_depth(number + 1)

#sys.getrecursionlimit()
#sys.setrecursionlimit(15)
#recursion_depth(10)


# EXERCISE 10 <ISSUES> ------------------------------------------------------------------

import os

def get_dirlist(path):
    """
      Return a sorted list of all entries in path.
      This returns just the names, not the full path to the names.
    """
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist

def print_files(path, prefix = ""):
    """ Print recursive listing of contents of path """
    if prefix == "":  # Detect outermost call, print a heading
        print("Folder listing for", path)
        prefix = "| "

    dirlist = get_dirlist(path)
    for f in dirlist:
        print(prefix+f)                    # Print the line
        fullname = os.path.join(path, f)   # Turn name into full pathname
        if os.path.isdir(fullname):        # If a directory, recurse.
            print_files(fullname, prefix + "| ")

def print_full_files(path):
    dirlist = get_dirlist(path)
    for f in dirlist:
        fullname = os.path.join(path,f)
        if os.path.isdir(fullname):
            print_full_files(fullname)
        else:
            print(os.path.join(path,f))


# EXERCISE 11 <ISSUES> ------------------------------------------------------------------
