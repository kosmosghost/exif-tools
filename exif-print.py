#!/usr/bin/python

import sys
from exif import Image

def return_error_and_exit():
    print("Usage: exif-print.py [OPTION] [FILE]")
    quit()

def print_hardware_exif_tags(imagefile):
    hardware_list = ['make', 'model', 'orientation', 'x_resolution', 'y_resolution', 'resolution_unit', 'software', 'y_and_c_positioning', '_exif_ifd_pointer', 'exposure_time', 'f_number', 'exposure_program', 'photographic_sensitivity', 'exif_version', 'components_configuration', 'shutter_speed_value', 'aperture_value', 'brightness_value', 'exposure_bias_value', 'metering_mode', 'flash', 'focal_length', 'flashpix_version', 'color_space', 'pixel_x_dimension', 'pixel_y_dimension', 'sensing_method', 'scene_type', 'exposure_mode', 'white_balance', 'focal_length_in_35mm_film', 'scene_capture_type', 'lens_specification', 'lens_make', 'lens_model']
    exif_tags = imagefile.get_all()
    for i in hardware_list:
        try:
            print(i,":", exif_tags[i])
        except:
            print("no data")

def print_gps_exif_tags(imagefile): 
    gps_list = ['gps_latitude_ref', 'gps_latitude', 'gps_longitude_ref', 'gps_longitude', 'gps_altitude_ref', 'gps_altitude', 'gps_speed_ref', 'gps_speed', 'gps_img_direction_ref', 'gps_img_direction', 'gps_dest_bearing_ref', 'gps_dest_bearing', 'gps_horizontal_positioning_error', '_gps_ifd_pointer']
    exif_tags = imagefile.get_all()
    for i in gps_list:
        try:
            print(i,":", exif_tags[i])
        except:
            print("no data")

def print_all(imagefile):
    exif_tags = imagefile.get_all()
    for i in exif_tags:
        print(i,":", exif_tags[i])

def open_file(filename):
    try:
        filename_to_return = open(filename, 'rb')
        return filename_to_return
    except:
        print("Could not open", filename)
        return_error_and_exit()

def translate_to_exif(filename):
    try:
        imagefile_to_return = Image(filename)
        return imagefile_to_return
    except:
        print("Could not open Image file")
        return_error_and_exit()

def print_help():
    print("Usage: exif-print.py [OPTION] [FILE]")
    print("Option:")
    print("\t-a \tPrint all available data. This is the default.")
    print("\t-h \tPrint only hardware data")
    print("\t-g \tPrint location data")
    print("\t--help \tShow help")


def parse_argument_list(argument_list):
    parsed_list_to_return = {"hardware": False, "gps": False, "all": True}
    for i in argument_list:
        if i.lower() == "--help":
            print_help()
            quit()
        elif i.lower() == "-h":
            parsed_list_to_return["hardware"] = True
            parsed_list_to_return["all"] = False
        elif i.lower() == "-g":
            parsed_list_to_return["gps"] = True
            parsed_list_to_return["all"] = False
        elif i.lower() == "-a":
            parsed_list_to_return["all"] = True
        elif i != "exif-print.py":
            parsed_list_to_return["filename"] = i
        else:
            if i != "exif-print.py":
                print("Unable to process args")
                return_error_and_exit()
    return parsed_list_to_return
            
def process_and_print(parsed_argument_list):
    filename = open_file(parsed_argument_list["filename"])
    imagefile = translate_to_exif(filename)
    if imagefile.has_exif == False:
        print("No EXIF data present")
        quit()
    
    if parsed_argument_list['hardware'] == True:
        print_hardware_exif_tags(imagefile)
    if parsed_argument_list["gps"] == True:
        print_gps_exif_tags(imagefile)
    if parsed_argument_list["all"] == True:
        print_all(imagefile)
    

def run_program():
    argument_list = sys.argv
    parsed_argument_list = {}
    if len(argument_list) <= 1:
        return_error_and_exit()
    else:
        parsed_argument_list = parse_argument_list(argument_list)
        process_and_print(parsed_argument_list)

run_program()