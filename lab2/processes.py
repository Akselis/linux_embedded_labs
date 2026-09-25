from multiprocessing import Queue
import random as r
import os

def sendRandomInt(min: int, max: int, queue: Queue):
    while True:
        num = r.randint(min, max)
        print(f"[{os.getpid()}] The generated number is {num}")
        if(num != 0):
            queue.put(num)
        else:
            queue.put(None)
            print(f"[{os.getpid()}] Sentinel value sent. Terminating.")
            return

def receiveRandomInt(queue: Queue):
    while True:
        num = queue.get()
        if num is None:
            print(f"[{os.getpid()}] Sentinel value received. Terminating.")
            return
        if not isinstance(num, int):
            print(f"[{os.getpid()}] Error: number expected. Terminating.")
            return
        square = num ** 2
        print(f"[{os.getpid()}] {num} * {num} = {square}")
