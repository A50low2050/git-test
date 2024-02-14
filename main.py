
def my_func(func):

    def wrapper(*args, **kwargs):
        print('start')
        func(*args, **kwargs)
        print('end')

    return wrapper


def some_func(title):
    print(f'{title}')
    print('some')


some_func = my_func(some_func)
some_func(title='test')
print('test')
