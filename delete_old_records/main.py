import asyncio
from loguru import logger

from core.apis.erudite import Erudite
from core.apis.drive import Drive
from core.utils import alert


def get_offline(records: list) -> list:
    new_records = [record for record in records if record.get('type') == 'Offline1']
    return new_records


@logger.catch
@alert("popashuta@miem.hse.ru")
async def main():
    er = Erudite()
    drive = Drive()

    records = await er.get_needed_records()
    offline_records = get_offline(records)

    for record in offline_records:
        logger.info(f"Deleting record - {record}")
        await drive.delete_video(record.get('url'))
        await er.delete_record(record.get('id'))



if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

