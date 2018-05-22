from PIL import Image, ImageDraw, ImageFont
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306 as adafruit
import os

#____________________UTILITY VARIABLES____________________#

run = 1

#____________________SCREEN VARIABLES____________________#

# Raspberry Pi pin configuration:
DC1 = 23
RST1 = 24
SPI_PORT1 = 0
SPI_DEVICE1 = 0

DC2 = 12
RST2 = 16
SPI_PORT2 = 0
SPI_DEVICE2 = 1

# 128x32 display with hardware SPI:
disp = adafruit.SSD1306_128_32(rst=RST1, dc=DC1, spi=SPI.SpiDev(SPI_PORT1, SPI_DEVICE1, max_speed_hz=8000000))
disp2 = adafruit.SSD1306_128_32(rst=RST2, dc=DC2, spi=SPI.SpiDev(SPI_PORT2, SPI_DEVICE2, max_speed_hz=8000000))

disp.begin()
disp2.begin()

disp.clear()
disp2.clear()

disp.display()
disp2.display()

width = disp.width
height = disp.height

image = Image.new('1', (width, height))
image2 = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)
draw2 = ImageDraw.Draw(image2)

top = 0
bottom = height

font = ImageFont.load_default()
numberfont = ImageFont.load_default()


#____________________OSC VARIABLES____________________#

display_value_flag = 1
display_patch_list_flag = 1
display_menu_flag = 1
display_table_flag = 1

value1_name = ""
value1 = 0
value2_name = ""
value2 = "0"
value3_name = ""
value3 = "0"
value4_name = ""
value4 = "0"

# normalement 1
menu_line = 1
menu_cursor = [2, 2, 6, 6]

table = []

receive_address = '127.0.0.1', 9001


#____________________SYSTEM VARIABLES____________________#

patch_folder = os.getcwd() + '/PRESETS' #name of the folder containing the patches
patch_list = os.listdir(patch_folder) #list of atmnt folder in the previous folder
folder_list_size = len(patch_list) #size of the previous list
patch_number = 0 #number of the current patch according to the list
patch_name = "" #name of the current atmtn folder
