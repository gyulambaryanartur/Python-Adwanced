import functools
import datetime
import time

def timeit(filepath:str)->callable:
    def decor(func: callable) -> callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            func(*args, **kwargs)
            print('estimation time for ', func.__name__, ':', time.time()-start)
            with open(filepath, "a") as fl:
                fl.write(
                    f'func call time:{datetime.datetime.now()}  estimation time for ,func_name :{func.__name__},:,{time.time()-start}\n')
        return wrapper
    return decor

@timeit('aa.txt')
def foo():
    time.sleep(2)
    print('foo is called')


@timeit('bar.txt')
def bar():
    time.sleep(4)
    print('bar is called')


if __name__ == "__main__":
    bar()
    foo()
