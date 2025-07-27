import sqlite3

# Connect to the database
conn = sqlite3.connect('market_data.db')
cursor = conn.cursor()

# Update queries
cursor.execute("""
    UPDATE vendor_ratings
    SET business_type = 'Food Trucks'
    WHERE business_type = 'Food Truck'
""")

cursor.execute("""
    UPDATE vendor_ratings
    SET business_type = 'Small Restaurants'
    WHERE business_type = 'Small Restaurant'
""")

# Commit changes and close connection
conn.commit()
conn.close()

print("Kaam ho gaya bhai. 'Truck' se 'Trucks' aur 'Restaurant' se 'Restaurants' bana diya.")
