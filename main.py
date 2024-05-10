import tkinter as tk
from tkinter import filedialog, colorchooser
from PIL import Image, ImageOps, ImageTk, ImageFilter
from tkinter import ttk

# Function to add an image
def add_image():
    global file_path
    file_path = filedialog.askopenfilename(
        initialdir="D:/codefirst.io/Tkinter Image Editor/Pictures")
    if file_path:
        image = Image.open(file_path)
        width, height = int(image.width / 2), int(image.height / 2)
        image = image.resize((width, height), Image.LANCZOS)
        canvas.config(width=image.width, height=image.height)
        image = ImageTk.PhotoImage(image)
        canvas.image = image
        canvas.create_image(0, 0, image=image, anchor="nw")

# Function to change pen color
def change_color():
    global pen_color
    color = colorchooser.askcolor(title="Select Pen Color")
    if color[1]:
        pen_color = color[1]

# Function to change pen size
def change_size(size):
    global pen_size
    pen_size = size

# Function to draw on canvas
def draw(event):
    x1, y1 = (event.x - pen_size), (event.y - pen_size)
    x2, y2 = (event.x + pen_size), (event.y + pen_size)
    canvas.create_oval(x1, y1, x2, y2, fill=pen_color, outline='')

# Function to clear canvas
def clear_canvas():
    canvas.delete("all")
    if file_path:
        canvas.create_image(0, 0, image=canvas.image, anchor="nw")

# Function to apply filter
def apply_filter(selected_filter):
    global file_path
    if file_path:
        image = Image.open(file_path)
        width, height = int(image.width / 2), int(image.height / 2)
        image = image.resize((width, height), Image.LANCZOS)

        if selected_filter == "Black and White":
            image = ImageOps.grayscale(image)
        elif selected_filter == "Blur":
            image = image.filter(ImageFilter.BLUR)
        elif selected_filter == "Sharpen":
            image = image.filter(ImageFilter.SHARPEN)
        elif selected_filter == "Smooth":
            image = image.filter(ImageFilter.SMOOTH)
        elif selected_filter == "Emboss":
            image = image.filter(ImageFilter.EMBOSS)

        image = ImageTk.PhotoImage(image)
        canvas.image = image
        canvas.create_image(0, 0, image=image, anchor="nw")
    else:
        print("Please add an image first.")

# Creating the main window
root = tk.Tk()
root.geometry("1000x600")
root.title("Image Drawing Tool")
root.config(bg="#f0f0f0")

# Global variables
pen_color = "black"
pen_size = 5
file_path = ""

# Left frame
left_frame = tk.Frame(root, width=200, height=600, bg="#f0f0f0", bd=2, relief=tk.GROOVE)
left_frame.pack(side="left", fill="y", padx=10, pady=10)

# Canvas
canvas = tk.Canvas(root, width=750, height=600, bg="white", bd=2, relief=tk.GROOVE)
canvas.pack()

# Add Image Button
image_button = tk.Button(left_frame, text="Add Image", command=add_image, bg="#4CAF50", fg="white", relief=tk.FLAT)
image_button.pack(pady=10)

# Change Pen Color Button
color_button = tk.Button(left_frame, text="Change Pen Color", command=change_color, bg="#2196F3", fg="white", relief=tk.FLAT)
color_button.pack(pady=10)

# Pen Size Frame
pen_size_frame = tk.Frame(left_frame, bg="#f0f0f0")
pen_size_frame.pack(pady=10)

# Pen Size Radiobuttons
pen_size_1 = tk.Radiobutton(pen_size_frame, text="Small", value=3, command=lambda: change_size(3), bg="#f0f0f0")
pen_size_1.pack(side="left", padx=5)

pen_size_2 = tk.Radiobutton(pen_size_frame, text="Medium", value=5, command=lambda: change_size(5), bg="#f0f0f0")
pen_size_2.pack(side="left", padx=5)
pen_size_2.select()

pen_size_3 = tk.Radiobutton(pen_size_frame, text="Large", value=7, command=lambda: change_size(7), bg="#f0f0f0")
pen_size_3.pack(side="left", padx=5)

# Clear Button
clear_button = tk.Button(left_frame, text="Clear", command=clear_canvas, bg="#FF5722", fg="white", relief=tk.FLAT)
clear_button.pack(pady=10)

# Filter Label
filter_label = tk.Label(left_frame, text="Select Filter", bg="#f0f0f0")
filter_label.pack()

# Filter Combobox
filter_combobox = ttk.Combobox(left_frame, values=["Black and White", "Blur", "Emboss", "Sharpen", "Smooth"], state="readonly")
filter_combobox.pack(pady=10)

# Binding Combobox Selection to Apply Filter Function
filter_combobox.bind("<<ComboboxSelected>>", lambda event: apply_filter(filter_combobox.get()))

# Binding Canvas Motion to Draw Function
canvas.bind("<B1-Motion>", draw)

# Running the application
root.mainloop()
