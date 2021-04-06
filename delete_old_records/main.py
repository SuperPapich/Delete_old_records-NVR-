import asyncio
from loguru import logger

from apis.erudite import Erudite
from apis.drive import Drive


def get_offline(records: list) -> list:
    records = [record for record in records if record.get('type') == 'Offline1']
    return records


@logger.catch
async def main():
    er = Erudite()
    drive = Drive()

    records = await er.get_needed_records()
    offline_records = get_offline(records)
    print(offline_records)
    await drive.delete_video("https://drive.google.com/file/d/1v-4-wUJ4klnVLRcjTcjCHlfQJz6DRRKj/preview")
    #print(offline_records)
    # for record in records:
    #     await drive.delete_video(records[i].get('url'))



if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
