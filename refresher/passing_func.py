def methodception(another):
    return another()


def add_two_numbers():
    return 35 + 77


# print(methodception(add_two_numbers))
# print(methodception(lambda:35+77))
my_list = [13, 56, 77, 484]
print(list(filter(lambda x: x != 13, my_list)))
print([x for x in my_list if x!=13])
print((lambda x: x *3)(5))