class Restaurant():
    '''餐馆'''
    def __init__(self, restaurant_name, cuisine_type):
        '''初始化'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        '''餐厅名字，类型'''
        print("This restaurant name is :" + self.restaurant_name.title() + ".")
        print("This restaurant cuisine type is :" + self.cuisine_type.title() + ".")

    def open_restaurant(self):

        print("Restaurant open!")

restaurant = Restaurant('chen', 'china')
restaurant.describe_restaurant()
restaurant.open_restaurant()
