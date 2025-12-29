import json
import gzip # <--- เพิ่มตัวนี้
import requests
from bs4 import BeautifulSoup

# รายชื่อเว็บที่จะ Index (ใส่เพิ่มได้ไม่จำกัด)
database = []

# 🔥 โหลดรายการเว็บจากไฟล์ sites.txt (ใส่กี่เว็บก็ได้ ไม่จำกัด)
try:
    with open('sites.txt', 'r', encoding='utf-8') as f:
        urls = [line.strip() for line in f if line.strip()]
    print(f"📂 โหลดเป้าหมายสำเร็จ: {len(urls)} เว็บไซต์")
except FileNotFoundError:
    print("❌ ไม่พบไฟล์ sites.txt! กรุณาสร้างไฟล์นี้และใส่ URL บรรทัดละ 1 เว็บ")
    urls = []

print("🕷️ เริ่มต้นเก็บข้อมูล...")
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

for url in urls:
    try:
        print(f"กำลังอ่าน: {url}")
        # เพิ่ม headers ให้เหมือนคนจริงๆ มากที่สุด
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9',
        }
        response = requests.get(url, headers=headers, timeout=10) # เพิ่ม timeout เป็น 10 วิ
        
        if response.status_code != 200:
            print(f"⚠️ Skip {url}: Status {response.status_code}")
            continue

        response.encoding = 'utf-8' # บังคับ utf-8 ป้องกันภาษาต่างดาว
        soup = BeautifulSoup(response.content, 'html.parser')
        
        title = soup.title.string if soup.title else url
        # ดึงข้อความมาแค่ 500 ตัวอักษรเพื่อเป็นตัวอย่าง
        text = " ".join([p.text for p in soup.find_all('p')])[:500]
        
        database.append({
            "url": url,
            "title": title,
            "snippet": text
        })
    except Exception as e:
        print(f"❌ Error {url}: {e}")

print(f"📦 กำลังบีบอัดข้อมูล {len(database)} รายการ...")

# บันทึกเป็นไฟล์ JSON แบบบีบอัด (GZIP)
with gzip.open("database.json.gz", "wt", encoding="utf-8") as f:
    # separators=(',', ':') คือการลบเว้นวรรคทิ้งทั้งหมดเพื่อให้ไฟล์เล็กสุด
    json.dump(database, f, separators=(',', ':'))

print(f"✅ สร้างไฟล์ 'database.json.gz' สำเร็จ! (บีบอัดเรียบร้อย)")
print("👉 ขั้นตอนต่อไป: อัปโหลดไฟล์นี้ขึ้น archive.org")
