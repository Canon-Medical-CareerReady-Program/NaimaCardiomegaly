import tkinter as tk
from tkinter import filedialog
from coordinate import Coordinate
from result import Result
from typing import List
from PIL import Image, ImageTk
import csv

current_result :Result= None
image_results :List[Result]= []
image_results_index= 0
original_image :Image= None

# Creates the image/canvas
def update_image_to_index():
    global current_result, image_results, image_results_index,original_image
    current_result = image_results[image_results_index]
    
    
    original_image= Image.open(current_result.file_path)
    update_image()
   
    
    update_heart_coordinates()
    update_thorax_coordinates()

    update_heart_distance()
    update_thorax_distance()

    calculate_ratio_and_percentage()

    update_heart_line()
    update_thorax_line()

# Resizes the canvas when the window is resized
def canvas_resized(event):
    global current_result
    print(f"{canvas.winfo_width()}, {canvas.winfo_height()}")
    update_image()
    update_heart_line()
    update_thorax_line()


# Updates the image after the canvas is resized
def update_image():
    global current_result, original_image, tkimage
    
  
    if original_image !=None:
        canvas_width = canvas.winfo_width()
        canvas_height = canvas.winfo_height()
        image_ratio = original_image.size[0] / original_image.size[1]

        canvas_ratio = canvas_width / canvas_height

        if canvas_ratio > image_ratio:
            height = int(canvas_height)
            width = int(height * image_ratio)
        else:
            width = int(canvas_width)
            height = int(width / image_ratio)


        size_tuple= (width,height)
        resized_image = original_image.resize(size=size_tuple)
        tkimage= ImageTk.PhotoImage(image=resized_image)
        print(resized_image)

        canvas.create_image(0, 0, anchor= "nw", image=tkimage)


# Opens file explorer to insert an image (either a png, jpg or a jpeg file)
def open_image():
    global current_result, image_results, image_results_index
    file_paths = filedialog.askopenfilenames(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif")])
    
    if len(file_paths) > 0:
        image_results= []
        for file_path in file_paths:
            image_results.append(Result(file_path))
        update_image_to_index()
 
# Switches to the next image
def next_image(event=None):
    global current_result, image_results, image_results_index
    
    if image_results_index < len(image_results) - 1:
        image_results_index = image_results_index + 1
        update_image_to_index()
    

# Switches to the previous image
def previous_image(event=None):
    global current_result, image_results, image_results_index

    if image_results_index > 0:
        image_results_index = image_results_index -1
        update_image_to_index()

# Opens up a spreadsheet
def open_spreadsheet():
    global current_result, image_results, image_results_index
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
    if file_path:
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Image Name","Heart Distance", "Thorax Distance", "Cardiothoracic Ratio","Percentage","Symptomatic"])
            for result in image_results:
                writer.writerow([result.file_path,result.heart.distance(), result.thorax.distance(), result.calculate_ratio(), result.calculate_percentage(), result.symptomatic()])







# What happens when the mouse is pressed down on the image for the heart diameter
def start_drawing_hline():
    reset_button_colors()
    start_hbutton.configure(bg="#9DBEFF")
    canvas.bind("<Button-1>", start_hline)
    canvas.bind("<ButtonRelease-1>",calculate_Hdistance)
    
# Calculates the distance of the heart diameter (in pixels)
def calculate_Hdistance(event):
    global current_result
    update_heart_distance()
    calculate_ratio_and_percentage()

def update_heart_distance():
    distance = current_result.heart.distance()
    Hdistance_label.config(text=f"Heart Distance: {distance:.2f} px")

# What happens when the mouse is dragged along the image for the heart diameter
def start_hline(event):
    global current_result
    current_result.heart.start.x = event.x
    current_result.heart.start.y = event.y
    canvas.bind("<B1-Motion>", draw_hline)

# The heart line being seen by the user
def draw_hline(event):
    current_result.heart.end.x = event.x
    current_result.heart.end.y = event.y
    update_heart_line()

# Displays the co-ordinates of where the heart diameter starts and ends
    update_heart_coordinates()

# Changes the heart line when the image is changed    
def update_heart_line():
    canvas.delete("heart")
    if current_result != None:
        start = current_result.heart.start
        end = current_result.heart.end
        canvas.create_line(start.x, start.y, end.x, end.y, tags="heart", fill="yellow", width=2)
        canvas.tag_raise("heart")

# Changes the heart coordinates when the image changes
def update_heart_coordinates():
    start = current_result.heart.start
    end = current_result.heart.end
    Hcoordinates_label.config(text=f"Heart-  Start: ({start.x},{start.y}) End: ({end.x},{end.y})")





# What happens when the mouse is pressed down on the image for the thorax diameter
def start_drawing_Tline():
    reset_button_colors()
    start_Lbutton.configure(bg="#9DBEFF")
    canvas.bind("<Button-1>", start_Tline)
    canvas.bind("<ButtonRelease-1>",calculate_Ldistance)

# Calculates lung distance
def calculate_Ldistance(event):
    global current_result
    update_thorax_distance()
    calculate_ratio_and_percentage()
  
# Updating the thorax distance
def update_thorax_distance():
    distance = current_result.thorax.distance()
    Ldistance_label.config(text=f"Thorax Distance: {distance:.2f} px") 

# What happens when the mouse is dragged along the image for the thorax diameter
def start_Tline(event):
    global current_result
    current_result.thorax.start = Coordinate(event.x, event.y)
    canvas.bind("<B1-Motion>", draw_Tline)

# The lung line being seen by the user
def draw_Tline(event):
    current_result.thorax.end = Coordinate(event.x, event.y)
    update_thorax_line()

    update_thorax_coordinates()

# Updates the thorax coordinates depending on the image
def update_thorax_line():
    if current_result != None:
        start = current_result.thorax.start
        end = current_result.thorax.end
        canvas.delete("thorax")
        canvas.create_line(start.x, start.y, end.x, end.y, tags="thorax", fill="red", width=2)
        canvas.tag_raise("thorax")

# Updates the thorax coordinates depending on the image
def update_thorax_coordinates():
    start = current_result.thorax.start
    end = current_result.thorax.end
    Lcoordinates_label.config(text=f"Thorax-  Start: ({start.x},{start.y}) End: ({end.x},{end.y})")



# Calculates the cardiothoracic ratio
def calculate_ratio_and_percentage():

    global current_result
    heart_dist= current_result.heart.distance()
    thorax_dist= current_result.thorax.distance()
    

    if heart_dist !=0 and thorax_dist !=0:
        current_result.calculate_ratio()
        ratio_label.config(text=f"Cardiothoracic Ratio: {current_result.calculate_ratio():.2f}")
        
        current_result.calculate_percentage()
        percentage_label.config(text=f"Percentage: {current_result.calculate_percentage():.2f}%")

        if current_result.symptomatic():
            diagnosis_label.config(text="The patient exhibits symptoms of having \ncardiomegaly")
        else:
            diagnosis_label.config(text="The patient does not exhibit symptoms of \nhaving cardiomegaly")
    
    else:
        ratio_label.config(text=f"Cannot calculate. Distances missing")
        percentage_label.config(text="")
        diagnosis_label.config(text="")


# Resets the button colours
def reset_button_colors():
    start_hbutton.configure(bg="#797EF6")  # Reset heart button color to original blue
    start_Lbutton.configure(bg="#797EF6")




# Deletes the lines drawn
def stop_drawing():
    canvas.unbind("<Button-1>")
    canvas.unbind("<B1-Motion>")
    canvas.delete("heart")
    canvas.delete("thorax")
    Lcoordinates_label.config(text="")
    Hcoordinates_label.config(text="")
    Ldistance_label.config(text="")
    Hdistance_label.config(text="")
    ratio_label.config(text="")
    percentage_label.config(text="")
    diagnosis_label.config(text="")
    current_result.heart.clear()
    current_result.thorax.clear()




# Create the main window
window = tk.Tk()
window.title("Cardiomegaly Detector")
window.state("zoomed")
window.bind("<Right>", next_image)
window.bind("<Left>", previous_image)

# Creates a frame for the buttons
button_frame= tk.Frame(window,bg="lightgray", width=400)
button_frame.pack(side=tk.LEFT, fill=tk.BOTH)

# Creates the canvas
canvas = tk.Canvas(window, bd=0, highlightthickness=0, relief="ridge")
canvas.bind("<Configure>", canvas_resized)
canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)




# Create a button to open a new window for file explorer
button = tk.Button(button_frame, text="Open Image", command=open_image)
button.place(x=50, y=100)
button.configure(bg="#797EF6")

# Creates a button to draw the heart diameter
start_hbutton= tk.Button(button_frame,text="Draw Heart Diameter",command=start_drawing_hline)
start_hbutton.configure(bg="#797EF6")
start_hbutton.place(x=50, y=250)

# Creates a button to draw the lung diameter
start_Lbutton= tk.Button(button_frame,text="Draw Thorax Diameter",command=start_drawing_Tline)
start_Lbutton.configure(bg="#797EF6")
start_Lbutton.place(x=50, y=290)

# Creates a button to clear the canvas
stop_button = tk.Button(button_frame, text="Clear Canvas", command=stop_drawing)
stop_button.configure(bg="#D31A38")
stop_button.place(x=50, y=330)

# Creates a button to open a spreadsheet
spreadsheet_button = tk.Button(button_frame, text = "Save to Spreadsheet", command= open_spreadsheet)
spreadsheet_button.place(x=50, y=150)
spreadsheet_button.configure(bg="#797EF6")




#Creates a label for the heart co-ordinates
Hcoordinates_label = tk.Label(button_frame, text="", font=("Verdana",8),bg="lightgray")
Hcoordinates_label.place(x=50,y=620)

# Creates a label for the heart co-ordinates
Lcoordinates_label = tk.Label(button_frame, text="", font=("Verdana",8),bg="lightgray")
Lcoordinates_label.place(x=50,y=650)

# Creates a label to display the distance of the heart
Hdistance_label= tk.Label(button_frame, text="", font=("Verdana",10),bg="lightgray")
Hdistance_label.place(x=50, y=430)

#  Creates a label to display the distance of the lungs
Ldistance_label= tk.Label(button_frame, text="", font=("Verdana",10),bg="lightgray")
Ldistance_label.place(x=50, y=450)

# Creates a label to show the user what its called lmao
title_label= tk.Label(button_frame,text="Cardiomegaly Detector", font=("Verdana",12),bg="lightgray")
title_label.place(x=50, y=50)

# Creates a label to show the user the buttons that they can make measurements on
subheader_label= tk.Label(button_frame,text="Drawing Tools", font=("Verdana",12),bg="lightgray")
subheader_label.place(x=50,y=200)

# Creates a label to show the user the co-ordinates
coordinates_label= tk.Label(button_frame,text="Co-ordinates:",font=("Verdana",12),bg="lightgray")
coordinates_label.place(x=50,y=590)

#Creates a label to show the user the distances
distances_label=tk.Label(button_frame,text="Distances:",font=("Verdana",12),bg="lightgray")
distances_label.place(x=50,y=400)

# Creates a label to show the user the ratio
ratio_label= tk.Label(button_frame, text="", font=("Verdana",10),bg="lightgray" )
ratio_label.place(x=50, y=490)

# Creates a label to display the percentage
percentage_label=tk.Label(button_frame, text="", font=("Verdana",10),bg="lightgray")
percentage_label.place(x=50, y=510)

# Creates a label to display the diagnosis of the patient
diagnosis_label= tk.Label(button_frame, text="", font=("Verdana",10),bg="lightgray")
diagnosis_label.place(x=50, y=550)

# Run the main event loop
window.mainloop()