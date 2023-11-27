def wyswietl_co_drugi_element(lista):
    for i in range(1, len(lista), 2):
        print(lista[i])


# Przykład użycia funkcji z wykorzystaniem range():
lista_liczb = list(range(1, 11))  # Tworzenie listy liczb od 1 do 10
wyswietl_co_drugi_element(lista_liczb)
