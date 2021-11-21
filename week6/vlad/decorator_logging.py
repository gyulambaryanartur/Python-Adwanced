import time
import functools
import datetime


def timeit(filepath: str) -> callable:
    def decor(func: callable) -> callable:
        @functools.wraps(func)
        def wrapper(*args: tuple, **kwargs: dict):
            with open(filepath, 'a+') as log:
                log.write(
                    f'{func.__name__}\n'
                    f'{datetime.datetime.now()}\n'
                    f'{args}\n'
                    f'{kwargs}\n\n'
                )
            func(*args, **kwargs)

        return wrapper
    return decor


@timeit('foo.log')
def foo():
    time.sleep(2)
    print('foo is called')


@timeit('bar.log')
def bar(num: int):
    time.sleep(4)
    print('bar is called')


if __name__ == '__main__':
    bar(14)
    foo()
