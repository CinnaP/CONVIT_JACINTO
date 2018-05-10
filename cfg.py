from PIL import Image, ImageDraw, ImageFont
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306 as adafruit
import os

#____________________UTILITY VARIABLES____________________#

run = 1

#____________________SCREEN VARIABLES____________________#

# Raspberry Pi pin configuration:
RST = 24
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# 128x32 display with hardware SPI:
disp = adafruit.SSD1306_128_32(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))

# 128x64 display with hardware I2C
#disp = adafruit.SSD1306_128_64(rst=None, i2c_address=0x3c)
#disp2 = adafruit.SSD1306_128_64(rst=None, i2c_address=0x3d)
disp.begin()
#disp2.begin()
#disp.clear()
#disp.display()
width = disp.width
height = disp.height

image = Image.new('1', (width, height))
#image2 = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)
#draw2 = ImageDraw.Draw(image2)

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
value1 = "0"
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

patch_folder = os.getcwd() + '/HERE' #name of the folder containing the patches
patch_list = os.listdir(patch_folder) #list of files in the previous folder
folder_list_size = len(patch_list) #size of the previous list
patch_number = 0 #number of the current patch according to the list
patch_name = "" #name of the current patch




