try:

    terms = int(input("Enter the number of terms you want the sequence to have: "))

    current1, current2 = 1, 1
    print("\n")

    if terms > 2:

        print("1\n1")

        for _ in range(terms - 2):

            x = current1 + current2
            print(x)

            current1 = current2
            current2 = x

    else:

        for _ in range(terms):

            print(1)

except ValueError:

    print("\nInvalid value.")