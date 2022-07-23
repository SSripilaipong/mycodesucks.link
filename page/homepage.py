from dataclasses import dataclass
from typing import List

import jinja2
from jinja2 import Environment, FileSystemLoader
from lambler.template import TemplateBase


@dataclass
class AdviceForSignal:
    title: str
    short_description: str
    link: str


@dataclass
class Signal:
    title: str
    advice_list: List[AdviceForSignal]


class HomepageTemplate(TemplateBase):
    def __init__(self, template: jinja2.Template):
        self._template = template

    @classmethod
    def load(cls) -> 'HomepageTemplate':
        return cls(Environment(loader=FileSystemLoader('page')).get_template("homepage.html"))

    def render(self, signals: List[Signal]) -> str:
        return self._template.render(signals=signals)
