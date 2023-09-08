import os
import time
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('sftp.server.com', username='username', password='password')

sftp = ssh.open_sftp()
sftp.chdir('/path/to/csv/files')

while True:
    filenames = sftp.listdir()
    for filename in filenames:
        if filename.endswith('.csv'):
            local_filename = os.path.join('/path/to/local/folder', filename)
            sftp.get(filename, local_filename)
            print(f'Downloaded {filename}')
    time.sleep(600)

sftp.close()
ssh.close()
