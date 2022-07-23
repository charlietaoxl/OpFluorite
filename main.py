from os import listdir
from os.path import isfile, join
# import cv2

def display_image(str: path) -> None:
	print(new_sc + new_files[i])

if __name__ == '__main__':

	# Setting up the path and files
	mypath = '/Users/charlietao/Documents/Screenshots'
	new_sc = mypath + '/'
	previous_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

	# Starting the continuous file checking loop
	print('Start!')
	while True:
		new_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
		
		# Checks if directory list is different and locates different file path
		if previous_files != new_files:
			for i in range(len(new_files) - 1):
				if new_files[i] not in previous_files and new_files[i][0] == 'S':

					# Placeholder function
					display_image()
					break
					
			previous_files = new_files
