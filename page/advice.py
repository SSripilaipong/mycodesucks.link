import jinja2
from jinja2 import FileSystemLoader, Environment
from lambler.template import TemplateBase

from content.advice import Advice


class AdvicePage(TemplateBase):
    def __init__(self, template: jinja2.Template):
        self._template = template

    @classmethod
    def load(cls) -> 'AdvicePage':
        return cls(Environment(loader=FileSystemLoader('page')).get_template("advice.html"))

    def render(self, advice: Advice) -> str:
        return self._template.render(paragraphs=advice.paragraphs, title=advice.title)
