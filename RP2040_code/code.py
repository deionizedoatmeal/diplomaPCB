# diplomaPCB firmware v0.8
# GPLv3 applies
# ian k. bania, may 2022

#################
### LIBRARIES ###
#################
import board
import busio
import neopixel
import digitalio
import analogio
import adafruit_pcf8591.pcf8591 as PCF
from adafruit_pcf8591.analog_in import AnalogIn
from adafruit_pcf8591.analog_out import AnalogOut
from random import randrange

#################
### FUNCTIONS ###
#################
def set_7seg_disp(first_digit: int, second_digit: int):
    """writes the proper year to the 7 seg displays"""
    # set the component LEDs of 7 segment display
    if second_digit == 0:
        ones_A = True
        ones_B = True
        ones_C = False
        ones_D = True
        ones_E = True
        ones_F = True
        ones_G = False 
    
    if second_digit == 1:
        ones_A = False 
        ones_B = True
        ones_C = True
        ones_D = False
        ones_E = False
        ones_F = False
        ones_G = False 

    if second_digit == 2:
        ones_A = True 
        ones_B = True
        ones_C = False
        ones_D = True
        ones_E = True
        ones_F = False
        ones_G = True 

    if second_digit == 3:
        ones_A = True 
        ones_B = True
        ones_C = True
        ones_D = True
        ones_E = False
        ones_F = False
        ones_G = True 

    if second_digit == 4:
        ones_A = True 
        ones_B = True
        ones_C = True
        ones_D = False
        ones_E = False
        ones_F = False
        ones_G = True 

    if second_digit == 5:
        ones_A = True 
        ones_B = False
        ones_C = True
        ones_D = True
        ones_E = False
        ones_F = True
        ones_G = True 

    if second_digit == 6:
        ones_A = True 
        ones_B = False
        ones_C = True
        ones_D = True
        ones_E = True
        ones_F = True
        ones_G = True 

    if second_digit == 7:
        ones_A = True 
        ones_B = True
        ones_C = True
        ones_D = False
        ones_E = False
        ones_F = False
        ones_G = False

    if second_digit == 8:
        ones_A = True 
        ones_B = True
        ones_C = True
        ones_D = True
        ones_E = True
        ones_F = True
        ones_G = True 

    if second_digit == 9:
        ones_A = True 
        ones_B = True
        ones_C = True
        ones_D = True
        ones_E = False 
        ones_F = True
        ones_G = True 

    if first_digit == 0:
        tens_A = True
        tens_B = True
        tens_C = False
        tens_D = True
        tens_E = True
        tens_F = True
        tens_G = False 
    
    if first_digit == 1:
        tens_A = False 
        tens_B = True
        tens_C = True
        tens_D = False
        tens_E = False
        tens_F = False
        tens_G = False 

    if first_digit == 2:
        tens_A = True 
        tens_B = True
        tens_C = False
        tens_D = True
        tens_E = True
        tens_F = False
        tens_G = True 

    if first_digit == 3:
        tens_A = True 
        tens_B = True
        tens_C = True
        tens_D = True
        tens_E = False
        tens_F = False
        tens_G = True 

    if first_digit == 4:
        tens_A = True 
        tens_B = True
        tens_C = True
        tens_D = False
        tens_E = False
        tens_F = False
        tens_G = True 

    if first_digit == 5:
        tens_A = True 
        tens_B = False
        tens_C = True
        tens_D = True
        tens_E = False
        tens_F = True
        tens_G = True 

    if first_digit == 6:
        tens_A = True 
        tens_B = False
        tens_C = True
        tens_D = True
        tens_E = True
        tens_F = True
        tens_G = True 

    if first_digit == 7:
        tens_A = True 
        tens_B = True
        tens_C = True
        tens_D = False
        tens_E = False
        tens_F = False
        tens_G = False

    if first_digit == 8:
        tens_A = True 
        tens_B = True
        tens_C = True
        tens_D = True
        tens_E = True
        tens_F = True
        tens_G = True 

    if first_digit == 9:
        tens_A = True 
        tens_B = True
        tens_C = True
        tens_D = True
        tens_E = False 
        tens_F = True
        tens_G = True 
    return

def fall_sup_check():
    """updates the LEDs of any supply centers who are ocupied by a color than what the show"""
    for i in range(len(sup_pixels)):
        # color the supply center currently is
        color = old_current_LED[i]

        # color of piece currently occupying supply center 
        piece = get_sup_piece(supply_center_TPs[i])
        
        # create a new list
        current_LED[i] = piece

        if color == piece or piece == none:
            # no ownership change, check next LED
            continue
        elif color != piece:
            # onwership has changed, set color to match
            sup_pixels[i] = piece
    return

def get_sup_piece(sup_center):
    """uses ADC to retrieve the color the piece on a supply center"""
    # returns color based on voltage, voltages are:
    # 0.000 V -> none   => 1 MΩ
    # 0.471 V -> red    => 60 kΩ 
    # 0.943 V -> green  => 25 kΩ
    # 1.414 V -> blue   => 13.4 kΩ
    # 1.886 V -> purple => 7.5 kΩ
    # 2.357 V -> yellow => 4 kΩ
    # 2.829 V -> orange => 1.7 kΩ
    # 3.300 V -> white  => 0 Ω
    # get voltage
    if sup_center == sup5 or sup_center == sup6 or sup_center == sup34:
        # AVG over time!!!
        voltage = RPv * sup_center.value * sup_center.reference_voltage
    else:
        # AVG over time!!!
        voltage = PCFv * sup_center.value * sup_center.reference_voltage

    # use voltage to get color
    if voltage < min_voltage:
        return none
    if voltage >= min_voltage and voltage < 0.707:
        return red
    if voltage >= 0.707 and voltage < 1.179:
        return green
    if voltage >= 1.179 and voltage < 1.650:
        return blue
    if voltage >= 1.650 and voltage < 2.122:
        return purple
    if voltage >= 2.122 and voltage < 2.593:
        return yellow
    if voltage >= 2.593 and voltage < 3.065:
        return orange
    if voltage >= 3.065:
        return white
    else:
        return "error"


##################################
### GLOBALS AND INITIALIZATION ###
##################################
# define RGB colors to use
# feel free to change these if you want
red = (255, 0, 15)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (255, 0, 255)
yellow = (255, 255, 0)
orange = (230, 99, 0)
# adjusted for specific LEDs
white = (200, 255, 200)
none = (0, 0, 0)

colors = [red, green, blue, purple, yellow, orange, white]

# define LED brightness, 0 -> 1 float, feel free to change
brightness = 0.1

# min
min_voltage = 0.2

# RP2040 voltage calibration factor
RPv = 1/65535

# PCF8591 voltage calibration factor
PCFv = 1/65535

# define the RGB LEDs
sup_pixels = neopixel.NeoPixel(board.GP6, 34)
season_pixels = neopixel.NeoPixel(board.GP2, 3)
sup_pixels.brightness = brightness
season_pixels.brightness = brightness

# define the buttons
next_season = digitalio.DigitalInOut(board.GP4)
next_season.switch_to_input(pull=digitalio.Pull.DOWN)

prev_season = digitalio.DigitalInOut(board.GP5)
prev_season.switch_to_input(pull=digitalio.Pull.DOWN)

restart = digitalio.DigitalInOut(board.GP3)
restart.switch_to_input(pull=digitalio.Pull.DOWN)

# define the analog pins
sup5 =  analogio.AnalogIn(board.GP26)
sup6 =  analogio.AnalogIn(board.GP27)
sup34 =  analogio.AnalogIn(board.GP28)

# set up ADCs using I2C logic pins
i2c = busio.I2C(scl=board.GP1, sda=board.GP0)

# first PCF8591 IC (top L board)
ADC_1 = PCF.PCF8591(i2c, 0x48)
sup1 = AnalogIn(ADC_1, PCF.A0)
sup2 = AnalogIn(ADC_1, PCF.A1)
sup3 = AnalogIn(ADC_1, PCF.A2)
sup4 = AnalogIn(ADC_1, PCF.A3)

# second PCF8591 IC (top R board)
ADC_2 = PCF.PCF8591(i2c, 0x49)
sup7 = AnalogIn(ADC_2, PCF.A0)
sup8 = AnalogIn(ADC_2, PCF.A1)
sup9 = AnalogIn(ADC_2, PCF.A2)

# third PCF8591 IC (bottom L board)
ADC_3 = PCF.PCF8591(i2c, 0x4A)
sup10 = AnalogIn(ADC_3, PCF.A0)
sup11 = AnalogIn(ADC_3, PCF.A1)
sup12 = AnalogIn(ADC_3, PCF.A2)
sup13 = AnalogIn(ADC_3, PCF.A3)

# forth PCF8591 IC (bottom L board)
ADC_4 = PCF.PCF8591(i2c, 0x4C)
sup14 = AnalogIn(ADC_4, PCF.A0)
sup15 = AnalogIn(ADC_4, PCF.A1)
sup16 = AnalogIn(ADC_4, PCF.A2)
sup17 = AnalogIn(ADC_4, PCF.A3)

# fifth PCF8591 IC (bottom L board)
ADC_5 = PCF.PCF8591(i2c, 0x4B)
sup18 = AnalogIn(ADC_5, PCF.A0)
sup19 = AnalogIn(ADC_5, PCF.A1)
sup20 = AnalogIn(ADC_5, PCF.A2)
sup21 = AnalogIn(ADC_5, PCF.A3)

# sixth PCF8591 IC (bottom R board)
ADC_6 = PCF.PCF8591(i2c, 0x4D)
sup22 = AnalogIn(ADC_6, PCF.A0)
sup23 = AnalogIn(ADC_6, PCF.A1)
sup24 = AnalogIn(ADC_6, PCF.A2)
sup25 = AnalogIn(ADC_6, PCF.A3)

# seventh PCF8591 IC (bottom R board)
ADC_7 = PCF.PCF8591(i2c, 0x4E)
sup26 = AnalogIn(ADC_7, PCF.A0)
sup27 = AnalogIn(ADC_7, PCF.A1)
sup28 = AnalogIn(ADC_7, PCF.A2)
sup29 = AnalogIn(ADC_7, PCF.A3)

# eighth PCF8591 IC (bottom R board)
ADC_8 = PCF.PCF8591(i2c, 0x4F)
sup30 = AnalogIn(ADC_8, PCF.A0)
sup31 = AnalogIn(ADC_8, PCF.A1)
sup32 = AnalogIn(ADC_8, PCF.A2)
sup33 = AnalogIn(ADC_8, PCF.A3)

supply_center_TPs = [sup1, sup2, sup3, sup4, sup5, sup6, sup7, sup8, sup9, sup10, sup11, sup12, sup13, sup14, sup15, sup16, sup17, sup18, sup19, sup20, sup21, sup22, sup23, sup24, sup25, sup26, sup27, sup28, sup29, sup30, sup31, sup32, sup33, sup34]

# set 7 segement display pins
tens_A = digitalio.DigitalInOut(board.GP7)
tens_A.direction = digitalio.Direction.OUTPUT

tens_B = digitalio.DigitalInOut(board.GP8)
tens_B.direction = digitalio.Direction.OUTPUT

tens_C = digitalio.DigitalInOut(board.GP9)
tens_C.direction = digitalio.Direction.OUTPUT

tens_D = digitalio.DigitalInOut(board.GP10)
tens_D.direction = digitalio.Direction.OUTPUT

tens_E = digitalio.DigitalInOut(board.GP11)
tens_E.direction = digitalio.Direction.OUTPUT

tens_F = digitalio.DigitalInOut(board.GP12)
tens_F.direction = digitalio.Direction.OUTPUT

tens_G = digitalio.DigitalInOut(board.GP13)
tens_G.direction = digitalio.Direction.OUTPUT

ones_A = digitalio.DigitalInOut(board.GP14)
ones_A.direction = digitalio.Direction.OUTPUT

ones_B = digitalio.DigitalInOut(board.GP15)
ones_B.direction = digitalio.Direction.OUTPUT

ones_C = digitalio.DigitalInOut(board.GP16)
ones_C.direction = digitalio.Direction.OUTPUT

ones_D = digitalio.DigitalInOut(board.GP17)
ones_D.direction = digitalio.Direction.OUTPUT

ones_E = digitalio.DigitalInOut(board.GP18)
ones_E.direction = digitalio.Direction.OUTPUT

ones_F = digitalio.DigitalInOut(board.GP19)
ones_F.direction = digitalio.Direction.OUTPUT

ones_G = digitalio.DigitalInOut(board.GP20)
ones_G.direction = digitalio.Direction.OUTPUT

# initalize season and year counting
# counter % 3 is the season, 1 = spring, 2 = fall, 0 = winter
# counter // 3 is the year, 0 = 1901, 1 = 1902, etc
counter = 0

# calc year and season
season = counter % 3
year = counter // 3

# initalize current color list and set all LEDs to off
sup_pixels.fill(none)
for i in range(len(sup_pixels)):
    sup_pixels[i] = colors[randrange(7)]

# current color list initiation
current_LED = []
for i in range(34):
    current_LED.append(none)

# initalize turn history
# turn history is list of lists: [[counter1, [color1, color2, color3, ...]],  [counter2, [color1, color2, color3, ...]], ... ]
history = [counter, current_LED]

# initalize toggle variable
toggle = False

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True


#################
### MAIN LOOP ###
#################
while True:
    # set date displays
    ones = str(1901 + year)[3]
    tens = str(1901 + year)[2]
    set_7seg_disp(tens, ones)

    # set the appropriate season indicator turn off the others
    season_pixels[(season)%3] = white
    season_pixels[(season - 1)%3] = none
    season_pixels[(season - 2)%3] = none 

    # if the restart button is toggled
    if restart.value:
        # check if we've been thru this loop this toggle
        if toggle == True:
            continue

        # if first time in the loop set the toggle variable
        toggle = True

        # reset the counter (this resets the date display
        counter = 0
        season = counter % 3
        year = counter // 3

        # turn supply center LEDs off
        sup_pixels.fill(none)

        # reset the current color list
        current_LED = []
        for i in range(34):
            current_LED.append(none)

        # clear and reset the turn history list
        history = [] 
        history = [counter, current_LED]

        # ignore any coincidental press of next and prev
        continue

    # if the next button is toggled
    if next_season.value:
        # check if we've been thru this loop this toggle
        if toggle == True:
            continue

        # if first time in the loop set the toggle variable
        toggle = True

        # increment the season
        counter = counter + 1
        season = counter % 3
        year = counter // 3
        
        # if we are moving fall -> winter
        if season == 2:
            old_current_LED = current_LED

            # check supply centers to see if their ownership has changed
            fall_sup_check()

            # add old current list to history
            history.append([counter, old_current_LED])

        # ignore any coincidental press of prev
        continue
            
    # if the previous button is toggled
    if prev_season.value:
        # check if we've been thru this loop this toggle
        if toggle == True:
            continue

        # if first time in the loop set the toggle variable
        toggle = True

        # decrement the season
        counter = counter - 1
        season = counter % 3
        year = counter // 3

        # check to see if we need to regress the supply centers 
        if season == 1:
            # then get the supply center colors for this value in the list
            for i in range(len(history[-1][1])):
                sup_pixels[i] = history[-1][1][i]

            # now remove this value from history
            history.pop()
        continue

    # if no button is depressed
    else:
        toggle = False
        

