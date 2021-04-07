import asyncio
from loguru import logger

from apis.erudite import Erudite
from apis.drive import Drive


def get_offline(records: list) -> list:
    new_records = [record for record in records if record.get('type') == 'Offline1']
    return new_records


@logger.catch
async def main():
    er = Erudite()
    drive = Drive()

    records = await er.get_needed_records()
    offline_records = get_offline(records)
    for record in offline_records:
        print(record)
        await drive.delete_video(record.get('url'))
        await er.delete_record(record.get('id'))



if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

