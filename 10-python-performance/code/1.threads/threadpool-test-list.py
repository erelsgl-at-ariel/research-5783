import time 
import concurrent.futures

def sum_list(thelist:list):
	s = 0
	for x in thelist:
		s += x**3//10
	return s

start = time.perf_counter()

LISTSIZE = 5000000
big_list = list(range(LISTSIZE))

start = time.perf_counter()
big_sum=sum_list(big_list)
print(f"One thread: sum={big_sum}, time={time.perf_counter()-start} sec")

THREADCOUNT=4
SUBLISTSIZE = LISTSIZE//THREADCOUNT
start = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor(THREADCOUNT) as executor:
    futures = [executor.submit(sum_list, big_list[i*SUBLISTSIZE:(i+1)*SUBLISTSIZE]) for i in range(THREADCOUNT)] 
    big_sum = 0
    for res in concurrent.futures.as_completed(futures):   # return each result as soon as it is completed:
        r = res.result()
        # print("Partial sum: ", r)
        big_sum += r
print(f"{THREADCOUNT} threads: sum={big_sum}, time={time.perf_counter()-start} sec")
