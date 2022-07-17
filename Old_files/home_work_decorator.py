import functools
import sys
from collections import OrderedDict
import requests as requests

def cache(max_limit=64):
    def internal(f):
        @functools.wraps(f)
        def deco(*args, **kwargs):
            cache_key = (args, tuple(kwargs.items()))
            if cache_key in deco._cache:
                # увеличиваем счетчик обращений к url
                value_count = list(deco._cache[cache_key])
                value_count[0] += 1
                deco._cache[cache_key] = tuple(value_count)
                # переносимо в кінець списку
                deco._cache.move_to_end(cache_key, last=True)
                print("repeat in", *deco._cache.items())
                return deco._cache[cache_key]
           
            result = f(*args, **kwargs)
            # видаляємо якшо досягли ліміта
            if len(deco._cache) >= max_limit:
                # сортируем словарь по значению счетчика
                deco._cache = OrderedDict(sorted(deco._cache.items(), key=lambda x: x[1][0]))
                # видаляємо перший елемент
                deco._cache.popitem(last=False)

            deco._cache[cache_key] = result
            print("first in", *deco._cache.items())
            return result

        deco._cache = OrderedDict()
        return deco

    return internal

count = 1
@cache(max_limit=6)
def fetch_url(url, first_n=10):
    """Fetch a given url"""
    res = requests.get(url)
    return (count, res.content[:first_n]) if first_n else  (count, res.content)

fetch_url('https://ithillel.ua')
fetch_url('https://ithillel.ua')
fetch_url('https://google.com')
fetch_url('https://ithillel.ua')
fetch_url('https://dou.ua')
fetch_url('https://ain.ua')
fetch_url('https://google.com')
fetch_url('https://google.com')
fetch_url('https://dou.ua')
fetch_url('https://ain.ua')
fetch_url('https://ithillel.ua')
fetch_url('https://dou.ua')
