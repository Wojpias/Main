class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Library in {self.city}, {self.street}, {self.zip_code}\n" \
               f"Open hours: {self.open_hours}\nPhone: {self.phone}"


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Employee: {self.first_name} {self.last_name}\n" \
               f"Hire date: {self.hire_date}\nBirth date: {self.birth_date}\n" \
               f"Address: {self.city}, {self.street}, {self.zip_code}\nPhone: {self.phone}"


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Book: {self.author_name} {self.author_surname}\n" \
               f"Published: {self.publication_date}\n" \
               f"Number of pages: {self.number_of_pages}\n" \
               f"Available in library:\n{self.library}"


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        book_list = "\n".join([f" - {book}" for book in self.books])
        return f"Order details:\n" \
               f"Employee: {self.employee}\n" \
               f"Student: {self.student}\n" \
               f"Books:\n{book_list}\n" \
               f"Order date: {self.order_date}"


# Tworzenie instancji klas
library1 = Library("City1", "Street1", "12345", "9 AM - 6 PM", "123-456-789")
library2 = Library("City2", "Street2", "54321", "10 AM - 7 PM", "987-654-321")

employee1 = Employee("John", "Doe", "2022-01-01", "1990-05-15", "City1", "Street1", "12345", "111-222-333")
employee2 = Employee("Alice", "Smith", "2022-02-01", "1985-10-20", "City2", "Street2", "54321", "444-555-666")

book1 = Book(library1, "2021-01-01", "Author1", "Surname1", 200)
book2 = Book(library1, "2022-02-02", "Author2", "Surname2", 250)
book3 = Book(library2, "2023-03-03", "Author3", "Surname3", 300)
book4 = Book(library2, "2024-04-04", "Author4", "Surname4", 150)
book5 = Book(library2, "2025-05-05", "Author5", "Surname5", 180)

order1 = Order(employee1, "Student1", [book1, book3, book5], "2023-01-15")
order2 = Order(employee2, "Student2", [book2, book4], "2023-02-20")

# Wyświetlanie zamówień
print("Order 1:")
print(order1)

print("\nOrder 2:")
print(order2)
