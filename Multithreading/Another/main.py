import threading 
import time 
start = time.perf_counter()

def func(seconds):
    time.sleep(seconds)
    print("The Execution time is {s}".format(s = seconds))
func(2)
end = time .perf_counter()

print(f"Execution time is {end-start}")

t1 = threading.Thread(target=func,args=[2])
t2 = threading.Thread(target=func,args=[3])
t3 = threading.Thread(target=func,args=[4])

t1.run()
t2.run()
t3.run()

t1.join()
t2.join()
t3.join()

end = time .perf_counter()
print(f"The Thread execution time is {end-start}")