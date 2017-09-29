def change_return():
    while True:
        change_request = input("How much change do you need? ")
        change = int(change_request[-2:])
        if change in range(25, 100):
            q = change // 25
            change %= 25
            d = change // 10
            change %= 10
            n = change // 5
            change %= 5
            p = change // 1
            print("Your change comes out to:")
            print("{} quarters".format(str(q)))
            print("{} dimes".format(str(d)))
            print("{} nickels".format(str(n)))
            print("{} pennies".format(str(p)))

        elif change in range(10, 25):
            d = change // 10
            change %= 10
            n = change // 5
            change %= 5
            p = change // 1
            print("Your change comes out to:")
            print("{} dimes".format(str(d)))
            print("{} nickels".format(str(n)))
            print("{} pennies".format(str(p)))

        elif change in range(5, 10):
            n = change // 5
            change %= 5
            p = change // 1
            print("Your change comes out to:")
            print("{} nickels".format(str(n)))
            print("{} pennies".format(str(p)))

        elif change in range(1, 6):
            p = change // 1
            print("Your change comes out to:")
            print("{} pennies".format(str(p)))


change_return()
