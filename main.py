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
server.addMsgHandler("/cursor", mod.cursor_receive)
server.addMsgHandler("/clic", mod.cursor_clic)

print "Start OSCServer"
st = threading.Thread(target=server.serve_forever)
st.start()

# OPEN LAST PATCH
#mod.read_save_slot()
#mod.open_patch()

#CHOSE YOUR PATCH
mod.display_patch_list()
mod.open_patch()

#mod.display_menu()

while(cfg.run==1):
    pass
    mod.display_table()
    time.sleep(0.03)

mod.end_this()        
mod.display_black_screen1()
mod.display_black_screen2()
print("It's over")
exit()
