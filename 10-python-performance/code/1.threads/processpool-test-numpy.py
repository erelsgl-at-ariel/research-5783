import time 
import concurrent.futures
import numpy as np

def sum_list(thelist:np.array):
	return np.sum(thelist**3//10)

start = time.perf_counter()

LISTSIZE = 40000000
big_list = np.array(range(LISTSIZE), dtype='int64')

start = time.perf_counter()
big_sum=sum_list(big_list)
print(f"One thread: sum={big_sum}, time={time.perf_counter()-start} sec")

THREADCOUNT=4
SUBLISTSIZE = LISTSIZE//THREADCOUNT
start = time.perf_counter()
with concurrent.futures.ProcessPoolExecutor(THREADCOUNT) as executor:
    futures = [executor.submit(sum_list, big_list[i*SUBLISTSIZE:(i+1)*SUBLISTSIZE]) for i in range(THREADCOUNT)] 
    big_sum = 0
    for res in concurrent.futures.as_completed(futures):   # return each result as soon as it is completed:
        r = res.result()
        # print("Partial sum: ", r)
        big_sum += r
print(f"{THREADCOUNT} threads: sum={big_sum}, time={time.perf_counter()-start} sec")
