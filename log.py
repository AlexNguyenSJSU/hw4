import time

def timestamp (func):
    def wrapper():
        current_time = time.ctime()
        print(current_time)
        func()

    return wrapper
