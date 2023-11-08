from pyzbar.pyzbar import decode
import cv2

# Sample item database (you can replace this with your own database)
item_database = {
    "123456": {"name": "Product A", "price": 10.0},
    "789012": {"name": "Product B", "price": 15.0},
}

def scan_and_add_item(barcode):
    if barcode in item_database:
        item = item_database[barcode]
        print(f"Item found: {item['name']}, Price: ${item['price']}")
        # Add your logic to add the item to the cart or perform other actions
    else:
        print("Item not found in the database")

def delete_item(barcode):
    if barcode in item_database:
        del item_database[barcode]
        print(f"Item with barcode {barcode} has been deleted.")
    else:
        print("Item not found in the database.")

# Open the camera for barcode scanning
cap = cv2.VideoCapture(0)

pir_activated = False

while True:
    ret, frame = cap.read()

    decoded_objects = decode(frame)

    for obj in decoded_objects:
        barcode = obj.data.decode('utf-8')
        if pir_activated:
            delete_item(barcode)  # Call the function to delete the scanned item
        else:
            scan_and_add_item(barcode)  # Call the function to add the scanned item

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
