class MyTime:
   # ...

    def __init__(self, hrs=0, mins=0, secs=0):
       """ Create a new MyTime object initialized to hrs, mins, secs.
           The values of mins and secs may be outside the range 0-59,
           but the resulting MyTime object will be normalized.
       """

       # Calculate total seconds to represent
       totalsecs = hrs*3600 + mins*60 + secs
       self.hours = totalsecs // 3600        # Split in h, m, s
       leftoversecs = totalsecs % 3600
       self.minutes = leftoversecs // 60
       self.seconds = leftoversecs % 60

    def to_seconds(self):
        """ Return the number of seconds represented by this instance """
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def after(self, time2):
        """ Return True if I am strictly greater than time2 """
        return self.to_seconds() > time2.to_seconds()

    def __add__(self, other):
        return MyTime(0, 0, self.to_seconds() + other.to_seconds())

# EXERCISE 3 ----------------------------------------------------------------------------------------------------------

    def __gt__(self, time2):
        return self.to_seconds() > time2.to_seconds()

# EXERCISE 2 (With the amendments possible with EXERCISE 3)------------------------------------------------------------

    def between(self, t1, t2):
        is_between = False
        if self > t1 == False:
            is_between = False
        else:
            if self > t2 == True:
                is_between = False
            elif self.to_seconds() == t2.to_seconds():
                is_between == False
            else:
                is_between = True

        print(is_between)

# EXERCISE 4 ----------------------------------------------------------------------------------------------------------

    def increment(self, seconds):
        totalsecs = self.to_seconds()
        totalsecs += seconds
        if totalsecs > 0:
            self.hours = totalsecs // 3600
            leftoversecs = totalsecs % 3600
            self.minutes = leftoversecs // 60
            self.seconds = leftoversecs % 60
        else:
            print("The resulting time is negative, modern science hasn't quite figured out what that even is yet so I'm afraid have to reject it.")

t1 = MyTime(1, 15, 42)
t2 = MyTime(3, 50, 30)
obj = MyTime(2, 20, 53)

# EXERCISE 1 ----------------------------------------------------------------------------------------------------------

def between(obj, t1, t2):
    is_between = False
    if t1.after(obj) == True:
        is_between = False
    else:
        if obj.after(t2) == True:
            is_between = False
        elif obj.to_seconds() == t2.to_seconds():
            is_between == False
        else:
            is_between = True

    print(is_between)

between(obj, t1, t2)

obj.between(t1, t2)
obj.increment(500)
obj.increment(-50000)
