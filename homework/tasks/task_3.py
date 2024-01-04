import asyncio
from dataclasses import dataclass
from typing import Awaitable, List


@dataclass
class Ticket:
    number: int
    key: str


async def coroutines_execution_order(coros: List[Awaitable[Ticket]]) -> str:

    tickets = await asyncio.gather(*coros)

    sorted_tickets = sorted(tickets, key=lambda ticket: ticket.number)

    result = ''.join(ticket.key for ticket in sorted_tickets)

    return result


if __name__ == "__main__":

    async def just_return_ticket(t: Ticket) -> Ticket:
        return t

    tickets = [
        Ticket(number=2, key="мыла"),
        Ticket(number=1, key="мама"),
        Ticket(number=3, key="раму"),
    ]
    coros: List[Awaitable[Ticket]] = [just_return_ticket(t) for t in tickets]
    res = asyncio.run(coroutines_execution_order(coros))
    print(res)