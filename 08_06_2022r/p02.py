def main():
    n = int(input("Podaj liczbę naturalną: "))
    # Stosując instrukcję for, oblicz w zmiennej 'iloczyn' iloczyn liczb od 1 do n
    iloczyn = 1
    for liczba in range(1, n + 1):
        print(iloczyn)
        iloczyn *= liczba
    print("Iloczyn wynosi:", iloczyn)

main()
