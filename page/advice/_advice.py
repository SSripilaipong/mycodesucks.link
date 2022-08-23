from typing import Union

import jinja2
from jinja2 import FileSystemLoader, Environment
from lambler.template import TemplateBase

from content.advice import Advice, Paragraph, Video


class AdvicePage(TemplateBase):
    def __init__(self, template: jinja2.Template):
        self._template = template

    @classmethod
    def load(cls) -> 'AdvicePage':
        return cls(Environment(loader=FileSystemLoader('page')).get_template("advice/advice.html"))

    def render(self, advice: Advice) -> str:
        content = [make_content(c) for c in advice.content]
        return self._template.render(content_list=content, title=advice.title)


def make_content(c: Union[Paragraph, Video]) -> str:
    if isinstance(c, Paragraph):
        return f'<p class="color-secondary">{c.text}</p>'
    elif isinstance(c, Video):
        return (
            f'<div class="video-content"><div class="ratio ratio-16x9"><iframe src="{c.embed_url}" title="YouTube '
            f'video player" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; '
            f'picture-in-picture" allowfullscreen></iframe></div></div>')
    raise NotImplementedError()
