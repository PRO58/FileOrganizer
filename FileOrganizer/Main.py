from FileOrganizer import FileOrganizer



def Main():
	
	getPath = input("What is the path are you willing to work with? ")
	getExtension = input("Enter the file extension you want to organize: ")
	getFileName = input("Enter the file name: ")

	file_organizer = FileOrganizer(getPath,getExtension,getFileName)

	
	file_organizer.ChangePath()
	file_organizer.createFile()
	file_organizer.Organizer()





if __name__ == "__main__":
	Main()

	





