import time
def my_timer(orig_func):
    """ programmer: Erel Segal Halevy"""
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f'{ orig_func.__name__} ran in: {t2} sec')
        return result
    return wrapper