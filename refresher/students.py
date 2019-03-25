# class Students:
#     def __init__(self, name, school):
#         self.name = name
#         self.school = school
#         self.marks = []

#     def avg(self):
#         return sum(self.marks) / len(self.marks)

#     # def go_to_school(self):
#     #     print("I'm going to school")

#     @staticmethod
#     def go_to_school():
#         print("I'm going to school")

#     # @classmethod
#     # def go_to_school(cls):
#     #     print("I'm going to school")

# anna = Students("Anna", "MIT")
# anna.marks.append(56)
# anna.marks.append(60)
# anna.marks.append(90)
# print(anna.marks)
# print(anna.avg())
# anna.go_to_school()
# Students.go_to_school() #does not work when self argument

# === Exercise
# class Store:
#     def __init__(self, name):
#         self.name = name
#         self.items = []

#     def add_item(self, name, price):
#         self.items.append({
#             "name": name,
#             "price": price
#         })

#     def stock_price(self):
#         # total = 0
#         # for item in self.items:
#         #     total += item["price"]
#         # return total
#         return sum([item['price'] for item in self.items])


# tj = Store("TraderJoes")
# tj.add_item("Tomato", 10)
# tj.add_item("yogurt", 5)
# print(tj.stock_price())

# == exercise
class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, plus " - franchise"
        print ("{} - franchise".format(store.name))

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        print('{}, total stock price: {}'.format(
            store.name.upper(), int(store.stock_price()))


store = Store("Test")
store2 = Store("Amazon")
store2.add_item('keyboard', 160)

Store.franchise(store)
Store.franchise(store2)
Store.store_details(store)
Store.store_details(store2)
