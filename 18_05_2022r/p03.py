def main():
    x = int(input("Podaj pierwszą liczbę: "))
    y = int(input("Podaj drugą liczbę: "))
    if x < y:
        print(x, "jest mniejsze od", y)
    elif x == y:
        print(x, "jest równe", y)
    else:
        print(x, "jest większe od", y)

main()
