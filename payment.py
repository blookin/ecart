import tkinter as tk
from PIL import Image, ImageTk

def display_qr_code():
    # Open the QR code image
    qr_image_path = "path_to_your_qr_code_image.png"  # Replace this with the path to your QR code image
    qr_image = Image.open(qr_image_path)

    # Create a Tkinter window
    root = tk.Tk()
    root.title("QR Code Display")

    # Convert the image for displaying in Tkinter
    qr_image_tk = ImageTk.PhotoImage(qr_image)

    # Display the QR code image
    label = tk.Label(root, image=qr_image_tk)
    label.pack()

    root.mainloop()

# Call the function to display the QR code
display_qr_code()
