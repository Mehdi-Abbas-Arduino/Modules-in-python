# thread = a flow of execution like a seperate order of instructions .
#          However each thread takes a turn running to achieve concurrency 
#          GIL = global lock interpreter 
#             allows one thread to hold the control of python interpreter

# cpu Bound = program / task most of it's time waiting for internal events use multiprocessing

# IO Bound =  program / task spend most of it's waiting for external events use multithreading 

import threading
import time 
# start = time.time()
print(threading.active_count())
print(threading.enumerate())
# print(time.thread_time())
# end = time.time()
# print(f"The execution time taken is {end-start}")
import multiprocessing
# print(multiprocessing.active_children())