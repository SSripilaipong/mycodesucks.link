from typing import List

import jinja2
from jinja2 import Environment, FileSystemLoader
from lambler.template import TemplateBase

from ._signal import Signal


class HomeTemplate(TemplateBase):
    def __init__(self, template: jinja2.Template):
        self._template = template

    @classmethod
    def load(cls) -> 'HomeTemplate':
        return cls(Environment(loader=FileSystemLoader('page')).get_template("home/home.html"))

    def render(self, signals: List[Signal]) -> str:
        return self._template.render(signals=signals)
