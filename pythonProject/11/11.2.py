class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('Ресторан {} предлагает кухню {}.'.format(self.restaurant_name, self.cuisine_type))

    def open_restaurant(self):
        print('Ресторан {} открыт!'.format(self.restaurant_name))

restaurant1 = Restaurant('Макдоналдс', 'фастфуд')
restaurant2 = Restaurant('Potter', 'европейская')
restaurant3 = Restaurant('Sashimi', 'японская')

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
