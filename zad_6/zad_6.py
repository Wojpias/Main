def process_lists(list1, list2):
    combined = list(set(list1 + list2))  # Usunięcie duplikatów
    return [x**3 for x in combined]      # Każdy element do potęgi 3

# Wyświetlenie wyniku
print(process_lists([1, 2, 3], [2, 3, 4]))
