import asyncio
from typing import Coroutine


async def limit_execution_time(coro: Coroutine, max_execution_time: float) -> None:
    await asyncio.wait_for(coro, timeout=max_execution_time)


async def limit_execution_time_many(*coros: Coroutine, max_execution_time: float) -> None:
    limited_coros = [asyncio.wait_for(coro, timeout=max_execution_time) for coro in coros]
    await asyncio.gather(*limited_coros)
