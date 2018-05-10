from time import sleep
import psutil
import sys
import subprocess
import cfg

#______________________________ UTILITY FONCTIONS ______________________________#

def remap(x):
    old_min = -1
    old_max = 1
    new_min = 0
    new_max = 32
    x = (x - old_min)/(old_max - old_min)*(new_max - new_min) + new_min
    return(x)

#______________________________ DISPLAY FONCTIONS ______________________________#

def display_black_screen1():
    cfg.draw.rectangle((0,0,cfg.width,cfg.height), outline=0, fill=0)
    cfg.disp.image(cfg.image)
    cfg.disp.display()
    cfg.disp.clear()

def display_black_screen2():
    cfg.draw2.rectangle((0,0,cfg.width,cfg.height), outline=0, fill=0)
    cfg.disp2.image(cfg.image2)
    cfg.disp2.display()
    cfg.disp2.clear()

def display_loading_screen():
    """
    displays the classic loading screen and the name of the patch you're opening.
    this fonction is called by open_patch() and change_patch().
    """
    cfg.draw.rectangle((0,0,cfg.width,cfg.height), outline=0, fill=0)
    cfg.draw.text((0, 0), "OPENING " + cfg.patch_name, font=cfg.font, fill=255)
    cfg.draw.text((0, 0+8), ".", font=cfg.font, fill=255)
    cfg.disp.image(cfg.image)
    cfg.disp.display()
    cfg.disp.clear()
    sleep(0.5)
    cfg.draw.text((0, 0), "OPENING " + cfg.patch_name, font=cfg.font, fill=255)
    cfg.draw.text((0, 0+8), "..", font=cfg.font, fill=255)
    cfg.disp.image(cfg.image)
    cfg.disp.display()
    cfg.disp.clear()
    sleep(0.5)
    cfg.draw.text((0, 0), "OPENING " + cfg.patch_name, font=cfg.font, fill=255)
    cfg.draw.text((0, 0+8), "...", font=cfg.font, fill=255)
    cfg.disp.image(cfg.image)
    cfg.disp.display()
    cfg.disp.clear()
    sleep(0.5)
    cfg.draw.rectangle((0,0,cfg.width,cfg.height), outline=0, fill=0)
    cfg.disp.image(cfg.image)
    cfg.disp.display()
    cfg.disp.clear()


def display_value():
    """
    displays the received OSC value at the corresponding line only if display_value_flag = 1
    """
    #if cfg.display_value_flag == 1:
    cfg.display_value_flag = 0
    cfg.draw2.rectangle((0,0,cfg.width,cfg.height), outline=0, fill=0)
        
    cfg.draw2.line((0, cfg.height/2, cfg.width, cfg.height/2), fill=255)
    cfg.draw2.line((cfg.width/2, 0, cfg.width/2, cfg.bottom), fill=255)
        
    cfg.draw2.text((3, 0), cfg.value1_name, font=cfg.font, fill=255)
    cfg.draw2.text((cfg.width/2 + 3, 0), cfg.value2_name, font=cfg.font, fill=255)
    cfg.draw2.text((3, cfg.height/2 +2), cfg.value3_name, font=cfg.font, fill=255)
    cfg.draw2.text((cfg.width/2 + 3, cfg.height/2 +2), cfg.value4_name, font=cfg.font, fill=255)
        
    cfg.draw2.text((13, 15), str(cfg.value1), font=cfg.numberfont, fill=255)
    cfg.draw2.text((cfg.width/2+13, 15), str(cfg.value2), font=cfg.numberfont, fill=255)
    cfg.draw2.text((13, cfg.height/2 +15), str(cfg.value3), font=cfg.numberfont, fill=255)
    cfg.draw2.text((cfg.width/2 +13, cfg.height/2 +15), str(cfg.value4), font=cfg.numberfont, fill=255)
        
    cfg.disp2.image(cfg.image2)
    cfg.disp2.display()
    cfg.disp2.clear()
    #else:
     #   pass

def display_info():
    """
    displays the name of the current patch and CPU load
    """
    cpu = psutil.cpu_percent()
    cfg.draw.rectangle((0,0,cfg.width,cfg.height), outline=0, fill=0)
    cfg.draw.text((0, 0), "INFOS", font=cfg.font, fill=255)
    cfg.draw.text((0, 0+8), cfg.patch_name, font=cfg.font, fill=255)
    cfg.draw.text((0, 0+16), "CPU : "+str(int(cpu))+"%", font=cfg.font, fill=255)
    cfg.disp.image(cfg.image)
    cfg.disp.display()
    cfg.disp.clear()

def display_patch_list():
    """
    displays the files present in the "HERE" folder
    """
    if cfg.display_patch_list_flag == 1:
        cfg.display_patch_list_flag = 0
        cfg.draw.rectangle((0,0,cfg.width,cfg.height), outline=0, fill=0)
        cfg.draw.text((0, 0),"CHOOSE YOUR PATCH", font=cfg.font, fill=255)
        for i in range(cfg.folder_list_size):
            cfg.draw.text((0, 0+8*i+8),str(i)+" : "+cfg.patch_list[i], font=cfg.font, fill=255)
            print(str(i)+" : "+cfg.patch_list[i])
        cfg.disp.image(cfg.image)
        cfg.disp.display()
        cfg.disp.clear()
    else:
        pass

def display_table():
    """
    display the table on the screen
    """
    cfg.draw.rectangle((0,0,cfg.width,cfg.height), outline=0, fill=0)
    for i, j in enumerate(cfg.table):
        cfg.draw.point((i, j), fill=255)
    cfg.disp.image(cfg.image)
    cfg.disp.display()
    cfg.disp.clear()
    #cfg.display_table_flag = 0
    #print("table displayed")

def display_menu():
    """
    displays the menu
    """
    if cfg.display_menu_flag == 1:
        cfg.display_menu_flag = 0
        cfg.draw.rectangle((0,0,cfg.width,cfg.height), outline=0, fill=0)
        cfg.draw.rectangle(cfg.menu_cursor, outline=0, fill=255)
        cfg.draw.text((8, 0), "INFOS", font=cfg.font, fill=255)
        cfg.draw.text((8, 8), "TABLE", font=cfg.font, fill=255)
        cfg.draw.text((8, 16), "SAVE PATCH", font=cfg.font, fill=255)
        cfg.draw.text((8, 24), "LOAD PATCH", font=cfg.font, fill=255)
        cfg.draw.text((8, 32), "QUIT", font=cfg.font, fill=255)
        cfg.disp.image(cfg.image)
        cfg.disp.display()
        cfg.disp.clear()

def cursor_move(direction):
    """
    moves the cursor up, down or to initialisation
    """
    maxx = 58
    minn = 2
    if direction == "up":
        if cfg.menu_cursor[1] < maxx:
            cfg.menu_cursor[1] += 8
            cfg.menu_cursor[3] += 8
            cfg.menu_line += 1
            cfg.display_menu_flag = 1
    if direction == "down":   
        if cfg.menu_cursor[1] > minn:
            cfg.menu_cursor[1] -= 8
            cfg.menu_cursor[3] -= 8
            cfg.menu_line -= 1
            cfg.display_menu_flag = 1
    if direction == "init":
        cfg.menu_cursor = [2, 2, 6, 6]
        cfg.menu_line = 1
        cfg._display_menu_flag = 1
    


#______________________________ OSC FONCTIONS ______________________________#

def receive_value(addr, tags, stuff, source):
    """
    receive OSC messages and change the value of "name" global variables.
    here the OSC's adresses are related to the line the message is displayed on. the first argument
    of the message is the value (ex : 440) and the second argument is the name (ex : frequency)
    """
    value = stuff[0]
    typee = stuff[1]
    name = stuff[2]
    if addr=="/value1":
        cfg.value1_name = name
        if typee == "i":
            cfg.value1 = int(value)
        else:
            cfg.value1 = round(value, 2)
        cfg.display_value_flag = 1
    if addr=="/value2":
        cfg.value2_name = name
        if typee == "i":
            cfg.value2 = int(value)
        else:
            cfg.value2 = round(value, 2)
        cfg.display_value_flag = 1
    if addr=="/value3":
        cfg.value3_name = name
        if typee == "i":
            cfg.value3 = int(value)
        else:
            cfg.value3 = round(value, 2)
        cfg.display_value_flag = 1
    if addr=="/value4":
        cfg.value4_name = name
        if typee == "i":
            cfg.value4 = int(value)
        else:
            cfg.value4 = round(value, 2)
        cfg.display_value_flag = 1

def cursor_receive(addr, tags, stuff, source):
    value = stuff[0]
    if value == 1.0:
        cursor_move("up")
    if value == 0.0:
        cursor_move("down")

def cursor_clic(addr, tags, stuff, source):
    if cfg.menu_line == 1: # INFOS
        display_info()
    if cfg.menu_line == 2: #TABLE
        display_table
    if cfg.menu_line == 3: #SAVE
        pass
    if cfg.menu_line == 4: #LOAD
        display_patch_list()
    if cfg.menu_line == 5: #QUIT
        cfg.run = 0
        

def change_table(addr, tags, stuff, source):
    """
    changes the values of the list containing the array/waveform 
    """
    cfg.table = stuff
    #cfg.display_table_flag = 1
    #print ("table changed")
    #print cfg.table


#______________________________ SYSTEM FONCTIONS ______________________________#

def open_patch():
    """
    wait for a stdin.readline() number (TEMPORARY) and opens the corresponding patch
    (stdin.readlin() will be replaced by a serial information from the PIC)
    """
    global proc
    cfg.patch_number = sys.stdin.readline()
    cfg.patch_name = cfg.patch_list[int(cfg.patch_number)]
    proc = subprocess.Popen(["pd", cfg.patch_name], cwd=cfg.patch_folder,
                        stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    display_loading_screen()

def change_patch():
    """
    wait for a stdin.readline() number (TEMPORARY), closes the current patch and opens the chosen one
    (stdin.readlin() will be replaced by a serial information from the PIC)
    """
    global proc
    cfg.patch_number = sys.stdin.readline()
    cfg.patch_name = cfg.patch_list[int(cfg.patch_number)]
    proc.kill()
    proc = subprocess.Popen(["pd", cfg.patch_name], cwd=cfg.patch_folder,
                        stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    display_loading_screen()
    cfg.page = 1
    print cfg.page

def write_save_slot():
    """
    writes the name of current patch in save_slot.txt
    """
    with open("save_slot.txt", "w") as f:
        f.write("%s" % (cfg.patch_name))

def read_save_slot():
    """
    Reads the content of save_slot.txt which contains the last opened patch's name, then changes
    the value of cfg.patch_name. This allows to open the same patch after shutdown.
    """
    with open("save_slot.txt", "r") as f:
        cfg.patch_name = f.read()

def end_this():
    """
    end of the world
    """
    global proc
    write_save_slot()
    proc.kill()
