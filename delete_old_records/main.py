import asyncio
from loguru import logger

from apis.erudite import Erudite


@logger.catch
def filter(records: list) -> list:
    pass


@logger.catch
async def main():
    er = Erudite()
    records = await er.get_needed_records()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
