import os
import shutil
import sys
from pathlib import Path

def sort_files_by_extension(directory):
    """
    Sort files in the given directory into subfolders based on their extensions.
    Leaves subfolders untouched.
    """
    # Convert to absolute path
    directory = os.path.abspath(directory)
    
    # Check if directory exists
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return
    
    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a directory.")
        return
    
    # Walk through all items in the directory
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        
        # Skip if it's a directory (leave folders as they are)
        if os.path.isdir(item_path):
            print(f"Skipping folder: {item}")
            continue
        
        # Process only files
        if os.path.isfile(item_path):
            # Get file extension
            file_name, file_extension = os.path.splitext(item)
            
            # Handle files without extension
            if file_extension:
                # Remove the dot from extension
                extension = file_extension[1:].lower()
                # Handle empty extension (like .gitignore)
                if not extension:
                    extension = "no_extension"
            else:
                extension = "no_extension"
            
            # Create subfolder name (e.g., "txt_files", "jpg_files", etc.)
            subfolder_name = f"{extension}_files"
            subfolder_path = os.path.join(directory, subfolder_name)
            
            # Create the subfolder if it doesn't exist
            if not os.path.exists(subfolder_path):
                os.makedirs(subfolder_path)
                print(f"Created folder: {subfolder_name}")
            
            # Move the file to the subfolder
            destination = os.path.join(subfolder_path, item)
            
            # Handle duplicate filenames
            if os.path.exists(destination):
                base, ext = os.path.splitext(item)
                counter = 1
                while os.path.exists(os.path.join(subfolder_path, f"{base}_{counter}{ext}")):
                    counter += 1
                destination = os.path.join(subfolder_path, f"{base}_{counter}{ext}")
            
            shutil.move(item_path, destination)
            print(f"Moved: {item} -> {subfolder_name}/")

def main():
    # Check if folder path is provided as command line argument
    if len(sys.argv) != 2:
        print("Usage: python sort_files.py <folder_path>")
        print("Example: python sort_files.py /path/to/your/folder")
        sys.exit(1)
    
    folder_path = sys.argv[1]
    
    # Confirm with user before proceeding
    print(f"Are you sure you want to sort files in: {folder_path}")
    print("This will create subfolders for each file extension.")
    response = input("Continue? (yes/no): ").lower()
    
    if response in ['yes', 'y']:
        sort_files_by_extension(folder_path)
        print("\nDone! Files have been sorted by extension.")
    else:
        print("Operation cancelled.")

if __name__ == "__main__":
    main()