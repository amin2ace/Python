from customtkinter import CTk
from customtkinter import CTkEntry, CTkComboBox, CTkLabel, CTkButton
import paramiko


class App:
    def __init__(self):
        self.root = CTk()
        self.root.title("SSH/RDP Client")
        self.root.config(bg="#222222")
        self.root.geometry("600x300")

        self.hostname_label = CTkLabel(self.root, text=" Hostname: ", fg_color="#808080", font=("Arial", 12))
        self.hostname_label.pack(padx=10, pady=10, anchor="w")

        self.hostname_entry = CTkEntry(self.root, fg_color="#808080", font=("Arial", 12))
        self.hostname_entry.pack(padx=10, pady=10, fill="x", expand=True)

        self.username_label = CTkLabel(self.root, text="Username:", fg_color="#808080", font=("Arial", 12))
        self.username_label.pack( padx=10, pady=10, anchor="w")

        self.username_entry = CTkEntry(self.root, fg_color="#808080", font=("Arial", 12))
        self.username_entry.pack(padx=10, pady=10, ipady=3)

        self.protocol_label = CTkLabel(self.root, text="Protocol:", fg_color="#808080", font=("Arial", 12))
        self.protocol_label.pack(padx=10, pady=10, anchor="w")

        self.protocol_options = ["SSH", "RDP"]
        self.protocol_variable = CTkComboBox(self.root, values=self.protocol_options)
        self.protocol_variable.pack(padx=10, pady=10, ipady=3)

        self.connect_button = CTkButton(self.root, text="Connect", command=self.connect, fg_color="#FFFFFF", font=("Arial", 12))
        self.connect_button.pack(padx=10, pady=10, fill="x", expand=True)

        self.status_label = CTkLabel(self.root, text="Not connected", fg_color="#FFFFFF", font=("Arial", 12))
        self.status_label.pack(padx=10, pady=10)

        self.root.mainloop()

    def connect(self):
        hostname = self.hostname_entry.get()
        username = self.username_entry.get()
        protocol = self.protocol_variable.get()

        try:
            if protocol == "SSH":
                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(hostname, username=username)

                self.status_label.config(text="Connected to SSH server")
            else:
                raise NotImplementedError("Remote Desktop Protocol (RDP) is not yet implemented")
        except Exception as e:
            self.status_label.config(text="Failed to connect: " + str(e))


if __name__ == "__main__":
    app = App()
