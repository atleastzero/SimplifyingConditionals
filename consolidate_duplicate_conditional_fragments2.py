# By Kami Bigdely-Shamloo
# Consolidate duplicate conditional fragments
# This program changes car's gear according to the car speed. Then it
# displays the updated gear on the car's front panel.

def change_gear(str_gear):
    print("Gear changed to", str_gear)

def display_gear(str_gear):
    print("displayed gear:", str_gear)

def change_and_display_gear(str_gear):
    change_gear(str_gear)
    display_gear(str_gear)

def process_speed(speed):
    if 0 <= speed < 30:
        change_and_display_gear('1')
    elif 30 <= speed < 50:
        change_and_display_gear('2')
    elif 50 <= speed <= 90:
        change_and_display_gear('3')
    elif 90 <= speed:
        change_and_display_gear('4')
    elif speed <= 0:
        display_gear('R')

if __name__ == "__main__":
    process_speed(40)
