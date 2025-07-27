import sqlite3
import random
import string
from datetime import datetime, timedelta

# Connect to DB
conn = sqlite3.connect('market_data.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS vendor_ratings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    location TEXT,
    verification_status TEXT,
    overall_rating REAL,
    monthly_revenue REAL,
    monthly_profit REAL,
    business_type TEXT,
    payment_score REAL,
    reliability_score REAL,
    communication_score REAL,
    order_volume_score REAL,
    avg_payment_buffertime INTEGER,
    orders_per_month INTEGER,
    phone_number TEXT,
    credit_limit REAL,
    partner_since TEXT
)
''')

# Static options
locations = ['Mumbai', 'Delhi', 'Chennai', 'Kolkata', 'Bangalore', 'Hyderabad', 'Pune', 'Ahmedabad', 'Lucknow', 'Bhopal']
business_types = ['Street Food Stall', 'Small Restaurant', 'Food Truck', 'Catering Services']
verification_statuses = ['Verified', 'Pending', 'New Vendor', 'Unverified']

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
business_suffixes = [
    "Logistics", "Suppliers", "Vendors", "Traders", "Distributors", "Wholesalers", "Food Services",
    "Procurement", "Sourcing", "Retailers", "Kirana Services", "Material Co.", "Commodities", "Farm Connect", "Raw Foods",
    "Warehouse Ops", "Cold Storage", "Agro Traders", "B2B Mart", "Ingredient Co.", "Bulk Buyers"
]
def generate_vendor_name():
    return f"{random.choice(first_names)} {random.choice(middle_names)} {random.choice(last_names)} {random.choice(business_suffixes)}"



def random_phone():
    return '9' + ''.join(random.choices(string.digits, k=9))

def random_date():
    start_date = datetime(2015, 1, 1)
    random_days = random.randint(0, 365*9)
    return (start_date + timedelta(days=random_days)).strftime('%Y-%m-%d')

# Insert 200 vendors
for _ in range(200):
    name = generate_vendor_name()
    location = random.choice(locations)
    verification_status = random.choice(verification_statuses)
    overall_rating = round(random.uniform(2.5, 5.0), 2)
    revenue = round(random.uniform(50000, 500000), 2)
    profit = round(revenue * random.uniform(0.1, 0.4), 2)
    business_type = random.choice(business_types)
    payment_score = round(random.uniform(1.0, 5.0), 2)
    reliability_score = round(random.uniform(1.0, 5.0), 2)
    communication_score = round(random.uniform(1.0, 5.0), 2)
    order_volume_score = round(random.uniform(1.0, 5.0), 2)
    avg_buffertime = random.randint(1, 10)  # in days
    orders_per_month = random.randint(10, 500)
    phone_number = random_phone()
    credit_limit = round(random.uniform(5000, 50000), 2)
    partner_since = random_date()

    cursor.execute('''
        INSERT INTO vendor_ratings (
            name, location, verification_status, overall_rating, monthly_revenue,
            monthly_profit, business_type, payment_score, reliability_score,
            communication_score, order_volume_score, avg_payment_buffertime,
            orders_per_month, phone_number, credit_limit, partner_since
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        name, location, verification_status, overall_rating, revenue, profit,
        business_type, payment_score, reliability_score, communication_score,
        order_volume_score, avg_buffertime, orders_per_month, phone_number,
        credit_limit, partner_since
    ))

# Commit & Close
conn.commit()
conn.close()
print("🎉 200 vendor entries inserted into market_data.db successfully.")
