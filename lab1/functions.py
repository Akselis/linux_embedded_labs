import time
import threading
import string

def count(start, stop, step, interval, t0: float = 0):
    for s in range(start, stop, step):
        if t0 == 0:
            print(f"{threading.current_thread().name}: {s}")
        else:
            dt = "{:.2f}".format(time.time() - t0)
            print(f"[dt = {dt}s] {threading.current_thread().name}: {s}")
        time.sleep(interval)
        if(s + step == stop):
            count(stop, start, -step, interval, t0)

def greeting(interval, t0: float = 0):
    while True:
        if t0 == 0:
            print(f"Hello from {threading.current_thread().name}")
        else:
            dt = "{:.2f}".format(time.time() - t0)
            print(f"[dt = {dt}s] Hello from {threading.current_thread().name}")
        time.sleep(interval)

def alphabet(interval, t0: float = 0):
    a = string.ascii_uppercase
    for letter in a:
        if t0 == 0:
            print(f"{threading.current_thread().name}: {letter}")
        else:
            dt = "{:.2f}".format(time.time() - t0)
            print(f"[dt = {dt}s] {threading.current_thread().name}: {letter}")
        time.sleep(interval)
        if letter == a[-1]:
            alphabet(interval, t0)
