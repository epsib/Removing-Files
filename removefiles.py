import os
import shutil
import time


def main():


	deletedfolderscount = 0
	deletedfilescount = 0

	path = "/PATH_TO_DELETE"

	days = 30


	seconds = time.time() - (days * 24 * 3600)

	
	if os.path.exists(path):
		for root_folder, folders, files in os.walk(path):
			if seconds >= get_file_or_folder_age(root_folder):

				remove_folder(root_folder)
				deletedfolderscount += 1 
				break

			else:

				for folder in folders:

					folder_path = os.path.join(root_folder, folder)

					if seconds >= get_file_or_folder_age(folder_path):

						remove_folder(folder_path)
						deletedfolderscount += 1 

				for file in files:

					file_path = os.path.join(root_folder, file)

					if seconds >= get_file_or_folder_age(file_path):
						remove_file(file_path)
						deletedfilescount += 1

		else:

			if seconds >= get_file_or_folder_age(path):
				remove_file(path)
				deletedfilescount += 1

	else:

		# file/folder is not found
		print(f'"{path}" is not found')
		deletedfilescount += 1 

	print(f"Total folders deleted: {deletedfolderscount}")
	print(f"Total files deleted: {deletedfilescount}")


def remove_folder(path):

	if not shutil.rmtree(path):
		print(f"{path} is removed successfully")
	else:
		print(f"Cannot delete the "+path)



def remove_file(path):
	if not os.remove(path):
		print(f"{path} is removed successfully")

	else:
		print("Cannot delete the "+path)


def get_file_or_folder_age(path):
	ctime = os.stat(path).st_ctime
	return ctime

if __name__ == '__main__':
	main()