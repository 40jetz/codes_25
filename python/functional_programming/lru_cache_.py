from functools import lru_cache

@lru_cache
def fibonacci (n: int) -> int:

    if n <= 1:
        return n
    
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
for i in range (1,41):
    print(f' {i}: {fibonacci(i)}')