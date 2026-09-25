from multiprocessing import Process, Pipe
from processes import send_temperature, read_temperature

def main():
    (conn1, conn2) = Pipe()
    p1 = Process(target=send_temperature, args=(0.5, conn1,))
    p2 = Process(target=read_temperature, args=(conn2,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if __name__ == "__main__":
    main()
