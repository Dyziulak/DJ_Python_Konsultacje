def main():
    n = int(input("Podaj liczbę naturalną: "))
    # Stosując instrukcję for, oblicz w zmiennej 'suma' sumę liczb od 1 do n
    suma = 0
    for liczba in range(1, n + 1):
        print(suma)
        suma += liczba
    print("Suma wynosi:", suma)

main()
