
# FLOW OF SOLUTION
# upon launch steam will be opened
# the program will then listen for the steam vr application to open
# once opened the application will open the following applications: 
# vrchat
# vive hub
# voicemeter banana

# REQUIREMENTS
# All applications (Other than startup) will have a dependency that will have to be running before launch
# All application data will be read from a 'application.json' file
# Code will detect wether application is a steam application or a regular exe
# Applucations will be given a startup time before atempting to launch the next one
# each application will have an 'amountOfAttemps' constant that will dictate when applications will timeout
# each application will have a constant of 5 seconds between each atempt of startup


#FUNCTIONS
# get_json_data(filePath) - returns the json data from the file path
# is_steamvr_running() - returns true if steamVR is running
# is_steam_application(appJson) - returns true if application is a steam application
# run_steam_application(appJson) - runs steam application based on the appJson data
# run_regular_application(appJson) - runs regular application based on the appJson data
# is_dependency_running(dependencyExe) - returns true if application is running based on the appJson data
# launch_applications(appList) - Handles the for loop launch each application after each other


# run_application(appJson) - runs the application based on if it is a steam application or not


import json
import subprocess
import time
import psutil
import logging


# Sets up logging to both a file and the console with different log levels
def setup_logging(logfile):

    # sets up logging to both a file and the console with different log levels
    file_handler = logging.FileHandler(logfile)
    file_handler.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Sets up the log format for both handlers
    formatter = logging.Formatter(
        '%(asctime)s [%(levelname)s] %(message)s',
        datefmt='%H:%M:%S'
    )

    # Assign the formatter to both handlers
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logging.basicConfig(level=logging.DEBUG, handlers=[file_handler, console_handler])

# Checks if SteamVR is running by looking for the vrmonitor.exe process
def is_steamvr_running():
    logging.info("Checking if SteamVR is running...")

    # Goes though all running processes and checks if vrmonitor.exe is running
    for process in psutil.process_iter(['processName']):
        if process.info['processName'] == "vrmonitor.exe":
            logging.info("SteamVR is running.")
            return True
    logging.warning("SteamVR is not running.")
    return False

# Checks if the application is a Steam application based on the appJson data
def is_steam_application(appJson):
    if appJson["appType"] == "steam":
        return True
    return False

# Runs a Steam application based on the appJson data
def get_json_data(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def main():
    global DEBUG
    DEBUG = True

    setup_logging('DEBUG.log')
    data = get_json_data("application.json")
    return 0