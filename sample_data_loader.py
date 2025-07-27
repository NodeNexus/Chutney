import sqlite3
import os  
import json


def bulk_add_raw_materials():
    items = [
        # Vegetables
        ('Cabbage', 'Vegetables', 'kg', 'Fresh green cabbage'),
        ('Carrot', 'Vegetables', 'kg', 'Crunchy carrots'),
        ('Green Chilli', 'Vegetables', 'kg', 'Hot green chillies'),
        ('Potato', 'Vegetables', 'kg', 'Starchy potatoes'),
        ('Onion', 'Vegetables', 'kg', 'Pungent onions'),
        ('Tomato', 'Vegetables', 'kg', 'Juicy tomatoes'),
        ('Cauliflower', 'Vegetables', 'kg', 'Snow-white cauliflower'),
        ('Spinach', 'Vegetables', 'bundle', 'Fresh spinach leaves'),
        ('Capsicum', 'Vegetables', 'kg', 'Bell peppers in all colours'),
        ('Brinjal', 'Vegetables', 'kg', 'Purple eggplants'),

        # Spices
        ('Garlic', 'Spices', 'kg', 'Strong aroma garlic'),
        ('Ginger', 'Spices', 'kg', 'Zesty ginger roots'),
        ('Turmeric', 'Spices', 'kg', 'Ground turmeric powder'),
        ('Red Chilli Powder', 'Spices', 'kg', 'Fiery red powder'),
        ('Cumin Seeds', 'Spices', 'kg', 'Earthy cumin seeds'),
        ('Mustard Seeds', 'Spices', 'kg', 'Tiny black mustard'),
        ('Coriander Powder', 'Spices', 'kg', 'Aromatic dhaniya powder'),
        ('Garam Masala', 'Spices', 'kg', 'Blend of powerful masalas'),
        ('Fenugreek Seeds', 'Spices', 'kg', 'Bitter methi dana'),
        ('Asafoetida', 'Spices', 'g', 'Strong hing powder'),

        # Dairy
        ('Milk', 'Dairy', 'litre', 'Full-cream milk'),
        ('Paneer', 'Dairy', 'kg', 'Cottage cheese'),
        ('Curd', 'Dairy', 'kg', 'Thick homemade dahi'),
        ('Butter', 'Dairy', 'kg', 'Amul ka butter'),
        ('Cheese', 'Dairy', 'kg', 'Mozzarella/processed cheese'),

        # Staples
        ('Sugar', 'Staples', 'kg', 'Granulated sugar'),
        ('Salt', 'Staples', 'kg', 'Iodized table salt'),
        ('Wheat Flour', 'Staples', 'kg', 'Whole wheat atta'),
        ('Rice', 'Staples', 'kg', 'Long grain basmati'),
        ('Pulses', 'Staples', 'kg', 'Mixed dals - arhar, moong, chana'),
        ('Maida', 'Staples', 'kg', 'Refined white flour'),
        ('Poha', 'Staples', 'kg', 'Flattened rice'),
        ('Suji', 'Staples', 'kg', 'Semolina for halwa/idli'),
        ('Besan', 'Staples', 'kg', 'Gram flour'),
        ('Cooking Oil', 'Staples', 'litre', 'Refined sunflower/mustard oil'),

        # Leaves/Herbs
        ('Coriander', 'Leaves', 'bundle', 'Fresh coriander leaves'),
        ('Mint', 'Leaves', 'bundle', 'Cool pudina leaves'),
        ('Curry Leaves', 'Leaves', 'bundle', 'Fragrant curry patta'),

        # Condiments
        ('Pickle', 'Condiments', 'kg', 'Spicy mango or lemon pickle'),
        ('Ketchup', 'Condiments', 'litre', 'Tomato ketchup bottle'),
        ('Vinegar', 'Condiments', 'litre', 'Synthetic vinegar'),
        ('Soya Sauce', 'Condiments', 'litre', 'Dark Chinese flavour'),

        # Bakery / Packaged
        ('Bread', 'Bakery', 'pack', 'White or brown bread loaf'),
        ('Buns', 'Bakery', 'pack', 'Pav buns for vada pav'),
        ('Biscuits', 'Bakery', 'pack', 'Parle-G ya Marie'),
        ('Noodles', 'Packaged', 'pack', 'Instant noodles packet'),
        ('Cornflakes', 'Packaged', 'pack', 'Breakfast cereal'),

        # Others
        ('Tea Leaves', 'Beverages', 'kg', 'Strong chai patti'),
        ('Coffee', 'Beverages', 'kg', 'Instant coffee powder'),
        ('Ice Cubes', 'Frozen', 'kg', 'Crushed or block ice'),
        ('Lemon', 'Vegetables', 'kg', 'Juicy yellow lemons'),
        ('Green Peas', 'Frozen', 'kg', 'Frozen matar'),
    ]

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.executemany('''
        INSERT INTO raw_materials (name, category, unit_of_measurement, description)
        VALUES (?, ?, ?, ?)
    ''', items)
    conn.commit()
    conn.close()


def bulk_add_regions():
    regions = [
        ('Pune', 'Maharashtra', json.dumps(['Shivaji Market', 'Mandai'])),
        ('Hyderabad', 'Telangana', json.dumps(['Bowenpally Market'])),
        ('Kolkata', 'West Bengal', json.dumps(['Sealdah', 'Koley Market'])),
        ('Ahmedabad', 'Gujarat', json.dumps(['Jamalpur Market'])),
        ('Chennai', 'Tamil Nadu', json.dumps(['Koyambedu Market'])),
        ('Delhi', 'Delhi', json.dumps(['Azadpur Mandi', 'Ghanta Ghar Market'])),
        ('Bengaluru', 'Karnataka', json.dumps(['KR Market', 'Yeshwanthpur Market'])),
        ('Mumbai', 'Maharashtra', json.dumps(['Crawford Market', 'Vashi APMC'])),
        ('Lucknow', 'Uttar Pradesh', json.dumps(['Chowk Market', 'Dubagga Mandi'])),
        ('Indore', 'Madhya Pradesh', json.dumps(['Rajkumar Market', 'Chhawani Mandi'])),
    ]

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.executemany('''
        INSERT INTO market_regions (region_name, state, major_markets)
        VALUES (?, ?, ?)
    ''', regions)
    conn.commit()
    conn.close()

import random
from datetime import datetime, timedelta

def generate_market_data(days=90):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    cursor.execute("SELECT material_id FROM raw_materials")
    material_ids = [row[0] for row in cursor.fetchall()]
    
    cursor.execute("SELECT region_id FROM market_regions")
    region_ids = [row[0] for row in cursor.fetchall()]
    
    today = datetime.today()

    for day_offset in range(days):
        date = (today - timedelta(days=day_offset)).strftime("%Y-%m-%d")
        for mat_id in material_ids:
            for reg_id in region_ids:
                avg = random.uniform(10, 100)
                minp = round(avg * 0.85, 2)
                maxp = round(avg * 1.15, 2)
                avail = random.randint(60, 100)
                grade_a = random.randint(50, 80)
                grade_b = 100 - grade_a - random.randint(5, 15)
                grade_c = 100 - grade_a - grade_b
                stock = random.choice(['low', 'medium', 'high'])
                suppliers = random.randint(2, 10)

                cursor.execute('''
                    INSERT INTO daily_market_data (
                        material_id, region_id, date,
                        avg_price, min_price, max_price,
                        availability_percentage, 
                        quality_grade_a_percent, quality_grade_b_percent, quality_grade_c_percent,
                        stock_level, supplier_count
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    mat_id, reg_id, date, avg, minp, maxp, avail,
                    grade_a, grade_b, grade_c, stock, suppliers
                ))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    DATABASE = 'market_data.db'
    bulk_add_raw_materials()
    bulk_add_regions()
    generate_market_data(days=90)