first=int(input())
second=int(input())


print("""1 for +                                         2 for -
3 for *                                         4 for /
5 for **                                        6 for %
7 for //                                          """)
while True:
    operator=int(input())
    if operator == 1:
        print(f"{first} + {second} = ",first+second)
    elif operator == 2:
        print(f"{first} - {second} = ",first-second)
    elif operator == 3:
        print(f"{first} * {second} = ",first*second)
    elif operator == 4:
        print(f"{first} / {second} = ",first/second)
    elif operator == 5:
        print(f"{first} ** {second} = ",first**second)
    elif operator == 6:
        print(f"{first} % {second} = ",first%second)
    elif operator == 7:
        print(f"{first} // {second} = ",first//second)
    else:
        raise ValueError("Invalid input")
