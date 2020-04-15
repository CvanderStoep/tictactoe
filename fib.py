from functools import lru_cache
import pandas as pd
print(pd.__version__)

@lru_cache()
def fibonacci(n):
    if n <= 2: return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(1, 100):
    print(i, fibonacci(i))
