from db import get_db_connection

def get_products_by_brand(brand):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products WHERE brand = %s", (brand,))
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data

def get_suppliers_by_category(category):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    print(f"🔍 Searching for category: {category}")  # Debugging print

    query = "SELECT * FROM suppliers WHERE LOWER(product_categories) LIKE LOWER(%s)"
    cursor.execute(query, (f"%{category.strip().lower()}%",))  # Case-insensitive search

    data = cursor.fetchall()
    cursor.close()
    conn.close()

    print(f"✅ Found {len(data)} suppliers")  # Debugging print

    return data

print(get_suppliers_by_category("Laptops"))
