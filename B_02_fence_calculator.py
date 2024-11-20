# Ask user for width and loop until
# they enter a number that is more than zero
def num_check(question):
    error = "Please enter a number that is more than zero\n"
    while True:

        try:
            # Ask the user for a number
            response = float(input(question))

            # check that the number is more than zero
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main routine goes here

keep_going = ""
while keep_going == "":
    # Get width and height
    width = num_check("Width: ")
    length = num_check("Length: ")
    cost = num_check("Cost: ")

    # Calculate area / perimeter
    perimeter = 2 * (width + length)
    price = perimeter * cost

    # Display output
    print()
    print(f"Perimeter: {perimeter} units")
    print(f"Price: ${price:.2f}")

    # Ask user
    keep_going = input("Press enter to keep going or any key to quit. ")
    print()

print("Thank you for using the perimeter / area calculator")