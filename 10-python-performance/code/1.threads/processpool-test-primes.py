import time 
import concurrent.futures
import math

NUMBERS = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419,
    432353452334352,
    342545345343445]

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

start = time.perf_counter()
answers = [is_prime(p) for p in NUMBERS]
print(f"One thread: answers={answers}, time={time.perf_counter()-start} sec")

THREADCOUNT=4
start = time.perf_counter()
with concurrent.futures.ProcessPoolExecutor(THREADCOUNT) as executor:
    futures = [executor.submit(is_prime, p) for p in NUMBERS] 
    answers = []
    for future in concurrent.futures.as_completed(futures):   # return each result as soon as it is completed:
        answers.append(future.result())
print(f"{THREADCOUNT} threads: answers={answers}, time={time.perf_counter()-start} sec")
