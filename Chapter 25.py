class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return (self.items == [])


s = Stack()                     # Initialises stack
s.push(54)                      # Appends 54 and the following elements
s.push(45)
s.push("+")                     # You end up with [54, 45, "+"]

def print_stack(s):
    while not s.is_empty():         # While stack is NOT empty
        print(s.pop(), end=" ")     # Pop the last element and print it
    print()                         # Results in the stack getting printed backwards


def eval_postfix(expr):                             # Evaluating postfix expressions
    import re                                       # Import the Regular Expression module
    token_list = re.split("([^0-9])", expr)         # token_list is defined as everything in the expression, split up into unique elements
    print(token_list)                               # Prints token_list to double check everything worked
    stack = Stack()                                 # Initialises stack
    for token in token_list:                        # Uses token as an indexer for the the loop, looping through token_list
        if token == "" or token == " ":             # If the token element is either a space or empty (the "empty" being the space in between digits of a number. eg: ['5', '', '4'] = 54)
            continue                                # Skip this element
        if token == "+":                            # If the token is a plus
            sum = stack.pop() + stack.pop()         # Adds the two first items that it pops
            stack.push(sum)                         # Pushes that result back into the stack
            print(stack.items)                      # Another print statement to help you see what's actually happening to the stack
        elif token == "*":                          # If token is an asterisk
            product = stack.pop() * stack.pop()     # Multiply the two items that it pops
            stack.push(product)                     # Pushes that result into the stack
            print(stack.items)                      # Another print statement to help you see what's actually happening to the stack
        else:                                       # If it can't do anything
            stack.push(int(token))                  # Push the current token into the stack
    return stack.pop()                              # By now there should only be the single result in the stack, pops it out and returns it


print(eval_postfix("56 47 + 2 *"))


# EXERCISE ANSWERS -----------------------------------------------------------------

print(eval_postfix("1 2 + 3 *"))
print(eval_postfix("1 2 3 * +"))
