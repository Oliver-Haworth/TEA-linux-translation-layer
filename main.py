import os

# Map of file extensions to convert (e.g., legacy or unsupported formats)
file_type_map = {
    ".webp": ".png",
    ".doc": ".docx"
}

# Converts a Windows file path to Linux format
def wfp_to_lfp(wfp):
    drive = wfp[0].lower()  # Get drive letter (e.g., 'C')
    rest = wfp[2:].replace("\\", "/")  # Replace backslashes with slashes
    return f"/mnt/{drive}{rest}"

# Converts a Linux file path to Windows format
def lfp_to_wfp(lfp):
    if lfp.startswith("/mnt/"):
        drive = lfp[5]  # Extract drive letter
        rest = lfp[6:].replace("/", "\\")  # Replace slashes with backslashes
        return f"{drive.upper()}:\\{rest}"
    else:
        return lfp  # Leave unchanged if not a /mnt path

# Translates file extensions based on defined rules
def translate_file_type(filepath):
    base, ext = os.path.splitext(filepath)
    ext = ext.lower()
    return base + file_type_map[ext] if ext in file_type_map else filepath

# Main interaction loop
def main():
    direction = 0
    while direction not in (1, 2):
        print("Convert:")
        print("1 = Windows → Linux")
        print("2 = Linux → Windows")
        direction = input("Enter 1 or 2: ")
        if direction not in ("1", "2"):
            print("Invalid input, try again.")
        else:
            direction = int(direction)

    startfp = "Windows file path" if direction == 1 else "Linux file path"
    endfp = "Linux file path" if direction == 1 else "Windows file path"

    print(f"Paste {startfp} here:")
    fp = input()

    if direction == 1:
        result = wfp_to_lfp(fp)
    else:
        result = lfp_to_wfp(fp)

    result = translate_file_type(result)

    print(f"Translated {startfp} to {endfp}:")
    print(result)

# Run program
if __name__ == "__main__":
    main()
