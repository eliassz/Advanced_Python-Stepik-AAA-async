async def task_1(i: int, order: list):
    order.append("1")
    if i == 0:
        return
    if i > 5:
        await task_2(i // 2, order)
    else:
        await task_2(i - 1, order)


async def task_2(i: int, order: list):
    order.append("2")
    if i == 0:
        return
    if i % 2 == 0:
        await task_1(i // 2, order)
    else:
        await task_2(i - 1, order)


async def coroutines_execution_order(i: int = 42) -> int:
    order = []
    await task_1(i, order)
    return int("".join(order))

if __name__ == "__main__":
    import asyncio

    res = asyncio.run(coroutines_execution_order(7))
    print(res)
