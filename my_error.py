while True:
    try:
        name = input("Enter your name: ")
        score_1 = int(input("Enter score 1: "))
        score_2 = int(input("Enter score 2: "))
        break
    except ValueError as k:
        print(k, "Invalid input") 
    except ZeroDivisionError as z:
        print(z, "Cant divide by zero")
    else:
        print("Try again")           