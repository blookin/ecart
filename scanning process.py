import cv2
from pyzbar.pyzbar import decode
import sqlite3

def scan_and_display_item_info():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        decoded_objects = decode(frame)

        for obj in decoded_objects:
            barcode = obj.data.decode('utf-8')
            item_info = get_item_info(barcode)

            if item_info:
                print(f"Scanned Barcode: {barcode}")
                print(f"Item Name: {item_info[0]}")
                print(f"Item Price: ${item_info[1]}")
            else:
                print(f"Scanned Barcode: {barcode}")
                print("Item not found in the database")

        cv2.imshow('Barcode Scanner', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def get_item_info(barcode):
    conn = sqlite3.connect('item_database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name, price FROM items WHERE barcode = ?', (barcode,))
    item_info = cursor.fetchone()
    conn.close()
    return item_info

if __name__ == '__main__':
    scan_and_display_item_info()
