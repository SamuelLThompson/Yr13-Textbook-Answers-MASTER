def readposint(x):
    # checking if x has an assigned value (if the user input anything at all)
    if (not x) == True:
        print("No input detected.")
    else:
        # checking if it is an integer
        try:
            y = int(x)
            # checking if it is positive
            if int(x) > 0:
                print(x, "is positive")
            else:
                print(x, "is not positive.")
        except:
            print("'", x, "' is not an integer.")

x = input("Enter a positive integer: ")
readposint(x)

x = input("Enter a positive integer: ")
readposint(x)

x = input("Enter a positive integer: ")
readposint(x)

x = input("Enter a positive integer: ")
readposint(x)
