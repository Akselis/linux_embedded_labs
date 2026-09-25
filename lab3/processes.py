from multiprocessing.connection import PipeConnection, Connection
import os
import time as t
from datetime import datetime
from gpiozero import CPUTemperature

def send_temperature(interval: float, send_conn: PipeConnection):
    if send_conn.closed:
        print(f"[{os.getpid()}] Error: connection closed. Terminating")
        return

    for _ in range(0, 10):
        temp = CPUTemperature.temperature
        send_conn.send(temp)
        t.sleep(interval)

    send_conn.send(None)
    send_conn.close()

def read_temperature(recv_conn: PipeConnection):
    if recv_conn.closed:
        print(f"[{os.getpid()}] Error: connection closed. Terminating")
        return

    temp = recv_conn.recv()
    if temp is None:
        print(f"[{os.getpid()}] Error: sentinel value received. Terminating")
        recv_conn.close()
    if not isinstance(temp, property):
        print(f"[{os.getpid()}] Error: temperature expected. Terminating")
        recv_conn.close()

    print(f"[{os.getpid()}] {datetime.now():%I:%M:%S %p} \t\t {temp} *C")
