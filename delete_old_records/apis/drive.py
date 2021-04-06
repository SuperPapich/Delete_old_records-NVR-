import os
import pickle
from loguru import logger

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from settings import settings


class Drive:
    CREDS_PATH = settings.creds_path
    TOKEN_PATH = settings.token_path
    SCOPES = "https://www.googleapis.com/auth/drive"

    def __init__(self) -> None:
        self.refresh_token()
        self.service = build("drive", "v3", credentials=self.creds)

    def refresh_token(self) -> None:
        self.creds = None
        if os.path.exists(self.TOKEN_PATH):
            with open(self.TOKEN_PATH, "rb") as token:
                self.creds = pickle.load(token)
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.CREDS_PATH, self.SCOPES
                )
                self.creds = flow.run_local_server(port=0)
            with open(self.TOKEN_PATH, "wb") as token:
                pickle.dump(self.creds, token)
        if self.creds:
            logger.info("Creds created sucssessfully")

    async def delete_video(self, video_url: str) -> None:
        video_id = video_url.split('/')[5]
        try:
            request = self.service.files().delete(fileId=video_id).execute()

        except HttpError as error:
            logger.error(error)






