import customtkinter as ctk
from customtkinter import CTkLabel, CTkEntry, CTkButton, CTkComboBox
from threading import Thread
from paramiko import SSHClient, AutoAddPolicy
from subprocess import Popen, CREATE_NEW_CONSOLE

class SshGui:

    def __init__(self) -> None:
        self.create_gui()




    def connect_ssh(self):
        try:
            self.ip_address = self.ip_entry.get()
            self.port = int(self.port_entry.get())
            self.user = self.user_entry.get()
            self.password = self.pass_entry.get()
            self.establish_ssh_connection()
        except Exception as e:
            print("Error connecting SSH:", e)
        else:
            print("SSH connection initiated")


    def establish_ssh_connection(self):
        try:
            # stdin, stdout, stderr = client.exec_command('ls -l')
            ssh_client = SSHClient()
            ssh_client.load_system_host_keys()
            # ssh_client.set_missing_host_key_policy(AutoAddPolicy)
            ssh_client.connect(self.ip_address, self.port, self.user)
            print("SSH connection established successfully!")
            command = f'ssh -l {self.user} {self.ip_address} -p {self.port}'
            process = Popen(command, creationflags=CREATE_NEW_CONSOLE)
            process.wait()
            ssh_client.close()

        except Exception as e:
            print("Failed to establish SSH connection:", e)
            ssh_client.close()



SshGui()
