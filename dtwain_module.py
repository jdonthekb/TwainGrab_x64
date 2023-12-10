import datetime
import os
import os.path
import ctypes
from ctypes import *
from ctypes import windll
import tkinter.messagebox as messagebox
import imageio
import sys
import dtwain

# Define your conditions
USE_UNICODE = True
USE_64_BIT = True

# Conditional imports based on the conditions
if USE_UNICODE:
    if USE_64_BIT:
        dtwain_dll = "./dtwain64u.dll"
        dtwain_lib = "./dtwain64u.lib"
        dtwain_pdb = "./dtwain64u.pdb"
        dtwain_ini = "./dtwain64u.ini"
        twain_info = "./twaininfo.txt"
        twain_language = "./twainlanguage.txt"
        twain_resource_strings = "./twainresourcestrings_english.txt"
    else:
        dtwain_dll = "./dtwain32u.dll"
        dtwain_lib = "./dtwain32u.lib"
        dtwain_pdb = "./dtwain32u.pdb"
        dtwain_ini = "./dtwain32u.ini"
        twain_info = "./twaininfo.txt"
        twain_language = "./twainlanguage.txt"
        twain_resource_strings = "./twainresourcestrings_english.txt"
else:
    if USE_64_BIT:
        dtwain_dll = "./dtwain64.dll"
        dtwain_lib = "./dtwain64.lib"
        dtwain_pdb = "./dtwain64.pdb"
        dtwain_ini = "./dtwain64.ini"
        twain_info = "./twaininfo.txt"
        twain_language = "./twainlanguage.txt"
        twain_resource_strings = "./twainresourcestrings_english.txt"
    else:
        dtwain_dll = "./dtwain32.dll"
        dtwain_lib = "./dtwain32.lib"
        dtwain_pdb = "./dtwain32.pdb"
        dtwain_ini = "./dtwain32.ini"
        twain_info = "./twaininfo.txt"
        twain_language = "./twainlanguage.txt"
        twain_resource_strings = "./twainresourcestrings_english.txt"

# Now, you can use the dtwain module in your code, and it will refer to the correct version
# dtwain.some_function()

def convert_bmp_to_jpeg(directory, quality=100):
    for filename in os.listdir(directory):
        if filename.endswith(".bmp"):
            bmp_path = os.path.join(directory, filename)
            jpeg_path = os.path.join(directory, os.path.splitext(filename)[0])# + ".jpg")

            # Read the BMP image using imageio
            img = imageio.imread(bmp_path)

            # Save the image as JPEG with specified quality
            imageio.imwrite(jpeg_path, img, format="JPEG", quality=quality)

            # Delete the original BMP file
            os.remove(bmp_path)

def get_formatted_datetime():
    now = datetime.datetime.now()
    formatted_date = now.strftime("%m%d%Y-%H%M%S-")
    print(formatted_date)
    return formatted_date

def generate_filename(tags_list, name):
    # name = app.Entry2.get() # get our name from the input field | if there was a gui this is what we would use
    print("Name: " + name) # display to console
    formatted_tags = '-'.join(tags_list) # Join the tags
    current_time = get_formatted_datetime() # get current time | to stamp filename
    file_name = f"{current_time}{name}-{formatted_tags}.jpg" if name else f"{current_time}{formatted_tags}.jpg"
    print("Filename: " + file_name)
    return file_name

def show_twain_error_message():
    messagebox.showerror("Twain Device Error: No TWAIN Device Found!", "No Twain Devices Found. \nContact your system administrator to install a Twain driver.")

def acquire_image():
    pass