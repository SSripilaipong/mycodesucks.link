from http import HTTPStatus

from lambler.http import HttpApi, HtmlResponse
from lambler.template import Template

from page.homepage import HomepageTemplate, Signal

handler = HttpApi()


@handler.get("")
def homepage(template: HomepageTemplate = Template()):
    signals = [
        Signal(title="เปลี่ยนโค้ดนิดหน่อย ที่อื่นพัง ต้องแก้ตามอีก 10 ที่ เหนื่อย!"),
        Signal(title="มีฟังก์ชันที่ซับซ้อนมาก ๆ ไม่มีใครเข้าใจ คนเขียนลาออกไปแล้ว 😭"),
        Signal(title="ฝั่ง business พูดอย่างนึง ในโค้ดเขียนอีกอย่าง งง!"),
    ]
    return HtmlResponse(HTTPStatus.OK, template.render(signals=signals))
