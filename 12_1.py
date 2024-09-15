#1
class Product:
    def __init__(self, name, store, price):
        self.__name = name
        self.__store = store
        self.__price = price

    def __str__(self):
        return f'Product: {self.__name}, Store: {self.__store}, Price: {self.__price} RUB'

    @property
    def name(self):
        return self.__name

    @property
    def store(self):
        return self.__store

    @property
    def price(self):
        return self.__price


class Storage:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    def get_product_by_index(self, index):
        try:
            return str(self.__products[index])
        except IndexError:
            return 'Product not found.'

    def get_product_by_name(self, name):
        for product in self.__products:
            if product.name == name:
                return str(product)
        return 'Product not found.'

    def sort_by_name(self):
        self.__products.sort(key=lambda product: product.name)

    def sort_by_store(self):
        self.__products.sort(key=lambda product: product.store)

    def sort_by_price(self):
        self.__products.sort(key=lambda product: product.price)

    def __add__(self, other):
        if isinstance(other, Storage):
            total_price = sum(product.price for product in self.__products) + \
                          sum(product.price for product in other.__products)
            return total_price
        return NotImplemented

    def get_all_products(self):
        return self.__products.copy()

product1 = Product('Milk', 'Store 1', 30)
product2 = Product('Bread', 'Store 2', 10)
product3 = Product('Cheese', 'Store 3', 50)

storage = Storage()
storage.add_product(product1)
storage.add_product(product2)
storage.add_product(product3)

print(storage.get_product_by_index(0))
print(storage.get_product_by_index(1))
print(storage.get_product_by_index(2))

print(storage.get_product_by_name('Milk'))
print(storage.get_product_by_name('Bread'))
print(storage.get_product_by_name('Cheese'))

storage.sort_by_name()
for product in storage._Storage__products:
    print(product)

storage_2 = Storage()
storage_2.add_product(Product('Apples', 'Store 4', 40))
total_price = storage + storage_2
print(f'Total price: {total_price} RUB')



#2
class BeeElephant:
    def __init__(self, bee_part, elephant_part):
        self.bee_part = bee_part
        self.elephant_part = elephant_part

    def Fly(self):
       return self.bee_part >= self.elephant_part

    def Trampet(self):
       if self.elephant_part >= self.bee_part:
           return 'tu-tu-doo-doo'
       else:
           return 'wzzzz'

    def Eat(self, meal, value):
        if meal not in ['nectar', 'grass']:
            raise ValueError ('Meal must be either nectar or grass.')

        if meal == 'nectar':
            self.bee_part += value
            self.elephant_part -= value
        elif meal == 'grass':
            self.elephant_part += value
            self.bee_part -= value

        if self.bee_part > 100:
            self.bee_part = 100
        elif self.bee_part < 0:
            self.bee_part = 0

        if self.elephant_part > 100:
            self.elephant_part = 100
        elif self.elephant_part < 0:
            self.elephant_part = 0


animal = BeeElephant(50, 40)
animal.Eat('grass', 6)
animal.Eat('nectar', 60)

print(animal.Fly())
print(animal.Trampet())
print(animal.bee_part)
print(animal.elephant_part)




#3
class Bus:
    def __init__(self, max_seats, max_speed):
        self.speed = 0
        self.max_seats = max_seats
        self.max_speed = max_speed
        self.passengers = []
        self.free_seats = max_seats
        self.seats = {i: None for i in range(1, max_seats + 1)}

    @property
    def has_free_seats(self):
        return self.free_seats > 0

    def board(self, *names):
        for name in names:
            if self.free_seats > 0:
                self.passengers.append(name)
                self.free_seats -= 1
                for seat in self.seats:
                    if self.seats[seat] is None:
                        self.seats[seat] = name
                        break
            else:
                print(f'There are no available places for {name}.')

    def debrark(self, *names):
        for name in names:
            if name in self.passengers:
                self.passengers.remove(name)
                self.free_seats += 1
                for seat in self.seats:
                    if self.seats[seat] == name:
                        self.seats[seat] = None
                        break
            else:
                print(f'{name} is not a bus passenger.')

    def increase_speed(self, value):
        self.speed = min(self.speed + value, self.max_speed)

    def decrease_speed(self, value):
        self.speed = max(self.speed - value, 0)

    def __contains__(self, name):
        return name in self.passengers

    def __iadd__(self, name):
        self.board(name)
        return self

    def __isub__(self, name):
        self.debrark(name)
        return self

bus = Bus(max_seats=2, max_speed=90)

bus.board('Ivanov')
bus.board('Tokarev')
print(bus.passengers)
print(bus.has_free_seats)

bus += 'Petrov'
print(bus.seats)
print(bus.has_free_seats)

bus -= 'Tokarev'
print(bus.has_free_seats)
print(bus.seats)

bus.increase_speed(40)
print(bus.speed)




















