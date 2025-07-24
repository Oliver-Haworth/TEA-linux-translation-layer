# TEA (Translation Envelope Application)

TEA is a simple standalone Python utility designed to translate file paths between Windows and Linux formats and rename certain file extensions for basic compatibility. It is an MVP (minimum viable product) created as a summer project, primarily to help hobbyists and developers who want a lightweight translation layer without full Windows emulation.


---

# What TEA Does

Converts Windows file paths (e.g., C:\Users\Name\File.txt) into Linux-style paths (e.g., /mnt/c/Users/Name/File.txt), and vice versa.

Does not emulate Windows or provide full compatibility layers like Wine — it’s a simple translator utility.

Written in pure Python with no external dependencies (except Pillow if you include the .webp to .png converter).



---

# Who Is This For?

Anyone who finds it useful under the MIT License. TEA is ideal for hobbyists or developers looking for a lightweight way to handle basic Windows-to-Linux path and filetype translation.


---

# Usage

1. Ensure you have Python 3 installed.


2. If you plan to use the .webp to .png converter, install the Pillow library:

pip install pillow


3. Run the script via the command line:

python main.py


4. Follow the prompts to choose translation direction:

Enter 1 for Windows file path → Linux file path

Enter 2 for Linux file path → Windows file path



5. Paste your file path when prompted.


6. View the translated path with file extension translated where applicable.




---

# Known Status

This is an MVP and a work in progress.

No known bugs to date, but some unexpected behavior may occur.

Contributions or suggestions are welcome to improve TEA.



---

# Future Plans

No formal roadmap yet; development will continue iteratively as a personal summer project. Community suggestions and changes are welcome and will be considered.


---

# License

MIT License
