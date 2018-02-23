class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0, m=0, c=0):
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

    # EXERCISE 2 -----------------------------------------------------------------------------------------------------

    def ReflectX(self):
        """ Returns the Reflection of the point in the X Axis """
        ry = (0 - self.y)
        print("Reflection of point in the X Axis is: ", Point(self.x, ry))

    # EXERCISE 3 -----------------------------------------------------------------------------------------------------

    def SlopeFromOrigin(self):
        """ Returns the slope (Gradient) of the point with respect to the origin """
        slope = (self.y/self.x)
        print("The gradient of this point with respect to the origin is:", slope)

    # EXERCISE 4 -----------------------------------------------------------------------------------------------------

    def get_line_to(self, point_2):
        slope = (point_2.y - self.y) / (point_2.x - self.x)
        y_intercept = slope * (-self.x) + self.y
        if y_intercept >= 0:
            print("The Equation of this line is: ", "y =", slope,"x +", y_intercept)
        elif y_intercept < 0:
            print("The Equation of this line is: ", "y =", slope,"x ", y_intercept)
        
        tup = (slope, y_intercept)
        return tup

# EXERCISE 1 ---------------------------------------------------------------------------------------------------------

def distance(p, q):
    dx = q.x - p.x
    dy = q.y - p.y
    dsquared = dx*dx + dy*dy
    result = dsquared**0.5
    print("Distance between points = ", result)

def CircleCenterCalculator(a, b, c, d):         # THIS ONE IS REALLLLLY BROKEN. NONE OF THE VARIABLES MATCH AT ALL
    a.EquationOfLine(b)
    c.EquationOfLine(d)

    m1 = (0-(1/a.m))
    c1 = (m1*(0-a.x)) + a.y
    m2 = (0-(1/c.m))
    c2 = (m2*(0-c.x)) + c.y

    h = ((c2-c1)/(m2-m1))
    k = m1(h)-c1

    print("Centre of given circle = ", "(", h, ",", k, ")")


p = Point(2, 1)
q = Point(4, 2)

a = Point(5, 9)
b = Point(9, 5)
c = Point(5, 1)
d = Point(1, 5)

distance(p, q)
p.ReflectX()
p.SlopeFromOrigin()
p.EquationOfLine(q)
# CircleCenterCalculator(a, b, c, d)

# EXERCISE 6 ---------------------------------------------------------------------------------------------------------

MessageNumbers = ["0122163249", "0122161219", "0122154123", "0122453754", "0122334234", "0122123419"]
MessageTimes = ["Now", "Now", "Now", "Now", "Now", "Now"]
MessageText = ["Generic Text1", "Generic Text2", "Generic Text3", "Generic Text4", "Generic Text5", "Generic Text6"]

class SMS_Store:
    """ SMS_Store class acts as an inbox, a record of messages """

    def __init__(self):
        """ Create a new point at the origin """
        self.MyInbox = []

    def addNewArrival(self, from_number, time_arrived, text_of_SMS):
        Message = ("False", from_number, time_arrived, text_of_SMS)         # Makes new SMS tuple, inserts it after other messages
        self.MyInbox.append(Message)                                        # in the store. When creating this message, its has_been_viewed status is set False.

    def messageCount(self):
        print("You have: ", len(self.MyInbox), "Messages in your inbox")    # Returns the number of sms messages in my_inbox

    def getUnreadIndexes(self):
        UnreadSMS = 0
        for i in range(len(self.MyInbox)):                                  # Returns list of indexes of all not-yet-viewed SMS messages
            if self.MyInbox[i][0] == "False":
                UnreadSMS += 1
            else:
                pass
        print("You have: ", UnreadSMS, " new messages")

    def getMessage(self):
        SMSIndex = int(input("Enter index of desired message: "))           # Return (from_number, time_arrived, text_of_sms) for message[i]
        if SMSIndex < len(self.MyInbox):
            Message = ("Has Been Viewed",) + self.MyInbox[SMSIndex][1:]                 # Also change its state to "has been viewed".
            self.MyInbox.append(Message)
            print(Message)                                                  # If there is no message at position i, return None
        else:
            print("There is no message at that index")

    def delete(self):                                                       # Delete the message at index i
        SMSIndex = int(input("Enter index of desired message: "))
        del self.MyInbox[SMSIndex]
        print("Message Deleted")

    def clear(self):                                                        # Delete all messages from inbox
        self.MyInbox = []
        print("Inbox Cleared")

# TESTING CODE -------------------------------------------------------------------------------------------------------

Inbox = SMS_Store()

MessageCount = 0
for j in range(6):
    Inbox.addNewArrival(MessageNumbers[MessageCount], MessageTimes[MessageCount], MessageText[MessageCount])
    MessageCount += 1

Inbox.getUnreadIndexes()
Inbox.messageCount()
Inbox.delete()
Inbox.messageCount()
Inbox.getMessage()
Inbox.getUnreadIndexes()
Inbox.clear()
