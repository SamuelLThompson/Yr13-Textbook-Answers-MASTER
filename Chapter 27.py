class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)


left = Tree(2)              # Building a tree from the children upwards
right = Tree(3)
tree = Tree(1, left, right)

tree2 = Tree(1, Tree(2), Tree(3)) # Or all in one go - More concise by nesting constructor invocations

expressiontree = Tree("+", Tree(1), Tree("*", Tree(2), Tree(3)))

def print_tree_prefix(tree):            # printing tree in prefix - Traversal method is called:  P R E O R D E R
    if tree is None: return
    print(tree.cargo, end=" ")
    print_tree_prefix(tree.left)
    print_tree_prefix(tree.right)

def print_tree_postfix(tree):           # printing tree in postfix - Traversal method is called:  P O S T O R D E R
    if tree is None: return
    print_tree_postfix(tree.left)
    print_tree_postfix(tree.right)
    print(tree.cargo, end=" ")

def print_tree_infix(tree):             # printing tree in infix - Traversal method is called:  I N O R D E R
    if tree is None: return
    print_tree_infix(tree.left)
    print(tree.cargo, end=" ")
    print_tree_infix(tree.right)

print_tree_prefix(expressiontree)
print()
print_tree_postfix(expressiontree)
print()
print_tree_infix(expressiontree)
print("\n")

expressiontreebad = Tree("+", Tree(1), Tree("*", Tree("a"), Tree(3)))
print_tree_infix(expressiontreebad)

def print_tree_indented(tree, level=0):         # Weird and useless way to print a tree in this context
    if tree is None: return
    print_tree_indented(tree.right, level+1)
    print("  " * level + str(tree.cargo))
    print_tree_indented(tree.left, level+1)

#print_tree_indented(expressiontree)

# EXERCISE 2 -----------------------------------------------------------------------------------------------------------

def create_token_list(expr):
    import re                                       # Import the Regular Expression module
    token_list = re.split("([^0-9])", expr)         # token_list is defined as everything in the expression, split up into unique elements
    return token_list

# ----------------------------------------------------------------------------------------------------------------------

def get_token(token_list, expected):
    if token_list[0] == expected:
        del token_list[0]
        return True
    return False

def get_number(token_list):
    if get_token(token_list, "("):
        x = get_sum(token_list)         # Get the subexpression
        if not get_token(token_list, ")"):
            raise ValueError("Missing close parenthesis")
        return x
    else:
        x = token_list[0]
        if type(x) != type(0): return None
        del token_list[0]
        return Tree(x, None, None)

def get_product(token_list):
    a = get_number(token_list)
    if get_token(token_list, "*"):
        b = get_product(token_list)
        return Tree("*", a, b)
    return a

def get_sum(token_list):
    a = get_product(token_list)
    if get_token(token_list, "+"):
        b = get_sum(token_list)
        return Tree("+", a, b)
    return a


# EXERCISE 4 -----------------------------------------------------------------------------------------------------------

def save_tree_infix(tree):
    if tree is None: return
    save_tree_infix(tree.left)
    f.write(tree.cargo + "\n")
    save_tree_infix(tree.right)

def yes(ques):
    ans = input(ques).lower()
    return ans[0] == "y"

def animal():
    # Start with a singleton
    root = Tree("bird")

    # Loop until the user quits
    while True:
        print()
        if not yes("Are you thinking of an animal? "): break

        # Walk the tree
        tree = root
        while tree.left is not None:
            prompt = tree.cargo + "? "
            if yes(prompt):
                tree = tree.right
            else:
                tree = tree.left

            save_tree_infix(tree)

        # Make a guess
        guess = tree.cargo
        prompt = "Is it a " + guess + "? "
        if yes(prompt):
            print("I rule!")
            continue

        # Get new information
        prompt  = "What is the animal's name? "
        animal  = input(prompt)
        prompt  = "What question would distinguish a {0} from a {1}? "
        question = input(prompt.format(animal, guess))
        save_tree_infix(tree)

        # Add new information to the tree
        tree.cargo = question
        save_tree_infix(tree)
        prompt = "If the animal were {0} the answer would be? "
        if yes(prompt.format(animal)):
            tree.left = Tree(guess)
            tree.right = Tree(animal)
            save_tree_infix(tree)
        else:
            tree.left = Tree(animal)
            tree.right = Tree(guess)


f = open("animaldata.txt", "w")

animal()

f.close()
