import functools


# def my_decorator(func):
#     @functools.wraps(func)
#     def function_that_runs_fun():
#         print("In the decorator!")
#         func()
#         print('After the decorator')
#     return function_that_runs_fun


# @my_decorator  # get called before another function
# def my_function():
#     print('Im in the function!')


# my_function()


def decrorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func(*args, **kwargs):
            print('I am in the decorator!')
            if number == 56:
                print('Not runniing the funciton')
            else:
                func(*args, **kwargs)
            print('After the decorator')
        return function_that_runs_func
    return my_decorator


@decrorator_with_arguments(57)
def my_function_too(x, y):
    # print("Hello")
    print(x+y)


my_function_too(57, 68)
