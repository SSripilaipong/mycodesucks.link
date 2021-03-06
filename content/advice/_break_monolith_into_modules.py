from content.advice import Advice, Paragraph, Video

break_monolith_into_modules = Advice(
    id_="62d7e95a5a58191ee7e59114",
    title="ใช้ Modular Monolith แยกระบบใหญ่ออกเป็นระบบย่อย ๆ ตามส่วนงาน",
    title_url="ใช้_Modular_Monolith_แยกระบบใหญ่ออกเป็นระบบย่อย",
    short_description="ระบบขนาดใหญ่ที่ทุกส่วนเกี่ยวข้องเชื่อมโยงกันหมด ทำให้การแก้ไขโค้ดทำได้ลำบาก "
                      "การแยกระบบออกเป็นส่วนย่อย ๆ ที่เกี่ยวข้องกันให้น้อยที่สุด จะป้องกันผลกระทบของการแก้ไข "
                      "ไม่ให้แพร่กระจายไปทั่วระบบได้ แต่เราไม่จำเป็นต้องทำ microservices เสมอไปนะ!",
    content=[
        Paragraph(
            "ในระบบใหญ่ ๆ ที่ทุกอย่างเกี่ยวข้องกันไปหมด (ลองนึกภาพ class diagram ใหญ่ ๆ มีเส้นโยงกันยุบยับ) "
            "การแก้ไขทำได้ลำบาก แก้โค้ดนิดหน่อยอาจจะกระทบส่วนอื่น ๆ ไปหมด แนวทางหนึ่งคือเราแยกระบบออกเป็นระบบย่อย ๆ "
            "ตาม "
            "task/feature ที่เราทำ แล้วเราทำให้แต่ละระบบย่อยมีความเกี่ยวข้องกัน มี dependency ต่อกัน ให้น้อยที่สุด"
        ),
        Paragraph(
            "ในส่วนของการแยกระบบเป็นส่วนย่อย ๆ ส่วนมากเรามักจะนึกถึงการทำ microservices "
            "ซึ่งมันเพิ่มภาระในการดูแลให้กับทีมมากพอสมควร หลาย ๆ ครั้ง โดยเฉพาะสำหรับทีมเล็ก ๆ "
            "ข้อเสียของ microservices อาจจะไม่คุ้มข้อดีด้วยซ้ำ "
        ),
        Paragraph(
            "ในส่วนของการทำให้มี dependency ต่อกันน้อยที่สุด วิธีหนึ่งที่ทำได้ คือเราลดการ call method ของ class "
            "โดยตรง "
            "แล้วเปลี่ยนมาเป็นการสื่อสารผ่าน messaging แทน"
        ),
        Paragraph(
            "เช่น จากเดิม class A เรียกฟังก์ชัน f ของ class B "
            "เราเปลี่ยนให้ A ส่ง message M ไปที่ message queue แทน (เช่น Kafka หรือ RabbitMQ) แล้ว B รออ่าน message "
            "ทำให้ A กับ B ไม่ได้มีความเกี่ยวข้องกันโดยตรง <i>การแก้ไข A จะไม่ทำให้ B มีปัญหามาก</i> "
            "ตราบที่คนเขียน A กับ B สัญญากันว่าเราจะสื่อสารกันด้วย message หน้าตา M นะ มี field ตามนี้นะ"
        ),
        Paragraph(
            "ข้อเสียคือ A กับ B จะไม่สามารถทำงานแบบ synchronous ได้ ก็ต้องดูว่าในทาง business "
            "2 สิ่งนี้มันต้องทำงานต่อเนื่องกันหรือเปล่า หรือสามารถทำเป็น asynchronous ได้หรือไม่"
        ),
        Paragraph(
            "<i>Modular Monolith</i> คือเราแบ่งโค้ดของเราออกเป็น modules ย่อย ๆ เหมือนกับ microservices "
            "แต่มันยังเป็นก้อนเดียวกันอยู่ deploy พร้อมกัน test พร้อมกัน ทำให้เราได้ข้อดีของทั้ง microservices และ "
            "monolith คือระบบแบ่งเป็นส่วนย่อย ๆ และมี dependency ต่อกันน้อย เพราะสื่อสารกันด้วย messaging "
            "ในขณะที่ยังสามารถดูแลได้ง่ายอยู่ deploy ง่าย test ง่าย แก้ไขโค้ดได้ง่ายด้วย เพราะเรายังเป็น monolith อยู่"
        ),
        Paragraph(
            "ข้อเสียที่ต้องคิดคือ มันก็ยัง implement ยากอยู่ คือต้องมีระบบ messaging และต้องออกแบบการสื่อสารในลักษณะ "
            "asynchronous message ด้วย ซึ่งถ้าจากเดิมเราทำ monolith อยู่ อาจจะต้องประเมิณก่อนว่า "
            "cost ของการ refactor มันคุ้มหรือเปล่า"
        ),
        Paragraph(
            "ลองดูคลิปจาก <b>Code Opinion</b> เรื่องของ Modular Monolith จะช่วยให้เห็นภาพมากขึ้นครับ"
        ),
        Video("https://www.youtube.com/embed/VGShtGU3hOc"),
        Paragraph(
            "เกี่ยวกับเรื่องของ messaging ลองดูคลิปนี้จาก GOTO Conference โดย <b>Martin Fowler</b> "
            "จะเห็นรูปแบบที่หลากหลาย "
            "ของการรับส่ง message/event/command รวมทั้งปัญหาต่าง ๆ ที่อาจจะเกิดขึ้นได้ มากยิ่งขึ้นครับ"
        ),
        Video("https://www.youtube.com/embed/STKCRSUsyP0"),
    ],
)
