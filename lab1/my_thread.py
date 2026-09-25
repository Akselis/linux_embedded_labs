import threading
import time
from typing import Callable

class MyThread(threading.Thread):

    def __init__(self, target: Callable | None = None, args: tuple = (), kwargs: dict | None = None, **thread_kwargs):
            super().__init__(**thread_kwargs)
            self.my_target = target
            self.my_args = args
            self.my_kwargs = kwargs or {}
            self.t0 = time.time()

    def __str__(self) -> str:
         return f"{self.name} delta time: {time.time() - self.t0}"

    def start(self):
        print(f"Thread {self.name} starting")
        super().start()

    def run(self):
        if self.my_target:
            self.my_target(*self.my_args, **self.my_kwargs)
