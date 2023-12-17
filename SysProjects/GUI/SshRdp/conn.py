from subprocess import Popen, CREATE_NEW_CONSOLE
from paramiko import SSHClient, RejectPolicy


def establish_ssh_shell(host, port, user):
    
    try:
        ssh_client = SSHClient()
        ssh_client.load_system_host_keys()
        # ssh_client.connect(host, port, user)
        print("SSH connection established successfully!")
        command = f'ssh -l {user} {host} -p {port}'
        print(command)
        process = Popen(command, creationflags=CREATE_NEW_CONSOLE)
        print('opened')
        process.wait()
    except Exception as e:
        return f"Failed to establish SSH connection: {e}"
