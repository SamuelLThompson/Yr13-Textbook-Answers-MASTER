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

    def between(self, time1, time2):
        if (self.to_seconds() >= time1.to_seconds()) and (self.to_seconds() < time2.to_seconds()):
            return True
        if (self.to_seconds() >= time2.to_seconds()) and (self.to_seconds() < time1.to_seconds()):
            return True
        return False

# EXERCISE 4 ----------------------------------------------------------------------------------------------------------

    def increment(self,seconds):
        return MyTime(0,0,self.to_seconds()+seconds)
      
t1 = MyTime(1, 15, 42)
t2 = MyTime(3, 50, 30)
obj = MyTime(2, 20, 53)

# EXERCISE 5 ----------------------------------------------------------------------------------------------------------
t2.increment(1)
t2.inncrement(-900)
t1.increment(5000000)
t2.increment(-5000)

# EXERCISE 1 ----------------------------------------------------------------------------------------------------------

def between(object, time1, time2):
    if (object.to_seconds() >= time1.to_seconds()) and (object.to_seconds() < time2.to_seconds()):
        return True
    if (object.to_seconds() >= time2.to_seconds()) and (object.to_seconds() < time1.to_seconds()):
        return True
    return False

between(obj, t1, t2)

obj.between(t1, t2)
obj.increment(500)
obj.increment(-50000)
