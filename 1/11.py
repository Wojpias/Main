def wyswietl_imiona(imiona):
    if len(imiona) != 5:
        print("Podaj imiona kolego.")
    else:
        for imie in imiona:
            print(imie)

# Przykład użycia funkcji:
lista_imion = ["Anna", "Jan", "Katarzyna", "Tomasz", "Maria"]
wyswietl_imiona(lista_imion)