#Importing tkinter for easy GUI
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry

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
left_subframe = ttk.Frame(main_frame, padding=20)
left_subframe.pack(side='left', fill='both', expand=True)

#Rifht side subframe: data entry for categories, like rent, food, hobbies and percentages per each one.
right_subframe = ttk.Frame(main_frame, padding=20)
right_subframe.pack(side='right', fill='both', expand=True)


#Creating lef side subframe data input fields. 
#Date field
ttk.Label(left_subframe, text='Date:').grid(row=0, column=0, sticky='w', pady=5)
date_entry = DateEntry(left_subframe,
                        width=12,
                        background='darkblue',
                        foreground='white', 
                        borderwidth=2, 
                        date_pattern = 'yyyy-mm-dd')
date_entry.grid(row=0, column=1, pady=5, padx=5)

#Getting the date function
def get_date():
    selected_date = date_entry.get()
#Button to test date function:
#ttk.Button(left_subframe, text='Select date', command=get_date).grid(row=1, column=0, columnspan=1, pady=5)

#Select currency field
ttk.Label(left_subframe, text='Currency').grid(row=1, column=0, sticky='w', pady=5)
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
income_entry.grid(row=2, column=1, padx=5, pady=5)
income_entry.insert(0, '0.00')
income_entry.bind('<KeyPress>', format_input)








#Test button
#add_button = ttk.Button(main_frame, text='Test Button')
#add_button.pack(pady=5)

#Runs the mainloop (show main window)
root.mainloop()

 