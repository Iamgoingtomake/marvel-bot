from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from app.utils import string_utils

from .base import MarvelResourceDTO


@dataclass
class EventDTO(MarvelResourceDTO):

    title: str
    start: Optional[datetime]
    end: Optional[datetime]
    description: Optional[str] = None

    def __str__(self):
        return f"{self.id} - {self.title}"

    @property
    def short_description(self):
        return string_utils.limit_text(self.description)

    def build_twitter_status(self, title):
        status = f"{title}\n\n"
        status += f'What do you know about "{self.title}" ?\n'
        status += self.build_links_label()

        return status

    def build_telegram_status(self, title):
        status = f"*{title}*\n\n"
        status += f'What do you know about "{self.title}" ?\n'
        status += self.build_markdown_links()

        return status
