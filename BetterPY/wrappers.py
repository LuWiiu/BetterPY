from expectType import expect
from threading import Thread
import time

def ExOnMake(func):
    func()
    def wrapper():
        return func()
    return wrapper

def demoFunc(func):
    def wrapper():
        a = func()
        print(f"{a} came from function {func.__name__}")
        return a
    return wrapper

def expectFunc(func):
    def wrapper(*args):
        c = func(*args)
        if len(c) < 2: return c[0]
        a = c[0]
        b = c[-1]
        if expect.strict(a, b): return a
    return wrapper

def debugFunc(func):
    def wrapper():
        _time = time.time()
        a = func()
        print(f"{a} came from function {func.__name__} in time {time.time() - _time}")
        return a
    return wrapper

if __name__ == "__main__":
    @ExOnMake
    @demoFunc
    def p(): print("hi")

    @expectFunc
    def w(): return [0, str]
    w()

    @debugFunc
    def q(): print("b")
    q()