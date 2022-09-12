import asyncio


async def counter():
    print('Start')
    await asyncio.sleep(1)
    print('end')


async def main():
    await asyncio.gather(counter(), counter(), counter())


if __name__ == '__main__':
    import time

    s = time.perf_counter()
    asyncio.run(main())
    print(f'Elapsed time is {(time.perf_counter() - s):.2f}')
