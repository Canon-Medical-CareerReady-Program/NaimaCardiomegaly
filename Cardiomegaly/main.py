import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image


# Opens file explorer to insert an image (either a png, jpg or a jpeg file)
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
    if file_path:
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo



# Create the main window
window = tk.Tk()
window.title("Cardiomegaly Detector")

# Create a button to open a new window for file explorer
button = tk.Button(window, text="Open Image", command=open_file)
button.pack()
button.place(x=50, y=100)
button.configure(bg="#797EF6")


title_label= tk.Label(window,text="Cardiomegaly Detector", font=("Verdana",12))
title_label.place(x=50, y=50)

# Creating a label to store the image
image_label = tk.Label(window)
image_label.pack()


# Run the main event loop
window.mainloop()