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
ttk.Label(left_subframe, text='Date').grid(row=0,column=0,sticky='w',pady=5)
date_entry = DateEntry(left_subframe, width=12, background='darkblue', foreground='white', borderwidth=2)
date_entry.grid(row=0, column=1, pady=5, padx=5)
selected_date = date_entry.get()
print(selected_date)





#Test button
#add_button = ttk.Button(main_frame, text='Test Button')
#add_button.pack(pady=5)

#Runs the mainloop (show main window)
root.mainloop()
