import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from calculation import calculate_quote

'''
Variables needed
    - Cost price (input by the user)
    - Margin (drop down)
    - Hours spent (input by the user)
    - Total (input by the user)

Output
    - Quote = (cost_price * margin) + (hours_spent * wage)
        - For function please refer to caclulation.py file

    3 Croi_Meala_Honey_Transparent BG_alt.png
    /Users/timstephens/git/quotingTool/images/3 Croi_Meala_Honey_Transparent BG_alt.png
'''
def calculate_quote_gui():
    '''
    The following function takes in the input values set by the user, 
    calculates the quote and then displays it to them via the GUI.
    '''
    cost_price = float(cost_price_entry.get())
    margin = float(margin_var.get())
    hours_spent = float(hours_spent_entry.get())
    wage = float(wage_entry.get())


    # Calculate the quote based on the inputs
    calculated_quote=calculate_quote(cost_price, margin, hours_spent, wage)

    # Display the result
    result_label.config(text=f"Quote: €{calculated_quote}")

# Create the main window
root = tk.Tk()
root.title("Croi Meala Quoting Tool")

#Background colour
root.configure(bg="light pink")

# Load and display the logo
image_path = "/Users/timstephens/git/quotingTool/images/3 Croi_Meala_Honey_Transparent BG_alt.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)

# Define the new size
new_width = 150  # Adjust to your desired width
new_height = 45  # Adjust to your desired height

# Resize the image
resized_image = image.resize((new_width, new_height))
photo = ImageTk.PhotoImage(resized_image)

# Create a label to display the image
image_label = tk.Label(root, image=photo)
image_label.pack()


# Create input labels and entry fields
cost_price_label = tk.Label(root, text="Cost Price")
cost_price_label.pack()
cost_price_entry = tk.Entry(root)
cost_price_entry.pack()

# Create the dropdown menu for margin selection
margin_label = tk.Label(root, text="Margin")
margin_label.pack()
margin_var = tk.StringVar()
margin_dropdown = ttk.Combobox(root, textvariable=margin_var)
margin_dropdown['values'] = (2.5, 2.8, 3)
margin_dropdown.pack()

hours_spent_label = tk.Label(root, text="Hours Spent")
hours_spent_label.pack()
hours_spent_entry = tk.Entry(root)
hours_spent_entry.pack()

wage_label = tk.Label(root, text="Wage")
wage_label.pack()
wage_entry = tk.Entry(root)
wage_entry.pack()

# Create a submit button to calculate the quote
calculate_button = tk.Button(root, text="Calculate Quote", command=calculate_quote_gui)
calculate_button.pack()

# Create a label to display the quote
result_label = tk.Label(root, text="Quote: ")
result_label.pack()

# Start the main loop
root.mainloop()