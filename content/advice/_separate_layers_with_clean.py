from content.advice import Advice, Paragraph

separate_layers_with_clean = Advice(
    id_="62d96a915a5819259704414e",
    title="ใช้ Clean Architecture แยก domain logic ออกจากส่วนอื่น ๆ",
    title_url="ใช้_Clean_Architecture_แยก_domain_logic_ออกจากส่วนอื่น ๆ",
    short_description="abc",
    content=[
        Paragraph(
            "ในระบบใหญ่ ๆ ที่ทุกอย่างเกี่ยวข้องกันไปหมด (ลองนึกภาพ class diagram ใหญ่ ๆ มีเส้นโยงกันยุบยับ) "
            "การแก้ไขทำได้ลำบาก แก้โค้ดนิดหน่อยอาจจะกระทบส่วนอื่น ๆ ไปหมด แนวทางหนึ่งคือเราแยกระบบออกเป็นระบบย่อย ๆ "
            "ตาม "
            "task/feature ที่เราทำ แล้วเราทำให้แต่ละระบบย่อยมีความเกี่ยวข้องกัน มี dependency ต่อกัน ให้น้อยที่สุด"
        ),
    ],
)
