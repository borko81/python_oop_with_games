import asyncio
import time


async def main():
    print(f'{time.ctime()} Hello')
    await asyncio.sleep(1)
    print(f'{time.ctime()} Goodbye')


#
# loop = asyncio.get_event_loop()
# task = loop.create_task(main())
# loop.run_until_complete(task)

async def f():
    return 123


coro = f()
try:
    coro.send(None)
except StopIteration as e:
    print('The answer was:', e.value)


class A:
    def __iter__(self):
        self.x = 0
        return self

    def __next__(self):
        if self.x > 2:
            raise StopIteration
        self.x += 1
        return self.x


[print(i) for i in A()]
