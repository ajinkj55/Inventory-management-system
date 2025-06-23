import mysql.connector

# Database connection
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root123",
        database="Inventorydb"
    )
    

# Add a new product
def add_product(name, quantity, price):
    conn = connect_to_database()
    cursor = conn.cursor()
    query = "INSERT INTO products (product_name, quantity, price) VALUES (%s, %s, %s)"
    values = (name, quantity, price)
    cursor.execute(query, values)
    conn.commit()
    print(f"Product '{name}' added successfully!")
    cursor.close()
    conn.close()

# Delete a product
def delete_product(product_id):
    conn = connect_to_database()
    cursor = conn.cursor()
    query = "DELETE FROM products WHERE product_id = %s"
    cursor.execute(query, (product_id,))
    conn.commit()
    print(f"Product with ID {product_id} deleted successfully!")
    cursor.close()
    conn.close()

# Update product quantity
def update_quantity(product_id, new_quantity):
    conn = connect_to_database()
    cursor = conn.cursor()
    query = "UPDATE products SET quantity = %s WHERE product_id = %s"
    cursor.execute(query, (new_quantity, product_id))
    conn.commit()
    print(f"Quantity for product ID {product_id} updated to {new_quantity}!")
    cursor.close()
    conn.close()

# View available stock
def view_stock():
    conn = connect_to_database()
    cursor = conn.cursor()
    query = "SELECT * FROM products"
    cursor.execute(query)
    results = cursor.fetchall()
    print("\nAvailable Stock:")
    for row in results:
        print(f"ID: {row[0]}, Name: {row[1]}, Quantity: {row[2]}, Price: ${row[3]}")
    cursor.close()
    conn.close()

# Main menu
def main():
    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. Delete Product")
        print("3. Update Product Quantity")
        print("4. View Available Stock")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter product name: ")
            quantity = int(input("Enter product quantity: "))
            price = float(input("Enter product price: "))
            add_product(name, quantity, price)
        elif choice == '2':
            product_id = int(input("Enter product ID to delete: "))
            delete_product(product_id)
        elif choice == '3':
            product_id = int(input("Enter product ID to update: "))
            new_quantity = int(input("Enter new quantity: "))
            update_quantity(product_id, new_quantity)
        elif choice == '4':
            view_stock()
        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
