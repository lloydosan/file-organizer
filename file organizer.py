import os
import shutil

class FileOrganizer:
    def __init__(self, folder_path, verbose=False):
        self.folder_path = folder_path
        self.verbose = verbose

        self.file_types = {
            "Images": [".png", ".jpg", ".gif", ".jpeg"],
            "Documents": [".pdf", ".docx", ".xlsx", ".txt"],
            "Videos": [".mp4", ".mov", ".avi"],
            "Music": [".mp3", ".wav"],
            "Others": [],
            "Application": [".exe", ".msi"] 
        }

    def create_folder(self):
        for folder in self.file_types:
            folder_location = os.path.join(self.folder_path, folder)
            if not os.path.exists(folder_location):
                os.makedirs(folder_location)

    def move_files(self):
        for filename in os.listdir(self.folder_path):
            file_path = os.path.join(self.folder_path, filename)

            if os.path.isdir(file_path):
                if self.verbose:
                    print(f"Skippping Folder: {filename}")
                continue
            
            if self.verbose:
                print(f"Processing File: {filename}")

            _, extension = os.path.splitext(filename)
            print(f"Found file: {filename}")
            print(f"Extensions: {extension}")

            moved = False
            for folder, extensions in self.file_types.items():
                if extension.lower() in extensions:
                    shutil.move(file_path, os.path.join(self.folder_path, folder, filename))
                    moved = True
                    break

            if not moved:
                shutil.move(file_path, os.path.join(self.folder_path, "Others", filename))

    def organize(self):
        self.create_folder()
        self.move_files()
        print("Files Moved Succesfully!")

if __name__ == "__main__":
    path = input("Enter the folder path you want to organize: ")
    debug_choice = input("Enter debug mode?(Y/N): ").lower()

    verbose_mode = debug_choice == "y"
    
    if not os.path.exists(path):
        print("Folder does not exist or is not found")
    else:
        organizer = FileOrganizer(path, verbose=verbose_mode)
        organizer.organize()