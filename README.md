# OS X Terminal Day-Night Theme Switcher

Change the theme of your terminal based on whether it is day or night at your current location!

![A Night Theme and Day Theme](https://raw.githubusercontent.com/chestervonwinchester/terminal-day-night-theme-switcher/master/screenshot.png)

## Setup

First grab the repository

    git clone https://github.com/chestervonwinchester/terminal-day-night-theme-switcher.git

and move it to wherever you would like its final location to be. You must have a working version of python, with `requests` and `pyquery` libraries installed. If not, install them:

    pip install requests
    pip install pyquery

You must have themes named "Day" and "Night" defined in Terminal. Go to Terminal > Preferences and define them. I prefer to work in a light theme in the day and dark at night.

Edit the file `path/to/switcher/src/main.sh`. Set the variable `term_theme_switch=path/to/switcher/src` in line 1. This corresponds to where you moved the repository above.

Finally edit `path/to/switcher/src/main.sh` in line 2. Change *my location* to your location. For example, "miami, fl".


### Overview

A bash script calls a python script that determines whether it is day or night. The python script yields, "Day" or "Night", which is used as an argument to applescript that changes the theme of all open terminal tabs and windows accordingly.

You must have themes in Terminal named "Day" and "Night" for this to work.

### Getting the Theme
The python script executes, `./src/get_theme.py my location`, which queries google to determine the time of sunrise and sunset. It searches google based on the value of "my location". This must be changed in `src/main.sh` toyour location. The script opens the url with the `requests` library and parses the result with `pyquery`. Therefore, run

    pip install requests
    pip install pyquery

if you do not have these already installed.

This is a couple of scripts that query google for the times of sunrise and sunset in your area, and then use this information to set the theme of all open terminal windows to "Day" or "Night" depending on the local time. Of course, "Day" and "Night" themes must exist in your Terminal app.
