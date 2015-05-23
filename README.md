# Day / Night Theme Switcher for MAC OS X Terminal

Change the theme of your terminal based on whether it is day or night at your current location!

## Dependencies, setup, etc...

### Overview

A bash script calls a python script that determines whether it is day or night. The python script yields, "Day" or "Night", which is used as an argument to applescript that changes the theme of all open terminal tabs and windows accordingly.

You must have themes in Terminal named "Day" and "Night" for this to work.

### Getting the Theme
The python script executes, `./src/get_theme.py my location`, which queries google to determine the time of sunrise and sunset. It searches google based on the value of "my location". This must be changed in `src/main.sh` toyour location. The script opens the url with the `requests` library and parses the result with `pyquery`. Therefore, run

    pip install requests
    pip install pyquery

if you do not have these already installed.

This is a couple of scripts that query google for the times of sunrise and sunset in your area, and then use this information to set the theme of all open terminal windows to "Day" or "Night" depending on the local time. Of course, "Day" and "Night" themes must exist in your Terminal app.
