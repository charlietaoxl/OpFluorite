from os import listdir
from os.path import isfile, join
import cv2

def open_image(path: str):
	return cv2.imread(path, cv2.IMREAD_COLOR)

def apply_filter(image):
	new_image = image
	redder_map = image[:, :, 1] < image[:, :, 2]
	image[redder_map, 1] //= 2 
	return new_image

def display_image(path: str) -> None:
	cv2.imshow('Colour Filtered Screenshot', apply_filter(open_image(path)))
	cv2.setWindowProperty('Colour Filtered Screenshot', cv2.WND_PROP_TOPMOST, 1)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	cv2.waitKey(1)

# The main program
def main():
	
	# Setting up the path and files
	mypath = '/Users/charlietao/Documents/Screenshots'
	previous_files = set([f for f in listdir(mypath) if isfile(join(mypath, f))])

	# Starting the continuous file checking loop
	print('Start!')
	while True:
		new_files = set([f for f in listdir(mypath) if isfile(join(mypath, f))])
		
		# Checks if directory set is different and locates different file path
		set_diff = new_files.difference(previous_files)
		if set_diff:
			file_name = set_diff.pop()
			if file_name[0] == 'S':

				# Displaying image 
				new_path = mypath + '/' + file_name
				print(new_path)
				display_image(new_path)

			previous_files = new_files

# Running the program
if __name__ == '__main__':
	main()
