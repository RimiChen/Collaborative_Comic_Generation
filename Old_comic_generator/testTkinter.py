# Import the required libraries
from tkinter import *
from PIL import Image, ImageTk

# Create an instance of tkinter frame
win= Tk()

# Set the size of the tkinter window
win.geometry("700x350")

# Store newly created image
images=[]

# Define a function to make the transparent rectangle
def create_rectangle(x,y,a,b,**options):
   if 'alpha' in options:
      # Calculate the alpha transparency for every color(RGB)
      alpha = int(options.pop('alpha') * 255)
      # Use the fill variable to fill the shape with transparent color
      fill = options.pop('fill')
      fill = win.winfo_rgb(fill) + (alpha,)
      image = Image.new('RGBA', (a-x, b-y), fill)
      images.append(ImageTk.PhotoImage(image))
      canvas.create_image(x, y, image=images[-1], anchor='nw')
      canvas.create_rectangle(x, y,a,b, **options)
# Add a Canvas widget
canvas= Canvas(win)

# Create a rectangle in canvas
create_rectangle(50, 110,300,280, fill= "blue", alpha=.3)
create_rectangle(40, 90, 420, 250, fill= "red", alpha= .1)
canvas.pack()

win.mainloop()