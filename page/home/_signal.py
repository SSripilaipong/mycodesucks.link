from dataclasses import dataclass
from typing import List


@dataclass
class AdviceForSignal:
    title: str
    short_description: str
    link: str


@dataclass
class Signal:
    title: str
    advice_list: List[AdviceForSignal]
