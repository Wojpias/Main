class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        average_marks = sum(self.marks) / len(self.marks)
        return average_marks > 50


# Tworzenie dwóch przykładowych obiektów klasy Student


student1 = Student("John", [60, 75, 80])


student2 = Student("Alice", [40, 30, 20])


# Wywołanie metody is_passed dla obiektów i wyświetlenie wyników
result1 = student1.is_passed()
result2 = student2.is_passed()

print(f"{student1.name} - Passed: {result1}")
print(f"{student2.name} - Passed: {result2}")
