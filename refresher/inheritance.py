class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    # passing both args and kwags to cope with everything
    def friend(cls, origin, friend_name, *args, **kwargs):
        return cls(friend_name, origin.school, *args, **kwargs)
    # ==== passing **kwargs only
    # def friend(cls, origin, friend_name, **kwargs):
    #     return cls(friend_name, origin.school, **kwargs)
    # ==== passing *args only
    # def friend(cls, origin, friend_name, *args):
    #     return cls(friend_name, origin.school, *args)


class WorkingStudent(Student):
    def __init__(self, name, school, salary, job_title):
        super().__init__(name, school)
        self.salary = salary
        self.job_title = job_title


# anna = WorkingStudent('Anna','Oxford',20.00, 'Software Developer')
anna = WorkingStudent('Anna', 'Oxford', 20.00, 'Software Developer')
print(anna.salary)

friend = WorkingStudent.friend(
    anna, 'Greg', 17.5, job_title='Software Dev')
# friend = WorkingStudent.friend(anna, 'Greg', 17.5,'Software Dev')
print(friend.name)
print(friend.school)
print(friend.salary)


# ===========args, kwargs
# === *args : dont know how many args out there
# == *kwargs: dictionary
def what_are_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)


# kwargs return dictionary
what_are_kwargs(12, 4, 56, name='Jose', location='UK')
