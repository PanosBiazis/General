#!/usr/bin/env python3
import subprocess
import sys
import io
from PIL import Image
import pytesseract

def capture_screenshot():
    """
    Uses Flameshot to capture a screenshot interactively.
    The '-r' flag outputs the image data (PNG) to stdout.
    """
    try:
        result = subprocess.run(
            ["flameshot", "gui", "-r"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True
        )
    except subprocess.CalledProcessError as e:
        print("Error capturing screenshot:", e.stderr.decode())
        sys.exit(1)
    return result.stdout

def perform_ocr(image_data):
    """
    Opens the image from the given bytes and performs OCR using Tesseract.
    Returns the recognized text.
    """
    try:
        image = Image.open(io.BytesIO(image_data))
    except Exception as e:
        print("Error reading image data:", e)
        sys.exit(1)
    # Use pytesseract to extract text from the image
    text = pytesseract.image_to_string(image)
    return text

def main():
    print("Please select an area using Flameshot...")
    image_data = capture_screenshot()
    if not image_data:
        print("No image data captured. Exiting.")
        sys.exit(1)
    text = perform_ocr(image_data)
    print("\n--- Recognized Text ---")
    print(text)

if __name__ == "__main__":
    main()
