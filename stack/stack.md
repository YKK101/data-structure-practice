# Stack Specification

📝 วิธีการจัดเก็บข้อมูล โดยข้อมูลที่เข้ามาทีหลัง จะถูกเรียกใช้ก่อนเสมอ (Last In First Out : `LIFO`)

## Attributes
- `size: int` ระบุจำนวนของข้อมูลทั้งหมดที่ถูกเก็บอยู่ใน stack
- `list: Array` array ของข้อมูลทั้งหมดใน stack

## Method
- `count(): int` คืนจำนวนข้อมูลทั้งหมดที่ถูกเก็บอยู่ใน stack
- `peek(): object` แสดงค่าของ object ที่อยู่บนสุดของ stack และจะถูกเรียกใช้เป็นตัวถัดไป
- `push(object): void` เพิ่มข้อมูลใหม่เข้าไปยัง stack
- `pop(): object` ดึงข้อมูลตัวบนสุดออกมาจาก stack