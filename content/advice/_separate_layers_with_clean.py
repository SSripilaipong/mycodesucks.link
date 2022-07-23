from content.advice import Advice, Paragraph

separate_layers_with_clean = Advice(
    id_="62d96a915a5819259704414e",
    title="ใช้ Clean Architecture แยก domain logic ออกจากส่วนอื่น ๆ",
    title_url="ใช้_Clean_Architecture_แยก_domain_logic_ออกจากส่วนอื่น ๆ",
    short_description="แก้ logic นิดหน่อย REST API พัง หรือแก้ JSON ของ REST API นิดหน่อย database พังเฉย "
                      "อาจจะเป็นเพราะว่าแต่ละส่วน หรือแต่ละ layer ของเรามันปนกันอยู่หรือเปล่า "
                      "มาดูว่าจะแยกมันออกจากกันยังไงดี",
    content=[
        Paragraph(
            "คิดว่าหลายท่านน่าจะเห็นด้วย ว่าในหลาย ๆ ครั้ง โค้ดของเราซับซ้อน, อ่านยาก, ดูแลยาก, แก้ไขยาก "
            "เป็นเพราะเทคโนโลยีรอบ ๆ ที่เราเลือกนำมาใช้ เช่น database, REST API, หรือ API ภายนอกต่าง ๆ "
            "ซึ่งมันอาจจะทำให้ logic สำคัญของระบบ ที่เป็นตัวขับเคลื่อนธุรกิจของเรา สามารถพัฒนาได้ลำบาก"
        ),
        Paragraph(
            "แนวคิดของ Clean Architecture คือการที่เราแยก domain logic ออกจากส่วน technical ต่าง ๆ ของระบบ "
            "ไม่ว่าจะเป็น database หรือ API ใด ๆ domain logic จะต้องไม่ไป import หรือมี dependency ไปหาส่วนอื่น ๆ"
        ),
        Paragraph(
            "บางท่านอาจจะไม่คุ้นเคย เพราะเวลาทำระบบแบบง่าย ๆ พอเราเรียกตัว logic ให้ทำงาน ตัว logic ที่ import "
            "database client เข้ามาก็แค่เรียกตัว client ให้ทำงาน แล้วก็เอา database model ที่ได้กลับมา convert เป็น "
            "json response ส่งไปให้ frontend ตรง ๆ"
        ),
        Paragraph(
            "ซึ่งในงานที่ไม่ซับซ้อน วิธีนี้ก็ไม่ได้เลวร้ายแต่อย่างใด แต่พอเราเริ่มต้องทำ logic ต่าง ๆ "
            "ที่ซับซ้อนมากขึ้น ทีมเริ่มมีหลายคน แต่ละคนดูแลแต่ละส่วนแยกกันออกไป ก็อาจจะปัญหาที่เล่ามาได้ "
            "เช่น คนที่ดูแล database model แก้ data model นิดหน่อย ปรากฎโค้ดส่วน logic พัง "
            "หรือไม่ก็หน้าตาข้อมูล JSON บน REST API ดันเปลี่ยนตามซะงั้น frontend ก็เรียกใช้ไม่ได้"
        ),
        Paragraph(
            "Clean Architecture ก็เป็นแนวทางหนึ่งที่จะช่วยให้เราจัดการโค้ดของเรา ให้ดูแลแก้ไขง่าย "
            "และที่สำคัญ ทำงานร่วมกับคนในทีมได้ง่าย โดยใช้เทคนิค Dependency Inversion คือสลับทิศทางของ dependency "
            "แทนที่จะให้ domain logic ไปเรียกใช้ส่วนของ database และส่วนอื่น ๆ เราสร้าง interface ของสิ่งที่ "
            "domain logic จะใช้งานขึ้นมาภายในส่วนของ domain logic เอง แล้วเราให้ส่วนอื่น ๆ มา implement interface ไป "
            "จากนั้นเราก็ทำ Dependency Injection คือส่ง instance ของ database และอื่น ๆ ที่ implement มาจาก interface "
            "ของเรา เข้าไปให้ domain logic เรียกใช้"
        ),
        Paragraph(
            "เท่านี้ domain logic ก็ไม่จำเป็นต้อง import หรือมี dependency "
            "ไปหาส่วนอื่น ๆ แล้ว "
        ),
        Paragraph(
            "แต่ก็ต้องระวัง เพราะ Clean Architecture มันก็ทำได้หลายแบบ เช่นเราอยากให้ domain logic ของเรา clean "
            "มากที่สุด ก็สามารถทำได้ โดยการใช้ DTOs มาล้อม domain logic เอาไว้ทั้งหมด ทั้ง input และ output "
            "และภายในส่วนของ domain logic ก็ต้องไม่ใช้ library หรือ framework ภายนอกใด ๆ เลย ต้องเขียนเองทั้งหมด "
            "ซึ่งมันก็ดีในมุมที่ว่า logic ของเราจะไม่ขึ้นกับ library ที่ใช้ เวลาเราจะเปลี่ยน ก็เปลี่ยนได้ง่าย "
            "แต่ก็จะเหนื่อยหน่อยนะครับ ก็ต้องพิจารณาดู ว่าคุ้มกันหรือเปล่า"
        ),
        Paragraph(
            "ส่วนตัวมองว่า เบื้องต้นเรา focus ที่การแยกส่วนของ domain logic ออกจาก API และ database "
            "ได้ก็คิดว่าเพียงพอแล้วครับ "
        ),

        Paragraph(
            'สำหรับรายละเอียดเพิ่มเติม แนะนำให้ลองอ่าน blog Clean Coder จาก <b>Robert C. Martin</b> ผู้คิดค้น Clean '
            'Architecture เองได้เลยครับ: <a href="https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean'
            '-architecture.html" rel="noopener noreferrer" target="_blank">Clean Coder</a>'
        )
    ],
)
