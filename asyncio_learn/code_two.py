import asyncio
import random

c = (
    "\033[0m",  # End of color
    "\033[36m",  # Cyan
    "\033[91m",  # Red
    "\033[35m",  # Magenta
)


async def makerandom(idx: int, tresh: int = 6):
    print(c[idx + 1] + f'Initialize {idx}')
    i = random.randint(1, 10)
    while i <= tresh:
        print(c[idx + 1] + f'color is {idx} == {i}')
        await asyncio.sleep(idx + 1)
        i = random.randint(0, 10)
    print(c[idx + 1] + f"---> Finished: makerandom({idx}) == {i}" + c[0])


async def main():
    res = await asyncio.gather(*(makerandom(i, 10 - i - 1) for i in range(3)))
    return res


if __name__ == '__main__':
    asyncio.run(main())
