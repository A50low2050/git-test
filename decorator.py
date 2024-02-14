
def hello(func):
    def wrapper():
        print('start')
        func()
        print('end25')
        print('hi')

    return wrapper


def some_funct():
    print('hello')


some_funct = hello(some_funct)
some_funct()
