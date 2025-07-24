def webp_to_png(path):
    from PIL import Image

    # Check if the file has a .webp extension (case-insensitive)
    if not path.lower().endswith(".webp"):
        print("Error: File is not a .webp image.")
        return

    try:
        # Open the image file using Pillow
        img = Image.open(path)
        # Create new file path by replacing the .webp extension with .png
        new_path = path[:-5] + ".png"
        # Save the image as PNG format
        img.save(new_path, "PNG")
        print(f"Converted image saved as: {new_path}")
    except Exception as e:
        # Catch and print any error that occurs during opening/saving
        print("Error:", e)

print("What conversion are you trying to make?")
print("1 = webp → png")

print("Paste filepath of the image here:")
path = input()

# Call the conversion function with the user-provided path
webp_to_png(path)
