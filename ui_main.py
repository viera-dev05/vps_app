#Importing tkinter for easy GUI
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry

#Added defalut.json database for saving presets
import json
import os
#Path to my preset file
preset_path = os.path.join('presets', 'default.json')
#Load the presets
with open(preset_path, 'r') as preset_file:
    preset_data = json.load(preset_file)

#Setting up root window (main window)
root = tk.Tk()
root.title('Viera\'s Personal Savings App')
root.geometry('400x500') 

#Creating and packing the main frame
main_frame = ttk.Frame(root, padding=20)
main_frame.pack(fill='both', expand=True)
title_label = ttk.Label(main_frame, text='Personal Savings Tracker', font=('Segoe UI', 16))
title_label.pack(pady=10)

#Creating sub frames. 
#Left side subframe: data entry like date, income, description
left_subframe = ttk.Frame(main_frame, padding=5)
left_subframe.pack(side='left', fill='both', expand=True)

#Rifht side subframe: data entry for categories, like rent, food, hobbies and percentages per each one.
right_subframe = ttk.Frame(main_frame, padding=5)
right_subframe.pack(side='right', fill='both', expand=True)


#Creating lef side subframe data input fields. 
#Date field
ttk.Label(left_subframe, text='Date:').grid(row=0, column=0, sticky='e', pady=5)
date_entry = DateEntry(left_subframe,
                        width=12,
                        background='darkblue',
                        foreground='white', 
                        borderwidth=2, 
                        date_pattern = 'yyyy-mm-dd')
date_entry.grid(row=0, column=1, sticky='w', pady=5, padx=5)

#Getting the date function
def get_date():
    selected_date = date_entry.get()
#Button to test date function:
#ttk.Button(left_subframe, text='Select date', command=get_date).grid(row=1, column=0, columnspan=1, pady=5)

#Select currency field
ttk.Label(left_subframe, text='Currency:').grid(row=1, column=0, sticky='e', pady=5)
currency_options = ['MXN', 'USD']
currency_combo = ttk.Combobox(left_subframe, values=currency_options, state='readonly', width=5)
currency_combo.grid(row=1, column=1, pady=5, padx=5, sticky='w')
currency_combo.set('MXN') #default value



#Creating the Income input field
#Function that allow user to only input numbers and act similar to a cash register
def format_input(event):
    value = income_entry.get().replace('.', '').replace(',', '')
    if event.char.isdigit():
        value = (value + event.char)[-8:]
    elif event.keysym == 'BackSpace':
        value = value[:-1]
    else:
        return 'break'
#Add the point automatically after cents
    value = value.lstrip('0') or '0'
    if len(value) <=3:
        value = value.zfill(3) #Fill with 0 on the left of less than 3 digits including cents
    formatted = f'{int(value[:-2]):,}.{value[-2:]}' 
#Delete current input and replace with the new formatted one
    income_entry.delete(0, tk.END)
    income_entry.insert(0, formatted)
    return 'break'

#Field Label
ttk.Label(left_subframe, text='Income: $').grid(row=2, column=0, sticky='e', pady=5)

#Defining the income_entry variable
income_entry = ttk.Entry(left_subframe, width=15, justify='right')
income_entry.grid(row=2, column=1, padx=5, pady=5, sticky='w')
income_entry.insert(0, '0.00')
income_entry.bind('<KeyPress>', format_input)


#Description field
ttk.Label(left_subframe, text='Income Details:').grid(row=3, column=0, columnspan=2, sticky='w',pady=5)  
description_text = tk.Text(left_subframe, width=20, height=5, wrap='word')
#Used .Text instead of .Entry because Entry won't allow height option
description_text.grid(row=4, column=0, columnspan=2, sticky='w', pady=5)


#Right subframe fields
#Need to think of some things before coding this section (november 8th)
#Categories must support nesting and dynamic changes (adding or deleting a categorie)
#Should validate that percentages won't exceed the parent percentage
#Should be able to save/load categorie presets
#Need to be careful of extensibility for future charting or allow multiple profiles
#Scroll support if added a lot of categories

ttk.Label(right_subframe, text='Preset:').grid(row=0, column=0, pady=5, sticky='w')
preset_names = [preset_data['preset_name']]
#Selecting the preset from a combobox thats read from default.json
preset_combo = ttk.Combobox(right_subframe, values = preset_names, state='readonly', width=15)
preset_combo.grid(row=0, column=1, pady=5, sticky='w')
preset_combo.set(preset_names[0]) #set default

#Select preset function
def preset_selected(event):
    selected_name = preset_combo.get()
preset_combo.bind('<<ComboboxSelected>>', preset_selected)

#Function for dynamic labels depending on the preset.
category_labels = []

def show_categories(categories):
    #First clear labels
    for i in category_labels:
        i.destroy() #need to destroy each label, one by one
    category_labels.clear() #then clears the list

    #add new labels 
    



#Test button
#add_button = ttk.Button(main_frame, text='Test Button')
#add_button.pack(pady=5)

#Runs the mainloop (show main window)
root.mainloop()

 