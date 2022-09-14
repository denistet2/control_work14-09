# 1) Напишите программу, которая содержит функцию calculation(),
# которая принимает два параметра и вычисляет сумму и разность.
# Кроме того, данная функция сразу должна возвращать и сумму и разность.
# Результат вывести на экран.

def calculation():
    _summ = a + b
    _razn = a - b
    return (_summ), (_razn)
a=input()
b=input()
a=int(a)
b=int(b)
print(calculation())

# 2) Создайте дочерний класс Bus, который наследуется от класса Vehicle.
# Плата за проезд (fare) по умолчанию для любого транспортного средства составляет вместимость (capacity) * 100.
# Если транспортное средство является экземпляром автобуса,
# нам нужно добавить дополнительные 10% к полной стоимости проезда в качестве платы за обслуживание.
# Исходный код:
#
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity
    def fare(self):
        return self.capacity * 100 * 0.1
#
School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())
print(School_bus())
#






# 3) Напишите программу, которая содержит генератор calculation(),
# который принимает два параметра и вычисляет сумму и разность.
# Сперва возвращается сумма, потом разность.
# Результат вывести на экран.
def calculation():
    # первые два условия
    _num1 = a + b
    yield _num1
    _num2 = a - b
    yield _num2
_z = calculation()



a=input()
b=input()
a=int(a)
b=int(b)

print(next(_z))
print(next(_z))