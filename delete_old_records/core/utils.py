import smtplib
from loguru import logger
from functools import wraps

from .settings import settings


def alert(mail: str):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                result = await func(*args, **kwargs)
            except Exception as error:
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(mail, settings.gmail_password)
                logger.info("Login success")
                message = f"Delete all records has an error - {error}"
                server.sendmail(mail, mail, message)
                logger.info("Email sent!")
                server.close()
                raise Exception

        return wrapper

    return decorator
