
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


import json

# Open the file and load JSON data into a Python dictionary
def get_json_data(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def main():
    data = get_json_data("application.json")
    return 0