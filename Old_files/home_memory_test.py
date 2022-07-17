import functools
import sys
import psutil
from memory_profiler import profile
from memory_profiler import memory_usage

# измерение использования памяти (возможность выбора для декоратора):
# 1. sys.getsizeof(),
# 2. memory_usage() from memory_profiler,
# 3. psutil.Process(),
# 4. recursion function from GitHub
# 5. @profile from memory_profiler.

# декоратор memory_profiler, выводит размер памяти используемой декоратором test_mem(f):
@profile
def test_mem(f):
    @functools.wraps(f)
    def deco(*args, **kwargs):
        result = f(*args, **kwargs)
        # измерение и вывод используемой памяти при помощи системной функции sys.getsizeof()
        mem_getsizeof = sys.getsizeof(result)
        print(f'1) Working sys.getsizeof() in decorator. Usage memory:', mem_getsizeof)
        #result = mem_getsizeof # возможен возврат аргумента
        # измерение и вывод используемой памяти при  функции memory_usage() библиотеки memory_profiler
        mem_usage = memory_usage()
        print('2) Working memory_usage in decorator. Usage memory:', mem_usage)
        #result = mem_usage # возможен возврат аргумента
        # измерение в используемой памяти при помощи  функции библиотеки psutil memory_info()
        mem_psutil = psutil.Process().memory_info()
        print('3) Working psutil memory_info() in decorator. Usage memory:', mem_psutil, '\n')
        #result = mem_psutil # возможен возврат аргумента
        # рекурсивная функция измерение в используемой памяти c GitHub
        def get_size(obj, seen=None):
            # From https://goshippo.com/blog/measure-real-size-any-python-object/
            # Recursively finds size of objects
            size = sys.getsizeof(obj)
            if seen is None:
                seen = set()
            obj_id = id(obj)
            if obj_id in seen:
                return 0
            # Important mark as seen *before* entering recursion to gracefully handle
            # self-referential objects
            seen.add(obj_id)
            if isinstance(obj, dict):
                size += sum([get_size(v, seen) for v in obj.values()])
                size += sum([get_size(k, seen) for k in obj.keys()])
            elif hasattr(obj, '__dict__'):
                size += get_size(obj.__dict__, seen)
            elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
                size += sum([get_size(i, seen) for i in obj])
            return size
        print('4) Working recursion function from GitHub in decorator. Usage memory:', get_size(f))
        return result
    return deco
# декоратор функции memory_test():
@test_mem
# декоратор memory_profiler, выводит размер памяти используемой функцией memory_test():
@profile
def memory_test():
    # измерение и вывод используемой памяти при помощи системной функции sys.getsizeof()
    mem_getsizeof = sys.getsizeof(memory_test)
    print('1) Working sys.getsizeof() in memory_test(). Usage memory :', mem_getsizeof)
    # измерение и вывод используемой памяти при помощи функции memory_usage() библиотеки memory_profiler
    mem_usage = memory_usage()
    print('2) Working memory_usage in memory_test(). Usage memory:', mem_usage)
    # измерение в используемой памяти при помощи функции библиотеки psutil memory_info()
    mem_psutil = psutil.Process().memory_info()
    print('3) Working psutil.Process().memory_info() in memory_test(). Usage memory:', mem_psutil, '\n')
    # можно использовать любой аргумент для декоратора: 1. mem_getsizeof, 2. mem_usage, 3. mem_psutil.
    return mem_getsizeof

# возможно получение любого элемента из декоратора
print(f'!!! Print any returned arguments from ({memory_test.__name__}): {memory_test()} \n')