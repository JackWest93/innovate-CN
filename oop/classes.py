class Person():
    def __init__(self, name, age, height):
        self.name=name
        self.age=age
        self.height=height

    def set_location(self, city, country):
        self.city_=city
        self.country_=country

    def get_location(self):
        print(self.city_)
        print(self.country_)