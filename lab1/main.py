from my_thread import MyThread
import functions as f
import time

def main():
    t1 = MyThread(name = "counter-thread", target=f.count, args=(-30, 30, 2, 2.5, time.time()))
    t2 = MyThread(name = "greeting-thread", target=f.greeting, args=(5, time.time()))
    t3 = MyThread(name = "alphabet-thread", target=f.alphabet, args=(3.5, time.time()))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()
