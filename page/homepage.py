from dataclasses import dataclass
from typing import List

import jinja2
from jinja2 import BaseLoader, Environment
from lambler.content import Content
from lambler.template import TemplateBase


@dataclass
class Signal:
    title: str


class HomepageTemplate(TemplateBase):
    def __init__(self, template: jinja2.Template):
        self._template = template

    @classmethod
    def load(cls, page: str = Content("page/homepage.html")) -> 'HomepageTemplate':
        return cls(Environment(loader=BaseLoader()).from_string(page))

    def render(self, signals: List[Signal]) -> str:
        return self._template.render(signals=signals)
