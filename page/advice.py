from lambler.template import TemplateBase

from content.advice import Advice


class AdvicePage(TemplateBase):
    def __init__(self, template: str):
        self._template = template

    @classmethod
    def load(cls) -> 'AdvicePage':
        return cls("<html><body>{content}</body></html>")

    def render(self, advice: Advice) -> str:
        return self._template.format(content=", ".join([advice.title, advice.short_description, advice.content]))
