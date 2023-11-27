def pomnoz_przez_2_list_comprehension(lista):
    return [liczba * 2 for liczba in lista]


# Przykład użycia funkcji:
lista_liczb = [1, 2, 3, 4, 5]
wynik = pomnoz_przez_2_list_comprehension(lista_liczb)
print(wynik)
