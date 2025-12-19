from functools import lru_cache
import time  

@lru_cache(maxsize=None)
def fx(a): 
    time.sleep(3)
    return (a**2)

print(fx(3))
print(fx(4))
print(fx(6))
print(fx(7))
print(fx(8))
print(fx(3))
print(fx(4))
print(fx(5))
print(fx(6))
print(fx(7))
print(fx(8))