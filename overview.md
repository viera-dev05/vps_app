# Viera's Personal Savings App - Overview

## Preface 
November 3, 2025. 

This is my very first python project, in fact, my first coding project in general. My name's Abraham Viera, 33 years old, and am a language teacher and an academic coordinator at a language school in Mexico. I'm learning to code "in secret" to switch jobs and, maybe, get a better one...

I started learning code on October 27, 2025 (7 days ago). I finished "Intro to Programming" and "Python" course at Kaggle.com, made some challenges at Exercism.org and now, trying to jump right at creating stuff.

I'll be honest, I'll be using a lot of AI to learn to write code, but I will do my best to just ask for advice and write all on my own. 

By the way, the same day I began Kaggle's basic programming course, I enrolled in a virtual university in mexico, the UVEG, for a career in "Software Development Engineering" (also a secret to my coworkers). As it is a virtual school designed for people with jobs, we do only 1 module per month for a total of 41 modules. Although I got 3 modules credits right away thanks to my  admission test. 

I'm interested on "Data engineering", but choose a software developer degree because theres more options. My long term plan is still, to specialize in data engineering. 

If you read this, thank you. 


## Project Overview
Very simple app to calculate my personal savings. I usually do this on Excel or Google Sheets and wanted to make an app of it. My aim is to make an app able to determine savings based on the percentage I want to set for each category.

For example, from my 100% (in mexico each 15 days) I want to dedicate 50% to my daily life "needed" expenses, like rent, food, gas, etc. 30% to hobbies and 20% retirement savings. 

I want to be able to input the income, set the percentages I want, and the app should tell me how much I should deposit in each of my bank accounts. Would be awesome If I can store the data on each input, so I can track all my income and set "profiles" so I can switch between, maybe, family members and/or saving percentages presets. 


Pretty simple (I hope).

## Target Audience
Myself

## Main Functions
- Register income with date and description or source.
- Calculate balance and savings per category.
- Save percentage presets
- Add or remove categories
- Switch profiles (users)
- (maybe) Save the data in a data base. (JSON or SQLite recommended by Chatgpt).

## Project Structure
- `main.py` → entry point
- `savings.py` → register and calculation functions
- `overview.md` → structure, planification, and some background
- `README.md` → app specific info, without my nonsense
- add more if needed...

## General Flow
User opens app - Select profile - Set saving percentages or saving preset - Add or remove saving categories - Input income - Show results

## Future Considerations
- Save data base on SQLite
- Create GUI
- Add graphs
- Add a "savings objective" function, where you set an ammount and target time and calculates saving needed per month.
- Add saving projection graphs with or without positive interest (investments)
