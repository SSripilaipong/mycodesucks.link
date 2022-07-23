from dataclasses import dataclass
from typing import List


@dataclass
class Advice:
    id_: str
    title: str
    title_url: str
    short_description: str
    paragraphs: List[str]


too_much_coupling = Advice(
    id_="62d7ea5f5a58191ee7e59115",
    title="โค้ดแต่ละส่วนเราผูกมัดกันเกินไปหรือเปล่า",
    title_url="โค้ดแต่ละส่วนเราผูกมัดกันเกินไปหรือเปล่า",
    short_description="ทำความเข้าใจแนวคิดเรื่องของ coupling และ cohesion จะช่วยให้เราออกแบบ "
                      "class ต่าง ๆ ของเราได้ดีขึ้น "
                      "จะช่วยป้องกันผลกระทบของการแก้ไขโค้ดแต่ละส่วนได้",
    paragraphs=[
        "การที่โค้ดแต่ละส่วนขึ้นต่อกัน ทำให้การเปลี่ยนแปลงแก้ไข ที่ส่วนหนึ่งของโค้ด "
        "อาจจะทำให้อีกส่วนหนึ่งต้องแก้ตามด้วย",

        "เช่น class A ต้องใช้ฟังก์ชัน f ของ class B "
        "จะทำให้เมื่อมีการเปลี่ยนแปลงแก้ไขโค้ดของฟังก์ชัน f ใน B อาจจะทำให้เราต้องไปแก้โค้ดของ A ด้วย "
        "เช่น แก้ parameter ของ f แก้ return type หรือแก้ logic ในการคำนวณภายใน ของ f<br>"
        "ก็มีโอกาสทำให้เราต้องมาแก้โค้ดของ A ได้ทั้งสิ้น",

        "เพราะฉะนั้น ยิ่งโค้ดแต่ละส่วนของเราขึ้นต่อกันมากเท่าไหร่ ก็มีโอกาสที่การแก้โค้ดแค่เล็ก ๆ น้อย ๆ "
        "จะให้เราเหนื่อย ตามแก้งานเยอะมากเท่านั้น เราเรียกโค้ดลักษณะนี้ว่า "
        "<i>\"มี coupling ต่อกันสูง (Tight Coupling)\"</i> ",

        "การจะออกแบบระบบให้มี coupling ต่ำได้ ขึ้นอยู่กับความสามารถของ engineer, ความรู้เรื่อง design "
        "patterns, และความซับซ้อนของปัญหาด้วย",

        "ผมขอแนะนำคลิปเรื่องของ coupling และ cohesion จาก Code Opinion ที่เล่ามุมมองเกี่ยวกับ coupling และ cohesion "
        "และยกตัวอย่างในระดับของโค้ด, ระดับของ layer, และระดับของ service มาเล่าให้ฟังกันครับ",

        '<div class="embed-responsive embed-responsive-16by9"><iframe class="embed-responsive-item"'
        'src="https://www.youtube.com/embed/YDNR_gfBk0Q" title="YouTube video '
        'player" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; '
        'picture-in-picture" allowfullscreen></iframe></div>',
    ],
)

advice_mapper = {
    too_much_coupling.id_: too_much_coupling,
}
