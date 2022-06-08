def main():
    s = input("Podaj liczbę naturalną: ")
    print(type(s))
    n = int(s)
    # Stosując instrukcję for, wypisz kolejne liczby od 1 do n
    for i in range(1, n + 1):
        print(i)

main()
