import os
import shutil

# Ask user for folder path
folder_path = input("Enter the folder path to organize: ").strip()

# Check if folder exists
if not os.path.exists(folder_path):
    print("Folder does not exist!")
    exit()

# File categories
categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar"],
    "Programs": [".py", ".java", ".c", ".cpp", ".js"]
}

file_count = 0

# Read files
for file_name in os.listdir(folder_path):

    file_path = os.path.join(folder_path, file_name)

    # Skip folders
    if os.path.isdir(file_path):
        continue

    extension = os.path.splitext(file_name)[1].lower()
    category = "Others"

    # Find category
    for category_name, extensions in categories.items():
        if extension in extensions:
            category = category_name
            break

    # Create category folder
    category_path = os.path.join(folder_path, category)
    os.makedirs(category_path, exist_ok=True)

    # Move file
    destination = os.path.join(category_path, file_name)

    # Handle duplicate filenames
    if os.path.exists(destination):
        name, ext = os.path.splitext(file_name)
        destination = os.path.join(
            category_path,
            name + "_copy" + ext
        )

    shutil.move(file_path, destination)

    print(f"Moved: {file_name} → {category}")
    file_count += 1

print("\n==============================")
print("File organization completed!")
print("Total files organized:", file_count)
print("==============================")