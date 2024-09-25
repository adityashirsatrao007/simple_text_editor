import sys

# Importing Tkinter based on Python version
if sys.version_info[0] < 3:
    from Tkinter import *  # Python 2.x
    import tkFileDialog
else:
    from tkinter import *  # Python 3.x
    from tkinter import filedialog

# Create the main application window
root = Tk()
root.title("Text Editor")  # Set the title of the window

# Create a text widget
text = Text(root)
text.grid()

# Function to save the text
def saveas():
    global text
    t = text.get("1.0", "end-1c")  # Get text from the text widget
    savelocation = filedialog.asksaveasfilename()  # Open save dialog
    with open(savelocation, "w+") as file1:  # Open the file for writing
        file1.write(t)  # Write the text to the file

# Create a save button
button = Button(root, text="Save", command=saveas)
button.grid()

# Functions to change the font
def FontHelvetica():
    global text
    text.config(font="Helvetica")  # Set font to Helvetica

def FontCourier():
    global text
    text.config(font="Courier")  # Set font to Courier

# Create a menu for font selection
font = Menubutton(root, text="Font")
font.grid()
font.menu = Menu(font, tearoff=0)
font["menu"] = font.menu

# Font options
helvetica = IntVar()
courier = IntVar()
font.menu.add_checkbutton(label="Courier", variable=courier, command=FontCourier)
font.menu.add_checkbutton(label="Helvetica", variable=helvetica, command=FontHelvetica)

# Start the main event loop
root.mainloop()
