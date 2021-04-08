from loguru import logger
from aiohttp import ClientSession

from ..settings import settings


class Erudite:
    ERUDITE_API_URL = settings.erudite_url
    ERUDITE_API_KEY = settings.erudite_api_key
    DEL_DATE = settings.del_date

    async def get_needed_records(self) -> list:
        params = {"todate": self.DEL_DATE}
        async with ClientSession() as session:
            records = await session.get(
                f"{self.ERUDITE_API_URL}/records", params=params
            )
            async with records:
                records = await records.json()

        if type(records) == list:
            logger.info(f"Records older than {self.DEL_DATE} found")
            return records
        else:
            logger.warning("No records found")
            return []

        

    async def delete_record(self, record_id: str):
        async with ClientSession() as session:
            res = await session.delete(
                f"{self.ERUDITE_API_URL}/records/{record_id}",
                headers={"key": self.ERUDITE_API_KEY},
            )
            async with res:
                ans = await res.json()

        if res.status == 200:
            logger.info(f"Record with id: {record_id} deleted")
        elif res.status == 404:
            logger.info(f"Record with id: {record_id} is not found in Erudite")
        else:
            logger.error("Erudite is not working properly...")
