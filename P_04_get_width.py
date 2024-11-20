# Ask user for width and loop until they
# enter a number that is more than zero

error = "Please enter a number that is worth more than zero\n"
while True:

    try:
        # ask tbe user for a number
        width = float(input("width: "))

        # check that the number is more than zero
        if width > 0:
            break
        else:
            print(error)

    except ValueError:
        print(error)
