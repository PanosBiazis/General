import qrcode

def generate_qr_code(data, version):
    # Create a QR code instance with the specified version
    qr = qrcode.QRCode(
        version=version,  # controls the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # error correction level
        box_size=10,  # size of each box in pixels
        border=4,  # thickness of the border (minimum is 4)
    )
    
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image
    img.save("qr_code.png")
    print("QR code generated and saved as 'qr_code.png'.")

def main():
    # Get the version from the user
    while True:
        try:
            version = int(input("Enter the QR code version (1-40): "))
            if 1 <= version <= 40:
                break
            else:
                print("Please enter a number between 1 and 40.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Get the data from the user
    user_input = input("Enter the data to encode in the QR code: ")
    generate_qr_code(user_input, version)

if __name__ == "__main__":
    main()
