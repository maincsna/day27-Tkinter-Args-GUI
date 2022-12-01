def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

# print(add(3, 5, 6))

def calculator(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

#
# calculator(add=3, multiply=5)

class Car:

    def __init__(self,**kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make = "Nissan", model="Alex")
print(my_car.model)