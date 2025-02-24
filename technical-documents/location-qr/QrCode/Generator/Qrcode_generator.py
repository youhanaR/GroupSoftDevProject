"""
QR Code Generator

This script generates a QR code from user-provided input and then decodes it to retrieve the original content.

Workflow:
1. Sets up the necessary dynamic library path (specific to macOS with Homebrew).
2. Imports required libraries:
   - 'qrcode' for generating QR codes.
   - 'pyzbar' from 'pyzbar' for decoding QR codes.
   - 'PIL' (Pillow) for image processing.
3. Prompts the user to input the content that will be encoded into a QR code.
4. Generates the QR code and saves it as an image file ("myqr.png").
5. Opens the saved image, converts it to grayscale, and decodes the QR code.
6. Prints the decoded content if successful, otherwise notifies that no QR code was found.

Dependencies:
- qrcode
- pyzbar
- Pillow

"""



import os
os.environ["DYLD_LIBRARY_PATH"] = "/opt/homebrew/lib"

import qrcode  
from pyzbar.pyzbar import decode
from PIL import Image

# Prompt the user to enter the content for the QR code
qr_content = input("Enter the content for the QR code: ")

# Generate the QR code
myqr = qrcode.make(qr_content)
myqr.save("myqr.png")

# Open the generated QR code image
qr_image = Image.open("myqr.png").convert('L')  

# Decode the QR code
decoded_data = decode(qr_image)

# Check if QR code is decoded successfully and print the content
if decoded_data:
    print(decoded_data[0].data.decode("ascii"))
else:
    print("No QR code found.")
