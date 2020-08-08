from Tkinter import *
from PIL import Image,ImageTk

#### Root window with tkinter
root = Tk()
root.title("aVer")

#### Methods ####

#### Variables ####
current_img = Image.open("C:\\Users\\lsaz1\\Downloads\\1590617036447.png") # Height > screen
# current_img = Image.open("C:\\Users\\lsaz1\\Pictures\\1500x500.jpg") # Width > screen

# Get image's original size in pixels
width, height = current_img.size

# Get screen size in pixels
w_height = root.winfo_screenheight()  
w_width = root.winfo_screenwidth() 

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
	print("Image is bigger all around")
elif height > w_height:

	final_height = w_height - 100 
	final_width = int(float(final_height) * relative)
	
elif width > w_width:
	print("Image is fatter")
elif height < w_height and width < w_width:
	print("Image fits!")


resize_img = current_img.resize((final_width,final_height),Image.ANTIALIAS)

current_resize_img = ImageTk.PhotoImage(resize_img)

#### Widgets ####
show_img = Label(image=current_resize_img)

#### UI ####
show_img.grid(row=0,column=0,columnspan=3)

# Event Loop
root.mainloop()
