class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Property: {self.area} sq. meters, {self.rooms} rooms\n" \
               f"Price: ${self.price}\nAddress: {self.address}"


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"House: {self.area} sq. meters, {self.rooms} rooms\n" \
               f"Price: ${self.price}\nAddress: {self.address}\n" \
               f"Plot: {self.plot} sq. meters"


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Flat: {self.area} sq. meters, {self.rooms} rooms\n" \
               f"Price: ${self.price}\nAddress: {self.address}\n" \
               f"Floor: {self.floor}"


# Tworzenie obiektu klasy House
house = House(
    area=150, rooms=5, price=200000, address="123 Main Street", plot=500
)

# Tworzenie obiektu klasy Flat
flat = Flat(area=80, rooms=3, price=120000, address="456 Oak Avenue", floor=2)

# Wyświetlanie informacji o obiektach
print("House:")
print(house)

print("\nFlat:")
print(flat)
