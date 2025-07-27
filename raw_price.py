DATABASE = 'market_data.db'
import random
import sqlite3
conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()
def size_of_table():
    cursor.execute(f"SELECT COUNT(*) FROM raw_materials")
    return cursor.fetchone()[0]


for i in range(1,size_of_table()+1):
    cursor.execute('''SELECT name, unit_of_measurement, raw_price FROM raw_materials WHERE material_id = ?''', (i,))
    material = cursor.fetchone()
    name = material[0]
    unit = material[1]
    price = material[2]
    lw = price + price * (random.randint(-10,10) /100)
    l2w = lw + lw * (random.randint(-10,10) /100)
    l3w = l2w + l2w * (random.randint(-10,10) /100)
    cursor.execute('''UPDATE raw_materials SET last_week =?, last2_week=?, last3_week = ? WHERE material_id = ?''',(lw,l2w,l3w,i))
    conn.commit()

conn.close()