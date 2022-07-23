from dataclasses import dataclass
from typing import List, Union


@dataclass
class Paragraph:
    text: str


@dataclass
class Video:
    embed_url: str


@dataclass
class Advice:
    id_: str
    title: str
    title_url: str
    short_description: str
    content: List[Union[Paragraph, Video]]
