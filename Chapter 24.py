class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next  = next

    def __str__(self):
        return str(self.cargo)

    def print_backward(self):
        if self.next is not None:
            tail = self.next
            tail.print_backward()
        print(self.cargo, end=" ")

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3

# FOLLOWING print_list FUNCTION IS THE MODIFIED ONE AS PER THE EXERCISE SPECIFICATIONS ---------------------------------

def print_list(node):
    print("[", end="")
    while node is not None:
        if node.next:
            print(node, end=", ")
        else:
            print(node, end="")
        node = node.next
    print("]")
    print()

# ----------------------------------------------------------------------------------------------------------------------

print_list(node1)

def print_backward_badly(list):
    if list is None: return
    head = list
    tail = list.next
    print_backward(tail)
    print(head, end=" ")

def print_backward(list):               # His print_backward was actually bullshit and didn't print it like a proper list like he said it did.
    if list is None: return             # REMEMBER THAT THE LIST IS STILL FORWARDS, SO IN THIS CASE (3) IS STILL THE FINAL ELEMENTS IN THE LIST
    print_backward(list.next)           # The following lines are ones that I added to make sure It actually DID print like a list (understanding how the (end="") parameter works is essential)
    if list.next is not None:           # If the next element is NOT None THEN check
        if list.next.next == None:      # If the one after the next is none (If it's the second to last element in this case)
            print(list, end=", ")       # Is so, print element with a comma and space
        else:                           # If not, (aka if this element is the FIRST one in the list)
            print(list, end="")         # Print with no space or comma, print it last
    else:                               # If this element IS the last one and refers to None
        print(list, end=", ")           # Print with a comma (SINCE THIS WILL BE THE FIRST ELEMENT PRINTED - TECHNICALLY... A Diagram would help with this, try dry running it yourself)
                                        # You know, I think this might ONLY work with lists that have three elements but it serves its purpose for this exercise
#print_backward(node1)

def remove_second(list):
    if list is None:
        return
    first = list
    second = list.next
    # Make the first node refer to the third
    first.next = second.next
    # Separate the second node from the rest of the list
    second.next = None
    return second

def print_backward_nicely(list):
    print("[", end="")
    print_backward(list)
    print("]")

print_backward_nicely(node1)


class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None

    def print_backward(self):
            print("[", end=" ")
            if self.head is not None:
                self.head.print_backward()

    def add_first(self, cargo):
        node = Node(cargo)
        node.next = self.head
        self.head = node
        self.length += 1
