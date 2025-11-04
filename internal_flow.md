# Internal Flow - Viera's Personal Savings App

## Flow Overview

The app starts in `main.py` and interacts with the modules `savings.py` and `database.py`. Below is a view of the internal flow:

User opens app

Select profile --- `database.py` load or create user data

Select saving preset --- `savings.py` load preset percentages

Edit preset (optional) --- `savings.py` modify categories and percentages

Save preset --- `database,py` save preset changes

Enter income --- `savings.py` calculate allocations

Display result --- `main.py` show updated balances per category

Notes:
- all data persistence (profiles, presets, income history) is handled by `database.py`
- `savings.py` contains all calculations and manipulations related do presets and allocations
- `main.py` handles user interaction and orchestrates the flow.


## Pseudocode
```python
    def main():
        user = selerc_or_create_user()  #database.py
        preset = select_preset(user)    #database.py / savings.py
        preset = edit_preset(preset)    #savings.py
        save_preset(user, preset)       #database.py
        income = get_income_from_user() #main.py
        updated_balances = allocate_income(income, preset) #savings.py
        show_result(updated_balances)   #main.py
```
## Technical Considerations
Store categories as rows in the database instead of columns to allow user-defined categories.

``` python
#database.py
save_user(user_data)
load_user(user_id)
save_preset(user_id, preset_dict)
load_preset(user_id)
```
