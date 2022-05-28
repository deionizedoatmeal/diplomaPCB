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

##################################
### GLOBALS AND INITIALIZATION ###
##################################
# define RGB colors to use
# feel free to change these if you want
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (255, 0, 255)
yellow = (255, 255, 0)
orange = (255, 165, 0)
white = (255, 255, 255)
none = (0, 0, 0)

# define LED brightness, 0 -> 1 float, feel free to change
brightness = 0.3

# RP2040 voltage calibration factor
RPv = 3.3/65535

# PCF8591 voltage calibration factor
PCFv = 3.3/65535

# define the RGB LEDs
sup_pixels = neopixel.NeoPixel(board.GP6, 34)
season_pixels = neopixel.NeoPixel(board.GP2, 3)

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

# define the supply center LEDs
Edi = sup_pixels[0]
Lvp = sup_pixels[1]
Lon = sup_pixels[2]
Nwy = sup_pixels[3]
Den = sup_pixels[4]
Kie = sup_pixels[5]
Swe = sup_pixels[6]
StP = sup_pixels[7]
Mos = sup_pixels[8]
War = sup_pixels[9]
Sev = sup_pixels[10]
Ank = sup_pixels[11]
Con = sup_pixels[12]
Smy = sup_pixels[13]
Gre = sup_pixels[14]
Bul = sup_pixels[15]
Rum = sup_pixels[16]
Ser = sup_pixels[17]
Try = sup_pixels[18]
Bud = sup_pixels[19]
Ven = sup_pixels[20]
Nap = sup_pixels[21]
Rom = sup_pixels[22]
Tun = sup_pixels[23]
Mar = sup_pixels[24]
Spa = sup_pixels[25]
Por = sup_pixels[26]
Bre = sup_pixels[27]
Par = sup_pixels[28]
Bel = sup_pixels[29]
Ber = sup_pixels[30]
Mun = sup_pixels[31]
Ven = sup_pixels[32]
Hol = sup_pixels[33]

# list holding all the neopixel objects
supply_center_LEDs = [Edi, Lvp, Lon, Nwy, Den, Kie, StP, MoS, War, Sev, Ank, Con, Smy, Gre, Bul, Rum]

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
counter = 1

# initalize current color list and set all LEDs to off
sup_LEDs_off()
current_list = []
for i in range(34):
    current_LED.append(none)

# initalize turn history
# turn history is list of lists: [[counter1, [color1, color2, color3, ...]],  [counter2, [color1, color2, color3, ...]], ... ]
history = [counter, current_list]

#################
### FUNCTIONS ###
#################
def set_7seg_disp(year: int):
    """writes the proper year to the 7 seg displays"""
    actual_year = year + 1
    tens_digit = str(actual_year)[0]
    ones_digit = str(actual_year)[1]

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

def reset_history():
    """clears all past turn history"""
    history = [] 
    history = [counter, current_list]
    return

def fall_sup_check():
    """updates the LEDs of any supply centers who are ocupied by a color than what the show"""
    for i in range(len(supply_center_LEDs)):
        # color the supply center currently is
        color = get_sup_color(supply_center_LEDs[i], i)

        # piece currently occupying supply center 
        piece = get_sup_piece(supply_center_TPs[i])

        if color == piece or piece == none:
            # no ownership change, check next LED
            continue
        elif color != piece:
            # onwership has changed, set color to match
            set_sup_color(supply_center_LEDs[i], piece)
    return

def get_sup_color(sup_center, i):
    """retrieves the color a supply center is currently showing"""
    # returns: blue, green, red, orange, purple, white, yellow, none
    return current_list[i]

def get_sup_piece(sup_center):
    """retrieves the color the piece on a supply center"""
    # returns color based on voltage, voltages are:
    # 0.000 V -> none
    # 0.471 V -> red
    # 0.943 V -> green
    # 1.414 V -> blue
    # 1.886 V -> purple 
    # 2.357 V -> yellow
    # 2.829 V -> orange 
    # 3.300 V -> white 
    # get voltage
    if sup_center == sup5 or sup_center == sup6 or sup_center == sup34:
        voltage = RPv * sup_center
    else:
        voltage = PCFv * sup_center

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

def set_sup_color(sup_center, color):
    """sets the supply center LED a certain color"""
    # neopixel library makes this easy
    sup_center(color) 
    # sup_pixels.show()
    return

def season_LED_on(season):
    """sets the season LED to white"""
    # neopixel library makes this easy
    season(white) 
    # sup_pixels.show()
    return

def season_LED_off(season):
    """sets the season LED to none"""
    # neopixel library makes this easy
    season(none)
    # sup_pixels.show()
    return

def sup_LEDs_off():
    """sets all supply center LEDs to none"""
    sup_pixels.fill(none)
    return

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

#################
### MAIN LOOP ###
#################
while True:
    led.value = True

    # check year and season
    season = counter % 3
    year = counter // 3

    # set displays
    set_7seg_disp(year)

    # if the restart button is toggled
    if restart.value:
        # reset the counter (this resets the date display
        counter = 1

        # reset the season displays
        set_season_on(season_pixels[season])
        set_season_off(season_pixels[(season - 1)%3])
        set_season_off(season_pixels[(season - 2)%3])

        # turn supply center LEDs off
        sup_LEDs_off()

        # reset the current color list
        current_list = []
        for i in range(34):
            current_LED.append(none)

        # clear and reset the turn history list
        reset_history()

    # if the next button is toggled
    if next_season.value:
        # increment the season
        counter = counter + 1
        
        # set the appropriate season indicator
        set_season_on(season_pixels[season])

        # turn off the other idicators
        set_season_off(season_pixels[(season - 1)%3])
        set_season_off(season_pixels[(season - 2)%3])

        # if we are moving fall -> winter
        if season == 1:
            # check supply centers to see if their ownership has changed
            fall_sup_check()

            # add old current list to history
            history.append([counter, current_list])

            # update the current list
            current_list = []
            for i in range(34):
                current_LED.append(none)
            
    # if the previous button is toggled
    if prev_season.value:
        # decrement the season
        counter = counter - 1
        # set the appropriate season indicator
        set_season_on(season_pixels[season])

        # turn off the other idicators
        set_season_off(season_pixels[(season - 1)%3])
        set_season_off(season_pixels[(season - 2)%3])

        # check to see if we need to regress the supply centers 
        if season == 1:
            # then get the supply center colors for this value in the list
            for i in range(len(history[-1][1])):
                set_sup_color(supply_center_LEDs[i], history[-1][1][i])

            # now remove this value from history
            history.pop()
        

