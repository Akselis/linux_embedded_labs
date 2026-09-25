from multiprocessing.connection import Connection
import os
import time as t
from datetime import datetime
from gpiozero import CPUTemperature

def send_temperature(interval: float, send_conn: Connection):
    if send_conn.closed:
        print(f"[{os.getpid()}] Error: connection closed. Terminating")
        return

    cpu = CPUTemperature()
    for _ in range(0, 10):
        temp = cpu.temperature
        send_conn.send(temp)
        t.sleep(interval)

    send_conn.send(None)
    send_conn.close()

def read_temperature(recv_conn: Connection):
    if recv_conn.closed:
        print(f"[{os.getpid()}] Error: connection closed. Terminating")
        return

    while True:
        temp = recv_conn.recv()
        if temp is None:
            print(f"[{os.getpid()}] Error: sentinel value received. Terminating")
            recv_conn.close()
            return
        if not isinstance(temp, float):
            print(f"[{os.getpid()}] Error: temperature expected. Terminating")
            recv_conn.close()
            return

        print(f"[{os.getpid()}] {datetime.now():%I:%M:%S %p} \t\t {temp} *C")
