# EXERCISE 1 ----------------------------------------------------------------------------------------------------------

print()
print(" 1 ----------------------------------------------------------------------------")
print()

letter_counts = {}

string = "ThiS is String with Upper and lower case Letters"
for letter in string.lower():
    if letter == " ":
        pass
    else:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1

letter_items = list(letter_counts.items())
letter_items.sort()
for i in range(len(letter_items)):
    print(letter_items[i])

# EXERCISE 2 ----------------------------------------------------------------------------------------------------------

print()
print(" 2 ----------------------------------------------------------------------------")
print()

# a.  35
# b.  4
# c.  True
# d.  Traceback (most recent call last): ... KeyError: 'pears'
# e.  0
# f.  (('apples', 15), ('bananas', 35), ('grapes', 12), ('oranges', 20))
# g.  False

def add_fruit(inventory, fruit, quantity=0):
    test = fruit in inventory

    if test == True:
        inventory[fruit] += quantity
    else:
        inventory[fruit] = quantity

    print(inventory)

new_inventory = {}
add_fruit(new_inventory, "strawberries", 10)
print("strawberries" in new_inventory)

if new_inventory["strawberries"] == 10:
    print("True")
else:
    print("False")

add_fruit(new_inventory, "strawberries", 25)

if new_inventory["strawberries"] == 35:
    print("True")
else:
    print("False")

# EXERCISE 3 ----------------------------------------------------------------------------------------------------------

print()
print(" 3 ----------------------------------------------------------------------------")
print()

counts = {}
longest = ""

f = open("ALICE'S ADVENTURES IN WONDERLAND PLAIN TEXT.txt", "r")
content = f.read()
f.close()

def word_count(str):
    global counts
    words = str.split()

    for word in words:
        if word.isalpha():
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
        else:
            pass

    global count_items
    count_items = list(counts.items())
    count_items.sort()

    alice = open("alice_words.txt", "w")
    alice.write("Word         Count\n")
    alice.write("==================\n")

    #for word in count_items:
        #alice.write(word + " " + str(counts[word]))
        #alice.write('\n')

    alice.close()

    print(count_items)

    global longest

    for word in words:
        if len(word) > len(longest):
            longest = word
        else:
            pass

word_count(content.lower())

print()
print("Alice appears:", str(counts["alice"]), "times in the book")
print()
print(" 4 ----------------------------------------------------------------------------")
print()
print("The longest word in the book is:", longest)
