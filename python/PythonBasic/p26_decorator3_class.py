from datetime import datetime


class DatetimeDecorator(object):
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        print(datetime.now())
        self.func(*args, **kwargs)
        print(datetime.now())
        print()

class MainClass(object):
    @DatetimeDecorator
    def func1():
        print("Main Function1 start")

    @DatetimeDecorator
    def func2():
        print("Main Function2 start")

    @DatetimeDecorator
    def func3():
        print("Main Function3 start")

my_obj = MainClass()
print(my_obj.func1())
my_obj.func2()
my_obj.func3()