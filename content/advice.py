from dataclasses import dataclass


@dataclass
class Advice:
    id_: str
    title: str
    short_description: str
    content: str


too_much_coupling = Advice(
    id_="62d7ea5f5a58191ee7e59115",
    title="โค้ดแต่ละส่วนเราผูกมัดกันเกินไปหรือเปล่า",
    short_description="ทำความเข้าใจแนวคิดเรื่องของ coupling และ cohesion จะช่วยให้เราออกแบบ "
                      "class ต่าง ๆ ของเราได้ดีขึ้น "
                      "จะช่วยป้องกันผลกระทบของการแก้ไขโค้ดแต่ละส่วนได้",
    content="abc<i>pqr</i>")

advice_mapper = {
    too_much_coupling.id_: too_much_coupling,
}
