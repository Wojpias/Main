def pomnoz_przez_2_for(lista):
    wynik = []
    for liczba in lista:
        wynik.append(liczba * 2)
    return wynik

# Przykład użycia funkcji:
lista_liczb = [1, 2, 3, 4, 5]
wynik = pomnoz_przez_2_for(lista_liczb)
print(wynik)