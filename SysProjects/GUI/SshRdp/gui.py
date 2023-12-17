
import customtkinter as ctk
from customtkinter import CTkComboBox, CTkLabel, CTkEntry, CTkButton
from proxy import connect_ssh

class Ssh_gui:
    
    def __init__(self):
        app = ctk.CTk()
        app.title("SSH Connection")
        
        app.resizable(width=False, height=False)


        self.connection = CTkComboBox(app, values=('SSH', 'RDP'))
        # self.connection.bind("<<ComboboxSelected>>", self.switch)

        ip_label = CTkLabel(app, text="IP Address:")
        self.ip_entry = CTkEntry(app)

        port_label = CTkLabel(app, text="Port:")
        self.port_entry = CTkEntry(app)

        self.user_label = CTkLabel(app, text="UserName:")
        self.user_entry = CTkEntry(app)

        connect_button = CTkButton(app, text="Connect", command=lambda: connect_ssh(self))

        self.connection.pack(padx=10, pady=10)

        ip_label.pack(padx=10)
        self.ip_entry.pack(pady=10, padx=10)

        port_label.pack(padx=2)
        self.port_entry.pack(pady=10)

        self.user_label.pack(pady=2)
        self.user_entry.pack(pady=10)

        connect_button.pack(pady=10)
        app.mainloop()

    # def switch(self):
    #     conn = self.connection.get()
    #     if conn == 'SSH':
    #         pass
    #     else:
    #         self.user_entry.destroy()
    #         self.user_label.destroy()

