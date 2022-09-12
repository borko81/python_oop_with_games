import concurrent.futures
from concurrent.futures import ThreadPoolExecutor as Executor
from threading import Thread
import time


def worker(data):
    print(f'The name is {data}')


names = 'first second last'.split()

with Executor(max_workers=4) as exe:
    result = []
    for n in names:
        result.append(exe.submit(worker, data=n))

    for future in concurrent.futures.as_completed(result):
        future.result()

print('-' * 30)
for n in names:
    thread = Thread(target=worker, args=(n,))
    thread.start()
    print('Waiting')
    thread.join()

