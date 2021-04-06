import asyncio
from loguru import logger

from apis.erudite import Erudite
from apis.drive import Drive


@logger.catch
def filter(record: list) -> bool:
    if record.get('type') == 'Offline':
        return True
    else:
        return False


@logger.catch
async def main():
    er = Erudite()
    drive = Drive()
    records = await er.get_needed_records()
    for i in range(len(records)):
        if filter(records[i]):
            #print(records[i])
            await drive.delete_video(records[i].get('url'))



if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
