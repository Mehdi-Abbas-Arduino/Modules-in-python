# thread = a flow of execution like a seperate order of instructions .
#          However each thread takes a turn running to achieve concurrency 
#          GIL = global lock interpreter 
#             allows one thread to hold the control of python interpreter

# cpu Bound = program / task most of it's time waiting for internal events use multiprocessing

# IO Bound =  program / task spend most of it's waiting for external events use multithreading 

import threading
import time 
from concurrent.futures import ThreadPoolExecutor
# Indicates some task be done
print(threading.active_count())
def func (seconds):
    print(f"Sleeping for {seconds}")
    time.sleep(seconds)
    return seconds
time1 = time.perf_counter()

# func(seconds=4)
def main():
    t1 = threading.Thread(target=func,args=[4])

    t2 = threading.Thread(target=func,args=[2])

    t3 = threading.Thread(target=func,args=[1])

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    time2 = time.perf_counter()
    print(f"Execution time is {time2-time1}")

def poolingDemo():
    with ThreadPoolExecutor() as executor:
        # future = executor.submit(func,3)
        # print(future.result())
        # future = executor.submit(func,5)
        # print(future.result())
        # future = executor.submit(func,6)
        # print(future.result())
        l = [3,5,6,7,8]
        results = executor.map(func,l)
        for result in results:
            print(result)

poolingDemo()