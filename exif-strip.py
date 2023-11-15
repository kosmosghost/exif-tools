#!/usr/bin/python


import sys
from exif import Image



def get_filename(filename):
    filename_to_return = open(filename, "rb")
    return filename_to_return

def translate_to_exif_data(image_file):
    image_file_to_return = Image(image_file)
    return image_file_to_return

def query_user_for_confirmation():
    user_input = input("Are you sure you want to delete all exif data? y/N? ")

    if user_input.lower() == "y":
        return True
    elif user_input.lower() == "n":
        return False
    else:
        print("Invalid choice.")
        print("Quitting...")
        quit()

def save_photo(image_filename, image_data):
    with open(image_filename, 'wb') as image_file:
        image_file.write(image_data.get_file())
    print("Modified Image saved over original")


def strip_all_exif_data(image_data):
    exif_data = image_data.get_all()
    for key in exif_data:
        image_data.delete(key)

def run_error_message_and_exit():
    print("Usage: exif-strip.py <filename>")
    quit()

def parse_args_and_get_filename():
    args = sys.argv
    if len(args) <= 1:
        run_error_message_and_exit()
    else:
        return sys.argv[1]

def get_image_file(image_filename):
    try:
        image_file_to_return = get_filename(image_filename)
        return image_file_to_return
    except:
        print("Error. Possible wrong filename?")
        run_error_message_and_exit()

def run_program():
    image_filename = parse_args_and_get_filename()
    image_file = get_image_file(image_filename)
    image_data = translate_to_exif_data(image_file)
    if query_user_for_confirmation() == True:
        strip_all_exif_data(image_data)
        save_photo(image_filename, image_data)
    else:
        print("EXIF DATA NOT CHANGED.")
        print("QUITTING...")
        quit()

run_program()