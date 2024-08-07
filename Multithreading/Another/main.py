import threading 
import time 
from concurrent.futures import ThreadPoolExecutor
start = time.perf_counter()

def func(seconds):
    time.sleep(seconds)
    print("The Execution time is {s} second . ".format(s = seconds))

func(2)
end = time .perf_counter()

print(f"Execution time is {end-start}")

# t1 = threading.Thread(target=func,args=[2])
# t2 = threading.Thread(target=func,args=[3])
# t3 = threading.Thread(target=func,args=[4])

# t1.run()
# t2.run()
# t3.run()

# t1.join()
# t2.join()
# t3.join()
'''
Func function runs 10 times and it sleeps for seconds give by the user 
'''
with ThreadPoolExecutor() as executor :
    pass 
threads = [] 
for i in range(1,11):
    # t = threading.Thread(target=func,args=[i])
    t = threading.Thread(target=func,args=[1.5])
    t.start()
    threads.append(t)
for thread in threads:
    thread.join()
print(threads)
end = time .perf_counter()
print(f"The Thread execution time is {end-start}")