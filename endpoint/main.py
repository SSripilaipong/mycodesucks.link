from http import HTTPStatus

from lambler.http import HttpApi, HtmlResponse, Param
from lambler.template import Template

from content.advice import advice_mapper, too_much_coupling, Advice
from page.advice import AdvicePage
from page.homepage import HomepageTemplate, Signal, AdviceForSignal

handler = HttpApi()


def _make_advice_for_signal(advice: Advice) -> AdviceForSignal:
    return AdviceForSignal(title=advice.title, short_description=advice.short_description,
                           link=f"/advice/{advice.id_}-{advice.title_url}")


@handler.get("")
def homepage(template: HomepageTemplate = Template()):
    signals = [
        Signal(title="เปลี่ยนโค้ดนิดหน่อย ที่อื่นพัง ต้องแก้ตามอีก 10 ที่ เหนื่อย!", advice_list=[
            _make_advice_for_signal(too_much_coupling),
            AdviceForSignal(
                title="ใช้ Modular Monolith แยกระบบใหญ่ออกเป็นระบบย่อย ๆ ตามส่วนงาน",
                short_description="abc",
                link="/advice/62d7e95a5a58191ee7e59114-ใช้_Modular_Monolith_แยกระบบใหญ่ออกเป็นระบบย่อย",
            ),
            AdviceForSignal(
                title="ใช้ Clean Architecture แยก domain logic ออกจากส่วนอื่น ๆ",
                short_description="abc",
                link="/advice/62d96a915a5819259704414e-ใช้_Clean_Architecture_แยก_domain_logic_ออกจากส่วนอื่น ๆ",
            ),
        ]),
        Signal(title="มีฟังก์ชันที่ซับซ้อนมาก ๆ ไม่มีใครเข้าใจ คนเขียนลาออกไปแล้ว 😭", advice_list=[
            AdviceForSignal(
                title="สร้าง testcase ก่อน refactor ทุกครั้ง",
                short_description="abc",
                link="/advice/62d96bcf5a5819259704414f-สร้าง_testcase_ก่อน_refactor_ทุกครั้ง",
            ),
            AdviceForSignal(
                title="จะ refactor ทั้งที ต้องทำให้คนอื่นเข้าใจด้วย โดยใช้ Domain-Driven Design",
                short_description="abc",
                link="/advice/62d96bda5a58192597044150-จะ_refactor_ทั้งที_ต้องทำให้คนอื่นเข้าใจด้วย_"
                     "โดยใช้_Domain_Driven_Design",
            ),
            AdviceForSignal(
                title="document เหตุผลการ refactor แต่ละครั้งเอาไว้ ช่วยให้คนอื่นเข้าใจง่ายขึ้น",
                short_description="abc",
                link="/advice/62d96be55a58192597044151-document_เหตุผลการ_refactor_แต่ละครั้งเอาไว้_"
                     "ช่วยให้คนอื่นเข้าใจง่ายขึ้น",
            ),
        ]),
        Signal(title="ฝั่ง business พูดอย่างนึง ในโค้ดเขียนอีกอย่าง งง!", advice_list=[
            AdviceForSignal(
                title="Domain-Driven Design เขียนโค้ดให้เหมือนเวลาคุยกัน",
                short_description="abc",
                link="/advice/62d96be55a58192597044151-Domain_Driven_Design_เขียนโค้ดให้เหมือนเวลาคุยกัน",
            ),
            AdviceForSignal(
                title="Event Storming Workshop ให้ dev และ business มองภาพงานในมุมเดียวกัน",
                short_description="abc",
                link="/advice/62d96be55a58192597044151-Event_Storming_Workshop_ให้_dev_และ_business_"
                     "มองภาพงานในมุมเดียวกัน ",
            ),
            AdviceForSignal(
                title="อธิบายงานด้วย Story อย่าสั่งงานด้วย requirement",
                short_description="abc",
                link="/advice/62d96be55a58192597044151-อธิบายงานด้วย_Story_อย่าสั่งงานด้วย_requirement",
            ),
            AdviceForSignal(
                title="ทำความเข้าใจสิ่งที่ business ต้องการจริง ๆ ด้วย Impact Mapping",
                short_description="abc",
                link="/advice/62d96be55a58192597044151-ทำความเข้าใจสิ่งที่_business_ต้องการจริง_ๆ_ด้วย_Impact_Mapping",
            ),
        ]),
        Signal(title="โค้ดเราเขียน Testcase ยากมากกก ไม่อยากเขียนแล้ว", advice_list=[
            AdviceForSignal(
                title="Test-Driven Development เขียน testcase ก่อนเขียนโค้ด ง่ายกว่านะ",
                short_description="abc",
                link="/advice/62d96be55a58192597044151-Test_Driven_Development_เขียน_testcase_ก่อนเขียนโค้ด_ง่ายกว่านะ",
            ),
            AdviceForSignal(
                title="Dependency Injection ช่วยให้สามารถ test logic โดยไม่ต้องต่อ database จริง ได้ง่ายขึ้น",
                short_description="abc",
                link="/advice/62d96be55a58192597044151-Dependency_Injection_ช่วยให้สามารถ_test_logic_"
                     "โดยไม่ต้องต่อ_database_จริง_ได้ง่ายขึ้น ",
            ),
            AdviceForSignal(
                title="เขียน testcase แบบ What ไม่ใช่แบบ How",
                short_description="abc",
                link="/advice/62d96be55a58192597044151-เขียน_testcase_แบบ_What_ไม่ใช่แบบ_How",
            ),
        ]),
        Signal(title="เขียน Testcase มาแล้วเป็นภาระ แก้โค้ดนิดหน่อย Testcase พัง ต้องมาซ่อมอีก", advice_list=[
            AdviceForSignal(
                title="อย่าเขียน testcase ที่ผูกกับ detail มากเกินไป",
                short_description="abc",
                link="/advice/62d96be55a58192597044151-abc",
            ),
        ]),
        Signal(title="โค้ดปัจจุบันแก้ยากมาก ต้องไปแก้ที่ class นู้นที class นี้ที", advice_list=[
            AdviceForSignal(
                title="ของที่ใช้ด้วยกัน เก็บไว้ใกล้กัน และแยกตามงานที่ต้องทำ",
                short_description="abc",
                link="/advice/62d96be55a58192597044151-abc",
            ),
            AdviceForSignal(
                title="Domain-Driven Design แบ่งส่วนต่าง ๆ ของระบบตามมุมมองทาง business",
                short_description="abc",
                link="/advice/62d96be55a58192597044151-abc",
            ),
        ]),
        Signal(title="ประเมิณเวลาที่ต้องใช้ใน project ไม่แม่น มีงานงอกขึ้นมาเรื่อย ๆ โดนดุ เครียด 😢", advice_list=[
            AdviceForSignal(
                title="estimate คลาดเคลื่อน ไม่ใช่ความผิดของ dev (หรือใครทั้งนั้น)",
                short_description="abc",
                link="/advice/62d96be55a58192597044151-abc",
            ),
            AdviceForSignal(
                title="เลี่ยงทำ project ใหญ่รวดเดียว, ทำ feature ย่อย ๆ ทีละ feature ดีกว่า",
                short_description="abc",
                link="/advice/62d96be55a58192597044151-abc",
            ),
        ]),
    ]
    return HtmlResponse(HTTPStatus.OK, template.render(signals=signals))


@handler.get("/advice/{key}")
def advice_page(key: str = Param("key"), template: AdvicePage = Template()):
    id_, _ = key.split("-", maxsplit=1)
    return HtmlResponse(HTTPStatus.OK, template.render(advice_mapper[id_]))
