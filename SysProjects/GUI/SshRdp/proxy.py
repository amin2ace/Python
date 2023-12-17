from conn import establish_ssh_shell

def connect_ssh(gui):
    try:
        ip_address = gui.ip_entry.get()
        port = int(gui.port_entry.get())
        user = gui.user_entry.get()
        print(ip_address, port, user)
    except Exception as e:
        print("Error connecting SSH:", e)
    else:
        establish_ssh_shell(ip_address, port, user)
        print("SSH connection initiated")
    
