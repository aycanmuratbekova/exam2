
const_hour = 40

class Employee:

    def __init__(self, name: object, pin: object, hour: object) -> object:
        self.name = name
        self.pin = pin
        self.hour = hour



    def calc_salary(self):
        pass

    def total_salary(self):
        pass

    def calc_performance(self):
        pass

    def spent_comp_money(self):
        pass


class Manager(Employee):
    def __init__(self, name, pin, hour):
        super().__init__(name, pin, hour)

    def calc_salary(self):
        return self.hour*200


class Secretary(Employee):
    pass

class SalesPerson(Employee):
    def __init__(self, name, pin, hour, salary, sell_count):
        super().__init__(name, pin, hour)
        self.sell_count = sell_count
        self.salary = salary

class Worker(Employee):
    def __init__(self, name, pin, hour, salary, sell_count):
        super().__init__(name, pin, hour)
        self.sell_count = sell_count
        self.salary = salary

    def calc_salary(self):
        return (self.salary + (self.hour) * 100)

class SecretaryEmployee(Employee):
    pass

manager = Manager('Aiperi', 1, 40)
worker = Worker('Asan', 2, 20, 20000, 22)

personal = [manager, worker]


def spend_comp_money():
    total_money = sum([ person.calc_salary() for person in personal])
    print("total_money ", total_money)

def prnt_info():
    for person in personal:
        print(
            f" ID : {person.pin}  Name : {person.name}"
        )

spend_comp_money()
prnt_info()


