# -*- coding: utf-8 -*-
from asyncio import new_event_loop

from src.ktc_api.aio import AKTCClient


async def main():
    client = AKTCClient()
    actual_version = await client.actual_version()
    print(actual_version.description)
    await client.close()


if __name__ == '__main__':
    loop = new_event_loop()
    loop.run_until_complete(main())
    loop.close()
