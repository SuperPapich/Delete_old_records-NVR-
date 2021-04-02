from loguru import logger
from aiohttp import ClientSession
from datetime import datetime, timedelta

from settings import settings


class Erudite:
    ERUDITE_API_URL = settings.erudite_url
    ERUDITE_API_KEY = settings.erudite_api_key
    DEL_DATE = settings.del_date

    async def get_all_records(self):
        async with ClientSession() as session:
            records = await session.get(
                f"{self.ERUDITE_API_URL}/records", params={"todate": self.DEL_DATE}
            )
            async with records:
                records = await records.json()
            logger.info(records)
