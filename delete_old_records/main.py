import asyncio
from loguru import logger

from erudite import Erudite


@logger.catch
async def main():
    er = Erudite()
    await er.get_all_records()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
