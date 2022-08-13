from content.advice import Advice, Paragraph
from content.advice._base import YoutubeVideo

ddd_for_communication = Advice(
    id_="62f729905a581921677ea1a0",
    title="Domain-Driven Design เขียนโค้ดให้เหมือนเวลาคุยกัน",
    title_url="Domain_Driven_Design_เขียนโค้ดให้เหมือนเวลาคุยกัน",
    short_description="เวลาเราเจอแนวคิดที่เข้าใจยาก หรือไม่คุ้นเคย โดยธรรมชาติ "
                      "เราจะพยายามนิยามมันขึ้นมาใหม่ในแบบของเรา ให้ตัวเราเข้าใจได้ "
                      "ซึ่งปัญหาจะเกิดขึ้น เวลาที่เราเอาแนวคิดที่เราคิดไปคุยกับคนอื่น ก็จะเข้าใจกันได้ลำบาก "
                      "ต้องแปลแนวคิดกลับไปกลับมา ลองทำความเข้าใจกับ Domain-Driven Design กันดู!",
    content=[
        Paragraph(
            "Domain-Driven Design เป็นแนวคิดการออกแบบ software ที่ต้องการให้ \"ทุกคน\" สื่อสารและเข้าใจได้ตรงกัน "
            "พูด \"ภาษา\" เดียวกัน โดย \"ทุกคน\" หมายถึง ไม่ใช่แค่ engineer แต่รวมทั้ง Product Manager, ฝ่าย Sales, "
            "หรือแม้แต่ลูกค้าก็ตาม!"
        ),
        Paragraph(
            "ทำไมเราถึงต้องให้คนอื่นมาเข้าใจโค้ดเราด้วย? จริง ๆ ไม่ต้องถึงกับเข้าใจโค้ด 100% ก็ได้ "
            "แค่เราให้มุมมองของเราเหมือนกับมุมมองของฝ่าย business เช่นถ้าฝ่าย business เรียกสิ่งนี้ว่า Cart "
            "ในโค้ดเราก็ควรจะเขียนว่า Cart เหมือนกัน (อันนี้แค่ตัวอย่างง่าย) เพราะหลาย ๆ "
            "ครั้งที่โค้ดมันอ่านไม่รู้เรื่อง อาจจะเป็นเพราะว่า engineer คนนั้นที่เขียน เขาใช้คำที่เขาคิดขึ้นมาเอง "
            "ไม่มีใครเข้าใจกับเขา หรือ model โครงสร้างของข้อมูล ในแบบที่ไม่สอดคล้องกับความรู้ของฝั่ง business "
            "พอผ่านไปนาน ๆ ก็ลืมแล้วก็กลายเป็นโค้ดที่ไม่มีใครเข้าใจไปในที่สุด เป็นเรื่องธรรมดา"
        ),
        Paragraph(
            "เพราะฉะนั้นการออกแบบตามแบบของ DDD ต้องอาศัยความร่วมมือจากทุกคนใน project ทั้ง engineer, "
            "business, หรือแม้แต่ลูกค้าด้วยซ้ำ ซึ่งก็เป็นแนวทางที่สอดคล้องกับแนวทางของ agile และ lean startup "
            "อยู่แล้ว (น่าเศร้าที่บริษัทไทยหลาย ๆ ที่ไม่ให้ความสำคัญ "
            "หรือไม่ก็ใหญ่ต้วมเตี้ยมจนเปลี่ยนอะไรก็ยากไปซะแล้ว; แล้วบริษัทคุณล่ะ?) "
        ),
        Paragraph(
            "เพิ่มเติมให้อีกหน่อย DDD มีแนวคิดอย่างหนึ่งที่ทรงพลังมาก ๆ นั่นคือ <b>Bounded Context</b> "
            "ในงานจริงเราจะพบว่าการทำ \"โค้ดให้เหมือนกับแนวคิดของ business\" มันเป็นไปไม่ได้ เพราะว่า "
            "แนวคิดของ business เองมันก็อาจจะไม่สอดคล้องกัน เช่นในแนวคิด business ของฝ่าย Sales กับฝ่ายบัญชี "
            "อาจจะมีสิ่งที่เรียกว่า <i>Order</i> เหมือนกันแต่ความหมายอาจจะเป็นคนละอย่าง "
            "พฤติกรรมของ Order สำหรับฝ่าย Sales กับฝ่ายบัญชีก็ต่างกัน ไม่ควรจะเอามารวมกันเป็น Order เดียวกัน"
            "เราจึงใช้แนวคิดของ Bounded Context เพื่อแบ่งของภาษาที่เราใช้ ในงานแต่ละส่วน ไม่ให้มาชนกัน "
            "ขออธิบายแค่คร่าว ๆ ประมาณนี้ครับ"
        ),
        Paragraph(
            "ขอแนะนำคลิปของคุณ <b>Eric Evans</b> ผู้คิดค้น Domain-Driven Design เอง "
            "โดยคลิปนี้เป็นคลิปที่ทำให้ผมสนใจและเริ่มศึกษา Domain-Driven Design ด้วยเช่นกัน"
        ),
        YoutubeVideo("pMuiVlnGqjk"),
        Paragraph(
            "และก็ขอแนะนำ Series \"ออกแบบ microservices ด้วย Domain-Driven Design\" "
            "โดย ผมเอง Copy Paste Engineer ซึ่งอาจจะเล่าได้ไม่สนุกและลึกซึ้งเท่าคุณ Eric Evans "
            "แต่ก็หวังว่าจะเป็นประโยชน์นะครับ"
        ),
        YoutubeVideo("bRTCWUtavBs"),
    ]
)