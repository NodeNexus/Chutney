import sqlite3
import random
import string

# Connect to DB
conn = sqlite3.connect('market_data.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS suppliers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    category TEXT,
    location TEXT,
    verification_status TEXT,
    overall_rating REAL,
    num_reviews INTEGER,
    price_range TEXT,
    quality_score INTEGER,
    reliability_score INTEGER,
    satisfaction_score INTEGER,
    avg_delivery_days INTEGER,
    min_order_cost REAL,
    phone TEXT,
    email TEXT
)
''')

# Static Lists
categories = ['Vegetables', 'Grains & Cereals', 'Dairy Products', 'Spices & Condiments', 'Meat & Poultry']
locations = ['Mumbai', 'Bangalore', 'Delhi', 'Pune']
verification_statuses = ['Verified', 'Pending', 'New Supplier', 'Unverified']

first_names = [
    "Aarav", "Ishaan", "Kavya", "Tara", "Dev", "Mira", "Riya", "Rohan", "Aryan", "Diya",
    "Yash", "Anaya", "Vivaan", "Nina", "Kabir", "Aanya", "Aditya", "Kiara", "Samar", "Ira",
    "Arjun", "Meera", "Reyansh", "Jiya", "Naman", "Sanvi", "Veer", "Avni", "Hriday", "Sia",
    "Rudra", "Tisha", "Ishita", "Neil", "Niharika", "Shaurya", "Swara", "Kian", "Myra", "Ayaan",
    "Anvi", "Daksh", "Aarohi", "Krishna", "Navya", "Manav", "Zoya", "Raghav", "Trisha", "Parth", "Prisha",
    "Shivansh", "Lavanya", "Ayansh", "Charvi", "Yuvaan", "Anushka", "Atharv", "Amaira", "Arnav", "Sara",
    "Viraj", "Mahira", "Om", "Aleeza", "Tanay", "Inaaya", "Kabira", "Simran", "Hardik", "Jhanvi",
    "Pranav", "Sanya", "Kartik", "Sneha", "Tanish", "Bhavna", "Rajat", "Neha", "Siddharth", "Isha",
    "Varun", "Vani", "Lakshya", "Pihu", "Ansh", "Chhavi", "Ahaan", "Alisha", "Raj", "Nitya",
    "Abhay", "Aadhya", "Jatin", "Kripa", "Vihaan", "Radha", "Saket", "Diya", "Rishi", "Shreya",
]
middle_names = [
    "Fresh", "Prime", "Organic", "Choice", "Select", "Pure", "Urban", "Elite", "Gold", "Smart",
    "Daily", "True", "Green", "Happy", "Spicy", "Bold", "Royal", "Shudh", "Fast", "Tandoor",
    "Swad", "Herbal", "Healthy", "Super", "Magic", "Power", "Dilli", "Biryani", "Masala", "Khaas",
    "Bazaar", "Mandai", "Local", "Apna", "Desi", "Zayka", "Taste", "Fast", "Top", "Budget",
    "Mithas", "Anaj", "Kirana", "Bazaar", "Cart", "Depot", "Express", "Foods", "Khaana", "Utsav",
    "Quick", "Taza", "Zaika", "Mezbaan", "Tandoori", "Anmol", "Sheher", "Quality", "Swaad", "No.1",
]
last_names = [
    "Enterprises", "Traders", "Foods", "Distributors", "Depot", "Brothers", "Sons", "Group", "Mart", "Bazaar",
    "Centre", "Grocery", "Hub", "Store", "House", "Outlet", "Point", "Mandi", "Bhandar", "Supplies",
    "Wholesale", "Retail", "Corner", "Kitchen", "Factory", "Mill", "Nationals", "Mandir", "Express", "Dukaan",
    "Collection", "Network", "Associates", "World", "Nivas", "Trunk", "Pvt Ltd", "Company", "Industries", "Heights",
    "Nagar", "Farm", "Lane", "Plaza", "Gali", "Chowk", "Services", "Cottage", "Udyog", "Gram",
    "Foods Co", "Supermart", "Market", "Deals", "Outlets", "Chain", "Mini Mart", "Corner Store", "India Ltd", "Traders Ltd",
]
suffixes = [
    "Logistics", "Suppliers", "Vendors", "Traders", "Distributors", "Wholesalers", "Food Services",
    "Procurement", "Sourcing", "Retailers", "Kirana Services", "Material Co.", "Commodities", "Farm Connect", "Raw Foods",
    "Warehouse Ops", "Cold Storage", "Agro Traders", "B2B Mart", "Ingredient Co.", "Bulk Buyers"
]

# Helpers
def gen_name():
    return f"{random.choice(first_names)} {random.choice(middle_names)} {random.choice(last_names)} {random.choice(suffixes)}"

def gen_email(name):
    slug = name.lower().replace(" ", "").replace("&", "and").replace(".", "")
    return f"{slug[:15]}@supplier.in"

def gen_price_range():
    low = random.randint(10, 30)
    high = low + random.randint(10, 30)
    return f"₹{low}-{high}/kg"

def gen_phone():
    return '9' + ''.join(random.choices(string.digits, k=9))

# Generate 200 fake suppliers
for _ in range(200):
    name = gen_name()
    category = random.choice(categories)
    location = random.choice(locations)
    verification = random.choice(verification_statuses)
    rating = round(random.uniform(2.5, 5.0), 1)
    reviews = random.randint(10, 500)
    price_range = gen_price_range()
    quality = random.randint(60, 100)
    reliability = random.randint(60, 100)
    satisfaction = random.randint(60, 100)
    delivery = random.randint(1, 10)
    min_order_cost = round(random.uniform(500, 5000), 2)
    phone = gen_phone()
    email = gen_email(name)

    cursor.execute('''
        INSERT INTO suppliers (
            name, category, location, verification_status, overall_rating,
            num_reviews, price_range, quality_score, reliability_score,
            satisfaction_score, avg_delivery_days, min_order_cost, phone, email
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        name, category, location, verification, rating, reviews, price_range,
        quality, reliability, satisfaction, delivery, min_order_cost, phone, email
    ))

conn.commit()
conn.close()
print("✅ Supplier data created successfully.")
