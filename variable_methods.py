# # # def my_print_method(par):
# # #     print(par)

# # # # my_print_method(1)


# # # def my_multiply(numberOne, numberTwo):
# # #     return numberOne*numberTwo

# # # my_print_method(my_multiply(2,4))

# # # === list
# # grades = [77, 80, 90, 95, 100]
# # tuple_grades = (77, 80, 90, 95, 100)  # immutable
# # set_grades = {77, 80, 90, 95, 100, 100}  # unique & unordered

# # # print(sum(grades)/len(grades))
# # # grades.append(78)
# # # tuple_grades = tuple_grades+ (100,)
# # # set_grades[0]=20
# # set_grades.add(60)
# # # print(set_grades)

# # set_one = {1, 2, 3, 4, 5}
# # set_two = {1, 3, 5, 7, 9, 11}
# # # print(set_one.intersection(set_two))
# # # print(set_one.union(set_two))
# # # print(set_one.difference(set_two))

# # # my_var = 'hello'
# # # for character in my_var: # iterables are strings, lists, sets, tuple and more
# # #     print(character)

# # # grades = [77, 80, 90, 95, 100]
# # # for num in grades:
# # #     print(num **2)

# # user_wants_number = True
# # while user_wants_number == True:
# #     print(10)
# #     user_input = input("Should we print again?(y/n)")
# #     if user_input == 'n':
# #         user_wants_number =False

# def who_do_you_know():
#     user_input = input("List the people that you know by space")
#     users = [user_input.strip().lower() for person in user_input.split()]
#     # print(newList)
#     return users


# def ask_user():
#     # known_people = ['Hiroko','Tomoko']
#     user_input = input("name?")
#     if user_input in who_do_you_know():
#         print('I know {}'.format(user_input))


# ask_user()

# # my_list = [0, 1, 2, 3, 4]
# # print([x for x in range(5)])
# # print([x * 3 for x in range(5)])
# # print([n for n in range(10) if n % 2 == 0])
# people_you_know = ['Rolf', 'John', ' Anna', "greg"]
# normalized_ppl = [person.strip().lower() for person in people_you_know]
# print(normalized_ppl)
# # who_do_you_know()

my_set = {1, 3, 5}
my_dic = {'name': 'John', 'age': 23, 'grades': [13, 34, 45, 78]}
another_dic = {1: 23, 2: 34, 3: 45}

lottery_player = {
    "name": "John",
    "numbers": (13, 45, 67, 89)
}

unversities = [
    {
    'name': 'Oxford',
    'location': 'UK'
},
    {
    'name': 'MIT',
    'location': 'US'
}
]

print (sum(lottery_player['numbers']))

