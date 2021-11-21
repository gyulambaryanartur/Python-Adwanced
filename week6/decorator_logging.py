import time
import functools
import datetime


def type(*arg: tuple, **kwarg: dict) -> callable:
    def decor(func: callable) -> callable:
        @functools.wraps(func)
        def wrapper(*args: tuple, **kwargs: dict):
            print(f'type{arg} pluss {kwarg}')
            argtype = list(zip(arg, args))
            args = []
            for items in argtype:
                args.append(eval(f'{str(items[0]).split()[1][1:-2:]}({items[1]})'))
            if kwarg:
                tp=str(kwarg.values()).split()[1][1:-4:]  
                fn = eval(f'{tp}({func(*args, **kwargs)})')
            else:
                fn = func(*args, **kwargs)
            return (fn)
        return wrapper
    return decor


@type(int, float,ret=int)
def foo(a, b):
    return a+b
@type(float)
def bar(a):
    return a



if __name__ == '__main__':
    print(bar(14))
    print(foo(4, 5))
