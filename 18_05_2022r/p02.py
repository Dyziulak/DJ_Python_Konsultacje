def main():
    x = input("Podaj pierwszą liczbę: ")
    x = int(x)
    y = input("Podaj drugą liczbę: ")
    y = int(y)
    if x < y:
        print(x, "jest mniejsze od", y)
    elif x == y:
        print(x, "jest równe", y)
    else:
        print(x, "jest większe od", y)

main()
