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
        Signal(title="โค้ดเราเขียน Testcase ยากมากกก ไม่อยากเขียนแล้ว"),
        Signal(title="เขียน Testcase มาแล้วเป็นภาระ แก้โค้ดนิดหน่อย Testcase พัง ต้องมาซ่อมอีก"),
        Signal(title="ประเมิณเวลาที่ต้องใช้ใน project ไม่แม่น มีงานงอกขึ้นมาเรื่อย ๆ โดนดุ เครียด 😢"),
    ]
    return HtmlResponse(HTTPStatus.OK, template.render(signals=signals))
