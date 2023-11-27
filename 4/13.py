def wyswietl_parzyste_elementy(lista):
    for liczba in lista:
        if liczba % 2 == 0:
            print(liczba)


# Przykład użycia funkcji z wykorzystaniem range():
lista_liczb = list(range(1, 11))  # Tworzenie listy liczb od 1 do 10
wyswietl_parzyste_elementy(lista_liczb)
