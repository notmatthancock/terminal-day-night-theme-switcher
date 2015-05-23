term_theme_switch_path=/Users/macuser/scratch/terminal_day_night_theme_switcher/src
theme=$(python $term_theme_switch_path/get_theme.py tallahasse, fl)
osascript $term_theme_switch_path/change_theme.applescript $theme
