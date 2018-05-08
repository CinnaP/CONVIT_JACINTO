import time
import OSC
import threading
import cfg
import mod


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

mod.display_menu()

while(cfg.run==1):

    mod.display_value()
    mod.display_menu()

mod.end_this()        
mod.display_black_screen1()
mod.display_black_screen2()
print("It's over")
exit()