import tkinter as tk
from tkinter import *

from funcs_for_checking_punctuation import (сhecking_correctness_of_login,
                                            checking_correctness_of_password)
from classes1 import User

# Initialize the main application window with title and fixed size
window = tk.Tk()
window.title('Registration/Login')  # Window title shown in the window's title bar
window.geometry('650x350')  # Set fixed window size (width x height in pixels)

# Global list to hold the current username and password input by the user
user_data = []

# Global references to Entry widgets (for username and password input fields)
txt_log = None
txt_pass = None

# Global references to Label widgets that display validation error messages
lbl_err_login = None       # For registration login errors
lbl_err_password = None    # For registration password errors
lbl_err_password_log = None  # For login form error messages (e.g., invalid credentials)

# Frames to hold Registration and Login UI elements separately
frame_reg = tk.Frame(window)
frame_log = tk.Frame(window)


# --- Function: get_usrname_password ---
# Purpose: Retrieve the current text input from the username and password fields.
# Returns: List [username, password] if both fields are non-empty; otherwise None.
def get_usrname_password():
    res1 = "{}".format(txt_log.get())  # Read current text from username Entry widget
    res2 = "{}".format(txt_pass.get())  # Read current text from password Entry widget
    if res1 == '' or res2 == '':
        # If either field is empty, do not return data (prevents processing incomplete input)
        pass
    else:
        # Return the username and password as a list
        return [res1, res2]


# --- Function: on_submit_reg ---
# Purpose: Handles "Submit" button click on the Registration form.
# Actions:
# 1. Retrieves user inputs.
# 2. Clears previous error messages.
# 3. Validates username and password format.
# 4. Displays error messages if validation fails.
# 5. Calls User.registration() if validation passes.
def on_submit_reg():
    global user_data, lbl_err_login, lbl_err_password

    user_data = get_usrname_password()  # Get input data from Entry fields

    # Clear any previous error messages displayed on the form
    lbl_err_login.config(text='')
    lbl_err_password.config(text='')

    # Validate username and password using external checking functions
    valid_login, err_login = сhecking_correctness_of_login(user_data[0])
    valid_password, err_password = checking_correctness_of_password(user_data[1])

    # Show validation error messages if validation failed
    if not valid_login:
        lbl_err_login.config(text=err_login)
    if not valid_password:
        lbl_err_password.config(text=err_password)

    # If both inputs are valid, proceed with user registration (e.g., store in database)
    if valid_login and valid_password:
        User.registration(user_data[0], user_data[1])
        print("Successful registration:", user_data)

    print(user_data)  # For debugging/logging purpose


# --- Function: on_submit_log ---
# Purpose: Handles "Submit" button click on the Login form.
# Actions:
# 1. Retrieves user inputs.
# 2. Clears previous login error message.
# 3. Checks if inputs are empty; if so, shows prompt to enter both.
# 4. Attempts user login by calling User.logining().
# 5. Displays error message if login fails.
def on_submit_log():
    global user_data, lbl_err_password_log

    user_data = get_usrname_password()  # Get input data from Entry fields

    lbl_err_password_log.config(text='')  # Clear previous login error message

    print(user_data)  # For debugging/logging purpose

    # If username or password is missing, notify user to enter both fields
    if not user_data or not user_data[0] or not user_data[1]:
        lbl_err_password_log.config(text='Please enter both login and password')
        return

    # Call the login method which checks credentials in the backend/database
    success = User.logining(user_data[0], user_data[1])

    # If login fails (wrong username/password), display an error message
    if not success:
        lbl_err_password_log.config(text='Invalid login or password')


# --- Function: clear_frames ---
# Purpose: Hide both Registration and Login frames.
# Called before displaying a frame to ensure only one form is visible at a time.
def clear_frames():
    frame_reg.forget()
    frame_log.forget()


# --- Function: reg_frame ---
# Purpose: Setup and display the Registration form.
# Actions:
# - Clears existing frame content to reset UI.
# - Creates input fields for username and password.
# - Creates labels for displaying validation error messages.
# - Adds a Submit button that triggers registration logic.
def reg_frame():
    clear_frames()  # Hide other frames
    frame_reg.pack(expand=True, fill='both')  # Show registration frame and allow it to expand

    # Remove all widgets currently in the registration frame (clears old UI)
    for widget in frame_reg.winfo_children():
        widget.destroy()

    # Title label for the registration form
    tk.Label(frame_reg, text='Registration').pack(pady=10)

    global txt_log, txt_pass, lbl_err_password, lbl_err_login

    # Username label and input field
    tk.Label(frame_reg, text='Login').pack(pady=6)
    txt_log = Entry(frame_reg, width=30)
    txt_log.pack(pady=5)

    # Label for login error messages (initially empty)
    lbl_err_login = tk.Label(frame_reg, text='', fg='red')
    lbl_err_login.pack(pady=2)

    # Password label and input field
    tk.Label(frame_reg, text='Password').pack(pady=6)
    txt_pass = Entry(frame_reg, width=30)
    txt_pass.pack(pady=5)

    # Label for password error messages (initially empty)
    lbl_err_password = tk.Label(frame_reg, text='', fg='red')
    lbl_err_password.pack(pady=2)

    # Submit button which triggers the registration validation and process
    tk.Button(frame_reg, text='Submit', command=on_submit_reg).pack(pady=20)


# --- Function: log_frame ---
# Purpose: Setup and display the Login form.
# Actions:
# - Clears existing frame content to reset UI.
# - Creates input fields for username and password.
# - Creates label for login error messages (e.g., incorrect password).
# - Adds a Submit button that triggers login logic.
def log_frame():
    clear_frames()  # Hide other frames
    frame_log.pack(expand=True, fill='both')  # Show login frame and allow it to expand

    # Remove all widgets currently in the login frame (clears old UI)
    for widget in frame_log.winfo_children():
        widget.destroy()

    # Title label for the login form
    tk.Label(frame_log, text='Login').pack(pady=10)

    global txt_log, txt_pass, lbl_err_password_log

    # Username label and input field
    tk.Label(frame_log, text='Login').pack(pady=6)
    txt_log = Entry(frame_log, width=30)
    txt_log.pack(pady=5)

    # Password label and input field
    tk.Label(frame_log, text='Password').pack(pady=6)
    txt_pass = Entry(frame_log, width=30)
    txt_pass.pack(pady=5)

    # Label for login error messages (e.g., invalid credentials)
    lbl_err_password_log = tk.Label(frame_log, text='', fg='red')
    lbl_err_password_log.pack(pady=2)

    # Submit button which triggers the login validation and process
    tk.Button(frame_log, text='Submit', command=on_submit_log).pack(pady=20)


# --- Main Menu UI ---
# This frame contains two buttons to switch between Registration and Login forms.
frame_menu = tk.Frame(window, bg='lightblue')
frame_menu.pack(side='top', fill='x', pady=10)

# Button to open the Registration form
tk.Button(frame_menu, text='Registration', command=reg_frame).pack(side='left', padx=10)

# Button to open the Login form
tk.Button(frame_menu, text='Login', command=log_frame).pack(side='left', padx=10)


# Start the Tkinter event loop, waiting for user interaction
window.mainloop()
