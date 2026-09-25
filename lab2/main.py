from multiprocessing import Process, Queue
from processes import sendRandomInt, receiveRandomInt

def main():
    q = Queue()
    p1 = Process(target=sendRandomInt, args=(-20, 20, q))
    p2 = Process(target=receiveRandomInt, args=(q, ))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if __name__ == "__main__":
    main()
