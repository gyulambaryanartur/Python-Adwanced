import time
import functools
import datetime


def type(*arg: tuple, **kwarg: dict) -> callable:

    def decor(func: callable) -> callable:
        @functools.wraps(func)
        def wrapper(*args: tuple, **kwargs: dict):
            # gathering types and values in one list
            argtype = list(zip(arg, args))
            args = []
            a=1
            print(type(a))
            for items in argtype:
                # converting args
                if isinstance(items[1], items[0]):
                    args.append(items[1])
                    

                else:
                    raise Exception("types are not compatable")
                if kwarg:
                   
                   if isinstance(items[1], items[0]) and \
                       (list(kwarg.values())[0]==items[0] or list(kwarg.values())[0]==float):
                    continue
                   
                   else:
                    raise Exception("types are not compatable")

                
            fn = func(*args, **kwargs)
            return (fn)
        return wrapper
    return decor


@type(int, int, ret=int)
def foo(a, b):
    return a+b


@type(float)
def bar(a):
    return a


if __name__ == '__main__':
    print(bar('ja'))
    print(foo(4, 5))
