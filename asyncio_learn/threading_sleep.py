import os
from time import sleep
from threading import Thread


def for_fun():
    sleep(1)
    print(f'PID={os.getpid()}\n')


threads = [
    Thread(target=for_fun) for _ in range(10)
]
[t.start() for t in threads]
[t.join() for t in threads]
