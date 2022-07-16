from http import HTTPStatus

from lambler.content import Content
from lambler.http import HttpApi, HtmlResponse

handler = HttpApi()


@handler.get("")
def homepage(page: str = Content("page/homepage.html")):
    return HtmlResponse(HTTPStatus.OK, page)
