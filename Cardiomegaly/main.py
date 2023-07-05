
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import ttk

# Opens file explorer to insert an image (either a png, jpg or a jpeg file)
def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif")])
    if file_path:
        image = tk.PhotoImage(file=file_path)
        canvas.config(width=image.width(), height=image.height())
        canvas.create_image(0, 0, anchor="nw", image=image)
        canvas.image = image  # Save a reference to the image to prevent it from being garbage collected

# What happens when the mouse is pressed down on the image for the heart diameter
def start_drawing_hline():
    canvas.bind("<Button-1>", start_hline)

# What happens when the mouse is dragged along the image for the heart diameter
def start_hline(event):
    global line1_start_x, line1_start_y
    line1_start_x = event.x
    line1_start_y = event.y
    canvas.bind("<B1-Motion>", draw_hline)

# The heart line being seen by the user
def draw_hline(event):
    canvas.delete("line1")
    canvas.create_line(line1_start_x, line1_start_y, event.x, event.y, tags="line1", fill="yellow", width=2)

# Displays the co-ordinates of where the heart diameter starts and ends

    Hcoordinates_label.config(text=f"Heart-  Start: ({line1_start_x},{line1_start_y}) End: ({event.x},{event.y})")

# What happens when the mouse is pressed down on the image for the lung diameter
def start_drawing_Lline():
    canvas.bind("<Button-1>", start_Lline)

# What happens when the mouse is dragged along the image for the lung diameter
def start_Lline(event):
    global line2_start_x, line2_start_y
    line2_start_x = event.x
    line2_start_y = event.y
    canvas.bind("<B1-Motion>", draw_Lline)

# The lung line being seen by the user
def draw_Lline(event):
    canvas.delete("line2")
    canvas.create_line(line2_start_x, line2_start_y, event.x, event.y, tags="line2", fill="red", width=2)

# Displays the co-ordinates of where the lung diameter starts and ends

    Lcoordinates_label.config(text=f"Lungs-  Start: ({line2_start_x},{line2_start_y}) End: ({event.x},{event.y})")

# Deletes the lines drawn
def stop_drawing():
    canvas.unbind("<Button-1>")
    canvas.unbind("<B1-Motion>")
    canvas.delete("line1")
    canvas.delete("line2")
    Lcoordinates_label.config(text="")
    Hcoordinates_label.config(text="")



# Create the main window
window = tk.Tk()
window.title("Cardiomegaly Detector")
window.state("zoomed")


# Creates a frame for the buttons
button_frame= tk.Frame(window,bg="lightgray", width=400)
button_frame.pack(side=tk.LEFT, fill=tk.BOTH)

# Creates the canvas
canvas = tk.Canvas(window)
canvas.pack(side=tk.RIGHT, fill=tk.Y, expand=True)

# Create a button to open a new window for file explorer
button = tk.Button(button_frame, text="Open Image", command=open_image)
button.pack()
button.place(x=50, y=100)
button.configure(bg="#797EF6")

# Creates a button to draw the heart diameter
start_hbutton= tk.Button(button_frame,text="Draw Heart Diameter",command=start_drawing_hline)
start_hbutton.pack()
start_hbutton.configure(bg="#797EF6")
start_hbutton.place(x=50, y=250)

# Creates a button to draw the lung diameter
start_Lbutton= tk.Button(button_frame,text="Draw Lung Diameter",command=start_drawing_Lline)
start_Lbutton.pack()
start_Lbutton.configure(bg="#797EF6")
start_Lbutton.place(x=50, y=290)

# Creates a button to clear the canvas
stop_button = tk.Button(button_frame, text="Clear Canvas", command=stop_drawing)
stop_button.pack()
stop_button.configure(bg="#D31A38")
stop_button.place(x=50, y=330)


#Creates a label for the heart co-ordinates
Hcoordinates_label = tk.Label(button_frame, text="", font=("Verdana",8),bg="lightgray")
Hcoordinates_label.pack()
Hcoordinates_label.place(x=50,y=800)

# Creates a label for the heart co-ordinates
Lcoordinates_label = tk.Label(button_frame, text="", font=("Verdana",8),bg="lightgray")
Lcoordinates_label.pack()
Lcoordinates_label.place(x=50,y=820)

# Creates a label to show the user what its called lmao
title_label= tk.Label(button_frame,text="Cardiomegaly Detector", font=("Verdana",12),bg="lightgray")
title_label.place(x=50, y=50)

# Creates a label to show the user the buttons that they can make measurements on
subheader_label= tk.Label(button_frame,text="Drawing Tools", font=("Verdana",12),bg="lightgray")
subheader_label.place(x=50,y=200)

# Creates a label to show the user the co-ordinates
coordinates_label= tk.Label(button_frame,text="Co-ordinates",font=("Verdana",12),bg="lightgray")
coordinates_label.place(x=50,y=750)

# Run the main event loop
window.mainloop()