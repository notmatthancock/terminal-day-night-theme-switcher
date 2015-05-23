# OS X Terminal Day-Night Theme Switcher

Automatically change the theme of your terminal based on whether it is day or night at your current location! This was developed under 10.6 (I know - my laptop is old). It should work under new versions but has not been tested.

![A Night Theme and Day Theme](https://raw.githubusercontent.com/chestervonwinchester/terminal-day-night-theme-switcher/master/screenshot.png)

## Setup

First grab the repository

    git clone https://github.com/chestervonwinchester/terminal-day-night-theme-switcher.git

and move it to wherever you would like its final location to be, called `path/to/switcher` throughout. You must have a working version of python, with `requests` and `pyquery` libraries installed. If not, install them:

    pip install requests
    pip install pyquery

You must have themes named "Day" and "Night" defined in Terminal. Go to Terminal > Preferences and define them. I prefer to work in a light theme in the day and dark at night.

Edit the file `path/to/switcher/src/main.sh`. Set the variable `term_theme_switch=path/to/switcher/src` in line 1.

Edit `path/to/switcher/src/main.sh` in line 2. Change \*my location\* to your location (caps dont really matter). For example, this line might read:

    theme=$(python get_theme.py miami, fl)

Finally, you should add `path/to/switcher/src/main.sh` to your crontab.

    crontab -e

Then add:

    0 * * * * path/to/switcher/src/main.sh

This will run every hour, and set your theme accordingly!
