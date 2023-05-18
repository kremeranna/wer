class IceCreamStand:
    def __init__(self, name, flavors, location, working_hours, type_flavors):
        self.name = name
        self.flavors = flavors
        self.location = location
        self.working_hours = working_hours
        self.type_flavors = type_flavors

    def show_flavors(self):
        print("Доступные вкусы мороженого:")
        for flavor in self.flavors:
            print("- " + flavor)

    def add_flavor(self, flavor):
        self.flavors.append(flavor)
        print(f'{flavor} добавлен в список')

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            print(f'{flavor} удален из списка')
        else:
            print(f'{flavor} не найден в списке')

    def check_flavor(self, flavor):
        if flavor in self.flavors:
            print(f'{flavor} есть в списке')
        else:
            print(f'{flavor} нет в списке')

    def describe_stand(self):
        print(f"Кафе: {self.name}")
        print(f"Место: {self.location}")
        print(f"Время работы: {self.working_hours}")

    def show_Typesflavors(self):
        print("Список вариантов мороженого:")
        for types in self.type_flavors:
            print("- " + types)


my_stand = IceCreamStand("ice", ['ванильное', 'шоколадное', 'клубничное'],
                         'ул. Солдата Корзуна', '9.00 - 18.00',
                         ['стаканчик', 'эскимо', 'шарик'])

my_stand.describe_stand()
my_stand.show_flavors()
my_stand.show_Typesflavors()

my_stand.check_flavor("ванильное")
my_stand.check_flavor("черничное")

my_stand.add_flavor("мятное")
my_stand.check_flavor("мятное")

my_stand.remove_flavor("шоколадное")
my_stand.check_flavor("шоколадное")