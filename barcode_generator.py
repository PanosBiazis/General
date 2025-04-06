import barcode
from barcode.writer import ImageWriter

def generate_barcode(data, format='code128'):
    # Create a barcode instance
    barcode_class = barcode.get_barcode_class(format)
    barcode_instance = barcode_class(data, writer=ImageWriter())

    # Save the barcode as an image file
    filename = barcode_instance.save('barcode')
    print(f"Barcode generated and saved as '{filename}.png'.")

def main():
    # Get the barcode format from the user
    available_formats = ['code128', 'ean13', 'upc']
    print("Available barcode formats:", ', '.join(available_formats))
    
    while True:
        format_choice = input(f"Enter the barcode format ({', '.join(available_formats)}): ")
        if format_choice in available_formats:
            break
        else:
            print("Invalid format. Please choose from the available formats.")

    # Get the data from the user
    user_input = input("Enter the data to encode in the barcode: ")
    generate_barcode(user_input, format_choice)

if __name__ == "__main__":
    main()
