print("\nWellcome to Py-Calculator!")

is_running = True
while is_running:
    try:
        expression = input("\nEnter expression [Q to escape]: ")
        if expression == "Q":
            is_running = False
        else:
            expression = eval(expression)
            print("Result:", expression)
    except:
        print("That's not an option, ha!")

print("\nThanks for using Py-Calculator!")