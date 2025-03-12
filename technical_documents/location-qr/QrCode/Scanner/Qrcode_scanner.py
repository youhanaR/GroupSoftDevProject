"""
QR Code Scanner using OpenCV and Pyzbar

This script captures video from the default webcam and continuously scans each frame for QR codes.
When a QR code is detected, the script prints its type and decoded content, then pauses for 6 seconds 
before continuing to scan. The video feed is displayed in a window titled "Qr_Code_Scanner", and the 
program can be exited by pressing the 'q' key.

Workflow:
1. Set the environment variable for dynamic libraries (specific to macOS with Homebrew).
2. Import required libraries:
   - OpenCV (cv2) for video capture and image processing.
   - pyzbar for decoding QR codes from image frames.
   - time for pausing between scans.
3. Initialize the webcam capture and set the resolution.
4. Enter an infinite loop to continuously:
   - Capture a frame from the webcam.
   - Decode any QR codes found in the frame and print their type and data.
   - Display the frame in a window.
   - Pause for 6 seconds after detecting a QR code.
5. Exit the loop and clean up resources when the user presses the 'q' key.

Dependencies:
- OpenCV
- pyzbar
- time

@author Jood Alrubian
"""


import os
os.environ["DYLD_LIBRARY_PATH"] = "/opt/homebrew/lib"

import cv2  
from pyzbar.pyzbar import decode  
import time 

# Initialize the webcam (device 0)
cam = cv2.VideoCapture(0)

# Set the resolution of the captured video
cam.set(3, 640)  # Width
cam.set(4, 480)  # Height

while True:
    # Capture a frame from the webcam
    success, frame = cam.read()  

   # Decode any QR codes present in the frame
    for barcode in decode(frame):
        print(barcode.type)  
        print(barcode.data.decode('utf-8'))  
        time.sleep(6)  # Pause for 6 seconds after a QR code is detected
    
    # Display the video frame in a window titled "Qr_Code_Scanner"
    cv2.imshow("Qr_Code_Scanner", frame)

   # Exit the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cam.release()

cv2.destroyAllWindows()
