from os import listdir
from os.path import isfile, join
import cv2
import time as pytime

# Global Variables
SC_FOLDER = '/Users/charlietao/Documents/Screenshots'


def apply_filter(image):
	new_image = image
	redder_map = image[:, :, 1] < image[:, :, 2]
	
	# less_red_map = image[:, :, 2] < (image[:, :, 1] + image[:, :, 0]) // 4

	# blue_green_sim_map = (image[:, :, 1] < image[:, :, 0] * 1.1) == (image[:, :, 0] < image[:, :, 1] * 1.1)
	
	# cyanish_map = blue_green_sim_map == less_red_map
	
	# image[cyanish_map, 2] //= 2 # Halves red values when pixel is Cyanish
	# image[cyanish_map, 1] += (256 - image[cyanish_map, 1] // 2) # Increases green values when pixel is Cyanish
	# image[cyanish_map, 0] += (256 - image[cyanish_map, 0] // 2) # Increases blue values when pixel is Cyanish
	
	image[redder_map, 1] //= 2 # Halves green values when pixel is Redder

	return new_image


def display_image(path: str, time: int, yes_filter: bool) -> None:
	# Adding filter or not
	if yes_filter:
		cv2.imshow('Displayed Screenshot', apply_filter(open_image(path)))
	else:
		cv2.imshow('Displayed Screenshot', open_image(path))

	# Window placement
	cv2.setWindowProperty('Displayed Screenshot', cv2.WND_PROP_TOPMOST, 1)
	
	# Necessary to keep the window open
	cv2.waitKey(time) 
	cv2.destroyAllWindows()
	cv2.waitKey(1)


def open_image(path: str):
	return cv2.imread(path, cv2.IMREAD_COLOR)


def find_folder(path) -> set:
	return set([f for f in listdir(path) if isfile(join(path, f))])


# Testing Function
def version_testing(version: int) -> None:
	curr_files = find_folder(SC_FOLDER)
	
	# Opening and filtering testing files
	for file in curr_files:

		# If Ver1 file, show original for 1 second then filtered
		if file[0:4] == 'Ver' + str(version):
			print('Testing file found.')
			path = SC_FOLDER + '/' + file
			print('Showing original.')
			display_image(path, 1000, False)
			print('Showing filtered.')
			display_image(path, 0, True)
	
	print('Testing Complete.')


# Main Program
def run(time):
	
	# Setting up the path and files
	previous_files = find_folder(SC_FOLDER)

	# Starting the continuous file checking loop
	print('Loop start!')
	while True:
		new_files = find_folder(SC_FOLDER)

		# If the sets are different, find different file
		set_diff = new_files.difference(previous_files)				
		if set_diff:
			file_name = set_diff.pop()
			print(file_name)
			
			# If file is a screenshot file, display screenshot
			if file_name[0] == 'S':
				new_path = SC_FOLDER + '/' + file_name
				print(new_path)
				display_image(new_path, time, True)
				
			previous_files = new_files

		# Preventing battery from draining via 1916 runs per second
		pytime.sleep(0.1)


# Console Start
if __name__ == '__main__':
	inp = input('RUN or TEST? \n').upper()
	if inp == 'RUN':
		time = input('Time? \n')
		run(int(time))
	elif inp == 'TEST':
		version_testing(1)
