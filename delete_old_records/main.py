import asyncio
from loguru import logger

from core.apis.erudite import Erudite
from core.apis.drive import Drive
from core.gmail import alert_async


def get_offline(records: list) -> list:
    new_records = [record for record in records if record.get('type') == 'Offline1']
    if len(new_records) > 0:
        logger.info("Offline records older than needed date found")
        return new_records
    else:
        logger.warning("No offline records older than needed date found")
        return []


@logger.catch
@alert_async
async def main():
    erudite = Erudite()
    drive = Drive()

    records = await erudite.get_needed_records()
    offline_records = get_offline(records)
    logger.info(offline_records)

    tasks = []
    for record in offline_records:
        tasks.append(erudite.delete_record(record.get('id')))
        tasks.append(drive.delete_video(record.get('url')))  

    await asyncio.gather(*tasks)

    logger.info("All needed records deleted")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

