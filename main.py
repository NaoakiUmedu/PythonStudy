# Python Study
# Next--->10
# format code = ctrl + alt + l

while True:
    try:
        x = int(input("Please etnter a number: "))
        break
    except ValueError:
        print("Oops! That was no valid number. Try again...")
