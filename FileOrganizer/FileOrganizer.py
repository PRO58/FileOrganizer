import os
import shutil

class FileOrganizer:
    def __init__(self, getPath, getExtension, fileName):
        self.getPath = getPath
        self.getExtension = getExtension
        self.fileName = fileName

    def ChangePath(self):
        try:
            os.chdir(f'{self.getPath}')
            print(f"Successfully switched to {self.getPath}")
        except FileNotFoundError:
            print(f"{self.getPath} Directory not found")

    def Organizer(self):
        FilesRequestedToMove = []
        self.search = os.popen(f"dir /B /A-D *.{self.getExtension}").read()
        FilesRequestedToMove.extend(self.search.split('\n')[:-1])  # Split the output into a list of file names

        for files in FilesRequestedToMove:
            source_path = os.path.join(self.getPath, files)
            destination_path = os.path.join(self.fileName, os.path.basename(files))

            if os.path.exists(source_path):
                shutil.move(source_path, destination_path)
                print(f"Successfully transferred {os.path.basename(files)}")
            else:
                print(f"Couldn't transfer {os.path.basename(files)}")

    def createFile(self):
        if not os.path.exists(self.fileName):
            os.makedirs(self.fileName)
            print("Successfully created file")
        else:
            print("File already exists")
