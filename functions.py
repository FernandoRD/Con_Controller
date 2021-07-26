import tkinter
from tkinter import messagebox, Message, W, SUNKEN
import os
import subprocess

home_drive = os.getenv('HOMEDRIVE')
home_path = os.getenv('HOMEPATH')

def load_file(location):
    data_out = dict()
    data_out_temp = list()
    file_path = home_drive+home_path+location
    try:
        with open(file_path, "r+") as server:
            data_out_temp = server.readlines()
        for i in data_out_temp:
            data_out[str(i.split(",")[0])] = str(i)
        return data_out
    except Exception as msg:
        messagebox.showerror("File", "load failed!\n" + str(msg))

def open_putty(user, password, ip):
    command = './putty.exe -ssh -l {} -pw {} {}'.format(user, password, ip)
    subprocess.Popen(command, stdout=subprocess.PIPE)

def open_winscp(user, password, ip, sudo):
    if sudo:
        command = './WinSCP.exe sftp://{}:{}@{} /rawsettings SftpServer=sudo%20su%20-c%20/usr/libexec/openssh/sftp-server'.format(user, password, ip)
    else:
        command = './WinSCP.exe sftp://{}:{}@{}'.format(user, password, ip)
    subprocess.Popen(command, stdout=subprocess.PIPE)


def open_wfreerdp(title, ip, user, password, width, height, full_screen):
    print(title, ip, user, password, width, height, full_screen)
    if full_screen:
        command = './wfreerdp.exe /u:{} /p:{} /v:{} /f /bpp:15 +compression -themes -wallpaper /audio-mode:2'.format(user, password, ip)
    else:
        #messagebox.showerror("Variaveis", "fullscreen: {}".format(full_screen))
        command = './wfreerdp.exe /u:{} /p:{} /v:{} /w:{} /h:{} /t:"{}" /bpp:15 +compression -themes -wallpaper /audio-mode:2'.format(user, password, ip, width, height, title)
    subprocess.Popen(command, stdout=subprocess.PIPE)

def update_server(frame, server_key):
        show_server = Message(frame, text=server_key, aspect=2000, anchor=W, relief=SUNKEN)
        show_server.place(x=80, y=30, width=215, height=30)
