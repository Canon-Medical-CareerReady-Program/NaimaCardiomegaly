import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

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

# Create a button to open a new window
button = tk.Button(window, text="Open Image", command=open_file)
button.pack()

#creating a label to store the image
image_label = tk.Label(window)
image_label.pack()

# Run the main event loop
window.mainloop()