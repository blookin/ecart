import cv2
from pyzbar.pyzbar import decode
import sqlite3

# Initialize the SQLite database
conn = sqlite3.connect('item_database.db')
cursor = conn.cursor()

# Create the 'items' table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS items (
        barcode TEXT PRIMARY KEY,
        name TEXT,
        price REAL,
        quantity INTEGER
    )
''')
conn.commit()

def scan_and_insert_item():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        decoded_objects = decode(frame)

        for obj in decoded_objects:
            barcode = obj.data.decode('utf-8')
            item_info = input_item_info(barcode)

            if item_info:
                print(f"Scanned Barcode: {barcode}")
                print(f"Item Name: {item_info[0]}")
                print(f"Item Price: ${item_info[1]}")
                print(f"Item Quantity: {item_info[2]}")
                insert_item(barcode, *item_info)
            else:
                print(f"Scanned Barcode: {barcode}")
                print("Item not found in the database")

        cv2.imshow('Barcode Scanner', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def input_item_info(barcode):
    name = input(f"Enter the name for the item with barcode {barcode}: ")
    price = float(input(f"Enter the price for the item with barcode {barcode}: "))
    quantity = int(input(f"Enter the quantity for the item with barcode {barcode}: "))
    return name, price, quantity

def insert_item(barcode, name, price, quantity):
    cursor.execute('INSERT INTO items (barcode, name, price, quantity) VALUES (?, ?, ?, ?)', (barcode, name, price, quantity))
    conn.commit()
    print(f"Item with barcode {barcode} inserted into the database.")

if __name__ == '__main__':
    scan_and_insert_item()
