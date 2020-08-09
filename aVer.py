from Tkinter import *
from PIL import Image,ImageTk
import sys

# Root #
root = Tk()
root.title("aVer")
# root.iconbitmap("")
# Maximize window
root.state("zoomed")

# Select file
if len(sys.argv) > 1:
    file = sys.argv[1]
else:
	print("Please select a file")

# Data #
current_img = Image.open(file) # Fits
# Get image's original size in pixels
width, height = current_img.size

# Get screen size in pixels
w_height = root.winfo_screenheight()  
w_width = root.winfo_screenwidth() 

final_width = width
final_height = height


# Methods #

def prevImage(event):
    print("prev image")

def nextImage(event):
	print("next image")


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

# Widgets #
show_img = Label(image=current_resize_img)
root.bind("a", prevImage)
root.bind("s", nextImage)

# UI #
show_img.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
