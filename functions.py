import tkinter
from tkinter import messagebox, Message
from tkinter.constants import W, SUNKEN, END
import os
import subprocess

home_drive = os.getenv('HOMEDRIVE')
home_path = os.getenv('HOMEPATH')

# Type define o tipo de uso 0 ou diferente de zero
def load_file(location, index, type):
    data_out = dict()
    data_out_temp = list()
    file_path = home_drive+home_path+location
    try:
        with open(file_path, "r+") as server:
            if type == 0:
                data_out_temp = server.read()
                return data_out_temp
            else:
                data_out_temp = server.readlines()
                for i in data_out_temp:
                    # Ao editar os arquivos o editor esta inserindo linhas vazias no final do arquivo, if desconsidera essas linhas ao montar a lista que retorna
                    if str(i.split(",")[index]) != "\n":
                        data_out[str(i.split(",")[index])] = str(i)
                return data_out
    except Exception as msg:
        messagebox.showerror("File", "load failed!\n" + str(msg))

def save_file(location,text_info):
    file_to_save = home_drive+home_path+location
    try:
        with open(file_to_save, "w+") as file:
            file.write(text_info.get(1.0,END))
            file.close()
    except Exception as e:
        messagebox.showerror("Erro",e)

def open_putty(user, password, ip):
    command = f'{home_drive}/{home_path}/Putty_Controller/putty.exe -ssh -l {user} -pw {password} {ip}'
    subprocess.Popen(command, stdout=subprocess.PIPE)
    
    
def open_winscp(user, password, ip, sudo):
    if sudo:
        command = f'{home_drive}/{home_path}/Putty_Controller/WinSCP.exe sftp://{user}:{password}@{ip} /rawsettings SftpServer=sudo%20su%20-c%20/usr/libexec/openssh/sftp-server'
    else:
        command = f'{home_drive}/{home_path}/Putty_Controller/WinSCP.exe sftp://{user}:{password}@{ip}'
    subprocess.Popen(command, stdout=subprocess.PIPE)


def open_wfreerdp(title, ip, user, password, width, height, full_screen):
    print(title, ip, user, password, width, height, full_screen)
    if full_screen:
        command = f'{home_drive}/{home_path}/Putty_Controller/wfreerdp.exe /u:{user} /p:{password} /v:{ip} /f /bpp:15 +compression -themes -wallpaper /audio-mode:2 +fonts'
    else:
        command = f'{home_drive}/{home_path}/Putty_Controller/wfreerdp.exe /u:{user} /p:{password} /v:{ip} /w:{width} /h:{height} /t:"{title}" /bpp:15 +compression -themes -wallpaper /audio-mode:2 +fonts'
        process = subprocess.Popen(command, stdout=subprocess.PIPE)
        #messagebox.showerror(process.communicate()[1])
        

def update_server(frame, server_key):
    show_server = Message(frame, text=server_key, aspect=2000, anchor=W, relief=SUNKEN)
    show_server.place(x=80, y=0, width=215, height=30)

def reload_files(servers_file, accounts_file):
    servers = load_file(servers_file,0)
    accounts = load_file(accounts_file,0)
    return_list = list()
    return_list.append(servers)
    return_list.append(accounts)
    return return_list

def create_accounts_used(accounts_key0, accounts_key1, accounts_key2, accounts_key3, accounts_key4, accounts_other, server_standalone, user_standalone):
    # Usar o usuario/senha dos campos
    if server_standalone.get() != "":
        # Cria a lista de accounts dos check buttoms
        accounts_used = list()
        #Verifica quais ckeck buttoms estão selecionados e substitui o valor do check buttom pelo nome da key
        if accounts_key0.get() != 0:
            accounts_key0 = "LTM"
        else:
            accounts_key0 =""

        if accounts_key1.get() != 0:
            accounts_key1 = "DUS"
        else:
            accounts_key1 = "" 

        if accounts_key2.get() != 0:
            accounts_key2 = "BRGER"
        else:
            accounts_key2 = ""

        if accounts_key3.get() != 0:
            accounts_key3 = "ADMU"
        else:
            accounts_key3 = ""

        if accounts_key4.get() != 0:
            accounts_key4 = "CONTROL"
        else:
            accounts_key4 = ""
        # Para o OTHER atribui o valor passado pelo usuario
        # Se estiver em branco atribui None e trata mais abaixo
        if accounts_other.get() != 0:
            if user_standalone.get() != "":
                accounts_other = user_standalone.get()
            else:
                accounts_other = None
        else:
            accounts_other = ""
        # Insere os valores na lista dos check buttoms
        accounts_used.append(accounts_key0);accounts_used.append(accounts_key1);accounts_used.append(accounts_key2);accounts_used.append(accounts_key3);accounts_used.append(accounts_key4);accounts_used.append(accounts_other)
        return accounts_used