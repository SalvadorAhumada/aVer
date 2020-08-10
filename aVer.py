from Tkinter import *
from PIL import Image,ImageTk
import sys
import os

####################
file_types_accepted = ('.png', '.jpg', '.jpeg')
####################

###############################################
#                                             #
# TODO: Add end and start of array limitation #
#                                             #
###############################################

root = Tk()
root.title("aVer")
if len(sys.argv) < 1:
	root.iconbitmap(sys.argv[2])
# Temporal disable resize
root.resizable(False, False)
w, h = root.winfo_screenwidth(), root.winfo_screenheight() -50
root.geometry("%dx%d+0+0" % (w, h))

# When we open the app we check for the file first
if len(sys.argv) > 1:
	file = sys.argv[1]
else:
	print("Please select a file")

# We pass that image to the app
current_img = Image.open(file)
# Get image's original size in pixels
width, height = current_img.size
# Get screen size in pixels
w_height = root.winfo_screenheight()  
w_width = root.winfo_screenwidth() 

################################# METHODS ###################################################
def renderComponent():
	global show_img, current_resize_img,current_img
	show_img = Label(image=current_resize_img)
	show_img.place(relx=0.5, rely=0.5, anchor=CENTER)
	root.mainloop()

#############################################################################################
def changeImage(event):
	global nextI, show_img, img_directory, images_array, current_resize_img, current_img, width, height
	key = event.keysym
	if key == 'Left':
		nextI = nextI - 1
	else:
		nextI = nextI + 1

	show_img.place_forget()
	current_img = Image.open(img_directory + images_array[nextI])
	width, height = current_img.size
	current_resize_img = ImageTk.PhotoImage(current_img)
	resizeImage()
	renderComponent()

#############################################################################################
def resizeImage():
	global width, height, w_height, w_width, current_resize_img, current_img
	# We now resize if needed
	final_width = width
	final_height = height
# Get aspect ratio
	if width > height:
		relative = ((height * 100) / width)
	else:
		relative = ((width * 100) / height)

	relative = float(relative)/100

	# Resize image
	if height > w_height and width > w_width:
# Image is too big overall. Scale down until both height and weight are smaller than screen
		while final_width > w_width or final_height > w_height:
			final_width = float(final_width* 0.8)
			final_height = float(final_height * 0.8)
	elif height > w_height:
# Image resizing depending on height
		final_height = w_height - 100 
		final_width = float(final_height) * relative

	final_width=int(final_width)
	final_height=int(final_height)

	resize_img = current_img.resize((final_width,final_height),Image.ANTIALIAS)
	current_resize_img = ImageTk.PhotoImage(resize_img)

resizeImage()

# Then we grab that image directory and make an array of all images within that directory
url = ""
img_directory = file
for letter in reversed(file):
	if letter == "\\":
		break
	url += letter

url = url [::-1]
img_directory = img_directory.replace(url, '')
entries = os.listdir(img_directory)
images_array = []
# We iterate in that array to find the index of the current image
for i in range(len(entries)):
	if entries[i].lower().endswith(file_types_accepted):
		images_array.append(entries[i])
current = images_array.index(url)
nextI = current

root.bind("<Left>", changeImage)
root.bind("<Right>", changeImage)

# Render
renderComponent()
