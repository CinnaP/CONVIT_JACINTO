import time
import OSC
import threading
import cfg
import mod

#commentaire TEST


server = OSC.OSCServer(cfg.receive_address)
server.addDefaultHandlers
server.addMsgHandler("/value1", mod.receive_value)
server.addMsgHandler("/value2", mod.receive_value)
server.addMsgHandler("/value3", mod.receive_value)
server.addMsgHandler("/value4", mod.receive_value)
server.addMsgHandler("/table", mod.change_table)
server.addMsgHandler("/cursor_updown", mod.cursor_receive_updown)
server.addMsgHandler("/cursor_leftright", mod.cursor_receive_leftright)

print "Start OSCServer"
st = threading.Thread(target=server.serve_forever)
st.start()

# OPEN LAST PATCH
mod.read_save_slot_and_open()

#CHOSE YOUR PATCH
#mod.display_patch_list()
#mod.open_patch()

#mod.display_menu()

while(cfg.run==1):

    while(cfg.page==0): #page 0 = MENU
        mod.display_menu()
        mod.display_value()
        time.sleep(0.03)

    while(cfg.page==1): #page 1 = WAVEFORM
        mod.display_table()
        mod.display_value()
        time.sleep(0.03)

    while(cfg.page==2): #page 2 = INFOS
        mod.display_info()
        mod.display_value()
        time.sleep(0.03)

    while(cfg.page==3): #page 3 = SAVE
        mod.display_black_screen1()
        mod.display_value()
        time.sleep(0.03)

    while(cfg.page==4): #page 4 = LOAD
        mod.display_patch_list()
        mod.display_value()
        time.sleep(0.03)

    while(cfg.page==5): #page 5 = QUIT
        mod.end_this()
   

mod.end_this()        
mod.display_black_screen1()
mod.display_black_screen2()
print("It's over")
exit()
