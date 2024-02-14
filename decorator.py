
def hello(func):
    def wrapper():
        print('start')
        func()
        print('end')

    return wrapper


def some_funct():
    print('hello')


some_funct = hello(some_funct)
some_funct()
