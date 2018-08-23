# Queue Specification

📝 วิธีการจัดเก็บข้อมูล โดยข้อมูลที่เข้ามาก่อน จะถูกเรียกใช้ก่อนเสมอ (First In First Out : `FIFO`)

## Attributes
- `size: int` ระบุจำนวนของข้อมูลทั้งหมดที่ถูกเก็บอยู่ใน queue
- `first: LinkedNode` node แรกสุด ซึ่งเริ่มชี้ไปยังข้อมูลตัวแรกใน queue
- `last: LinkedNode` node สุดท้าย ใช้เก็บข้อมูลล่าสุดที่ถูกเพิ่มเข้ามาใน queue เพื่อให้สามารถเพิ่มข้อมูลใหม่ต่อท้ายได้ถูกตำแหน่ง

## Methods
- `count(): int` คืนจำนวนข้อมูลทั้งหมดที่ถูกเก็บอยู่ใน queue
- `isEmpty(): boolean` คืนค่าว่า queue นั้นว่างหรือไม่
- `peek(): object` แสดงค่าของ object ที่อยู่หน้าสุดของ queue และจะถูกเรียกใช้เป็นตัวถัดไป
- `enqueue(object): void` เพิ่มข้อมูลใหม่เข้าไปยัง queue
- `dequeue(): object` ดึงข้อมูลตัวหน้าสุดออกมาจาก queue

## Implementation
[Go to queue.py](./queue.py)

---

# LinkedNode Specification

## Attributes
- `element: object` เก็บค่าของ node
- `next: LinkedNode` pointer ชี้ไปยัง node ถัดไป

## Implementation
[Go to linkedNode.py](./linkedNode.py)