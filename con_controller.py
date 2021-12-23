import tkinter
from tkinter import Label, Listbox, Message, IntVar, Checkbutton, Scrollbar, Toplevel, messagebox, filedialog
from tkinter.constants import BOTH, DISABLED, GROOVE, LEFT, RIGHT, W, SUNKEN, END, Y
import functions

# Teste

# Instancia a Janela
root = tkinter.Tk()
# Titulo da janela
root.title("Con Controller")

# Arquivos utilizados
servers_file="/path_to_file/servers.txt"
accounts_file="/path_to_file/accounts.txt"

# Editor de texto
def open_editor(config_file, file):
    
    def buttom_save():
        functions.save_file(config_file, text_info)
    # janela instanciada em cima da principal
    editor = Toplevel(root)
    editor.geometry("650x250")
    editor.minsize(height=250, width=650)
    editor.maxsize(height=250, width=650)
    editor.title("Editor")
    buttoms_frame=tkinter.Frame(editor, width=650, height=20, borderwidth=1, relief=GROOVE)
    button = tkinter.Button(buttoms_frame, text='Save', command=buttom_save)
    button.place(x=1,y=1, width=50, height=18)
    text_frame=tkinter.Frame(editor, width=650, height=230, borderwidth=1, relief=GROOVE)
    # Scroll da area de texto
    scrollbar = tkinter.Scrollbar(text_frame)
    # Area de texto associando o scroll a ela
    text_info = tkinter.Text(text_frame, yscrollcommand=scrollbar.set)
    # Limpa algum lixo que tiver
    text_info.delete(1.0,END)
    # Insere o conteúdo do arquivo
    text_info.insert(END,str(file))
    # configuring the scrollbar
    scrollbar.config(command=text_info.yview)
    
    # packing tudo
    scrollbar.pack(side=RIGHT, fill=Y)
    text_info.pack(fill=BOTH,expand=1)
    buttoms_frame.pack(padx=1,pady=1)
    text_frame.pack(padx=1,pady=1)
    #editor.mainloop()

def onOpen(config_file):
    try:
        file = functions.load_file(config_file,0,0)
        open_editor(config_file, file)
    except Exception as e:
        messagebox.showerror("Error",e)

# Limpa a janela
def destroy_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()
        
# Define e limpa o frame esquerdo
w_server = tkinter.Frame(root, width=300, height=310, borderwidth=1, relief=GROOVE)
destroy_frame(w_server)
# Define e limpa o frame direito
w_buttoms = tkinter.Frame(root, width=120, height=310, borderwidth=1, relief=GROOVE)
destroy_frame(w_buttoms)

# Carrega o arquivo de servidores
def load_servers(servers_file):
    servers = functions.load_file(servers_file,0,1)
    return servers
servers = load_servers(servers_file)

# Inicializa a variável que guarda a key de cada linha do arquivo de servidores
server_key = tkinter.StringVar()
# Atribui a key da última linha dos arquivo de servidores
server_key.set(str(list(servers.keys())[-1]))
# Título da lista com os servidores
title_server = tkinter.Message(w_server, text="Server", width=100)
title_server.place(x=1, y=37)

# Instancia o scroll da lista
servers_scroll = tkinter.Scrollbar(w_server)
servers_scroll.place(x=280, y=35, width=15, height=120)

# Instancia a lista de servidores
servers_list = Listbox(w_server, yscrollcommand = servers_scroll.set)

# Aponta o scrcoll para a lista
servers_scroll.config(command=servers_list.yview)

# Preenche a lista com as keys do arquivo de servers
for server in servers.keys():
    servers_list.insert(END, str(server))
servers_list.place(x=80, y=35, width=200, height=120)

# Instancia o message bar que mostra ultimo host abertop
title_show_server = tkinter.Message(w_server, text="Last Opened", width=100)
title_show_server.place(x=1, y=2)
# Define efeitos e atribui o valor da key do arquivo de servers
show_server = Message(w_server, text=server_key.get(), aspect=2000, anchor=W, relief=SUNKEN)
show_server.place(x=80, y=0, width=215, height=30)   

# Instancia a Entry do host definido pelo usuário 
title_server_standalone = tkinter.Message(w_server, text="Connect to: ", width=100)
title_server_standalone.place(x=1, y=163)
server_standalone = tkinter.Entry(w_server)
server_standalone.place(x=80, y=165, width=215)

# Instancia as Entries de usuário e senha OTHER com estado inicial DISABLED
title_user_standalone = tkinter.Message(w_server, text="User: ", width=100)
title_user_standalone.place(x=1, y=245)
user_standalone = tkinter.Entry(w_server, state=DISABLED)
user_standalone.place(x=80, y=247, width=215)

title_password_standalone = tkinter.Message(w_server, text="Password: ", width=100)
title_password_standalone.place(x=1, y=270)
password_standalone = tkinter.Entry(w_server, state=DISABLED)
password_standalone.place(x=80, y=272, width=215)

# Função que limpa as Entries definidas pelo usuário
def clear_server_standalone(e):
    server_standalone.delete(0,END)
    user_standalone.delete(0,END)
    password_standalone.delete(0,END)

# Executa a limpeza da Entry do host definido pelo usuário ao se selecionar um item da lista
servers_list.bind('<<ListboxSelect>>', clear_server_standalone)

# Habilita/desabilita os campos de usuário e senha quanodo OTHER é selecionado/deselecionado
def enable_fields():
    if user_standalone['state'] == tkinter.NORMAL:
        user_standalone['state'] = tkinter.DISABLED
    else:
        user_standalone['state'] = tkinter.NORMAL
    if password_standalone['state'] == tkinter.NORMAL:
        password_standalone['state'] = tkinter.DISABLED
    else:
        password_standalone['state'] = tkinter.NORMAL  

# Carrega o arquivo de accounts
accounts = functions.load_file(accounts_file,0,1)
# Instancia as keys para cada tipo de acconut usado
accounts_key0 = tkinter.IntVar()
accounts_key1 = tkinter.IntVar()
accounts_key2 = tkinter.IntVar()
accounts_key3 = tkinter.IntVar()
accounts_key4 = tkinter.IntVar()
accounts_other = tkinter.IntVar()

# Instancia os check buttoms dos accounts e atribui as keys de cada
title_accounts = tkinter.Message(w_server, text="Use account: ", width=100)
title_accounts.place(x=1, y=200)

# Associa o estado dos check buttoms ao valor das keys
account_check = Checkbutton(w_server, text="LTM",variable=accounts_key0)
account_check.place(x=75, y=200)
account_check = Checkbutton(w_server, text="DUS",variable=accounts_key1)
account_check.place(x=125, y=200)
account_check = Checkbutton(w_server, text="BRGER",variable=accounts_key2)
account_check.place(x=175, y=200)
account_check = Checkbutton(w_server, text="ADMU",variable=accounts_key3)
account_check.place(x=75, y=220)
account_check = Checkbutton(w_server, text="CONTROL",variable=accounts_key4)
account_check.place(x=135, y=220)

# Habilita/desabilita os campos de usuário e senha ao se selecionar/deselecionar OTHER
account_check = Checkbutton(w_server, text="OTHER",variable=accounts_other, command=enable_fields)
account_check.place(x=235, y=200)

# Função que chama a função que abre o putty
def do_open_putty(accounts_key0, accounts_key1, accounts_key2, accounts_key3, accounts_key4, accounts_other, accounts):
    global servers, server_key, servers_list
    # Usar o usuario/senha dos campos
    if server_standalone.get() != "":
        # Itera a lista e para cada posição
        for account in functions.create_accounts_used(accounts_key0, accounts_key1, accounts_key2, accounts_key3, accounts_key4, accounts_other, server_standalone, user_standalone):
            # Executa para os accounts pre definidos
            if account == "LTM" or account == "DUS" or account == "BRGER" or account == "ADMU" or account == "CONTROL":
                user = str(accounts.get(str(account))).split(",")[1]
                password = str(accounts.get(str(account))).split(",")[2]
                functions.open_putty(user, password, server_standalone.get())
                functions.update_server(w_server, server_standalone.get())
            # Executa para o OTHER
            elif account != "" and account != None:
                if password_standalone.get() != "":
                    user = user_standalone.get()
                    password = password_standalone.get()
                    functions.open_putty(user, password, server_standalone.get())
                    functions.update_server(w_server, server_standalone.get())
                else:
                    messagebox.showerror("Error","Empty Password")
                    break
            elif account == None:
                messagebox.showerror("Error","Empty User")
                break
                    
    # usa os valores dos arquivos de servers e accounts
    else:
        # Da linha selecionado, pega o valor da key que é usado para selecionar a linha do servers e split na coluna do IP
        ip = str(servers.get(str(servers_list.get(servers_list.curselection())))).split(",")[1]
        # Da linha selecionado, pega o valor da key que é usado para selecionar a linha do account e split na coluna do account
        account = str(servers.get(str(servers_list.get(servers_list.curselection())))).split(",")[2]
        # Usa o account para seleciona a linha e split no user
        user = str(accounts.get(str(account))).split(",")[1]
        # Usa o account para seleciona a linha e split no password
        password = str(accounts.get(str(account))).split(",")[2]
        # Executa a função que abre o putty
        functions.open_putty(user, password, ip)
        # Atualiza a message com o último aberto
        functions.update_server(w_server, servers_list.get(servers_list.curselection()))

# Função executada ao clicar no botão
def button_open_putty():        
    do_open_putty(accounts_key0, accounts_key1, accounts_key2, accounts_key3, accounts_key4, accounts_other, accounts)

# Raciocínio análogo para winscp e wfreerdp

def do_open_winscp(accounts_key0, accounts_key1, accounts_key2, accounts_key3, accounts_key4, accounts_other, sudo_value, accounts):
    global servers, server_key, servers_list
    if server_standalone.get() != "":
        for account in functions.create_accounts_used(accounts_key0, accounts_key1, accounts_key2, accounts_key3, accounts_key4, accounts_other, server_standalone, user_standalone):
            if account == "LTM" or account == "DUS" or account == "BRGER" or account == "ADMU" or account == "CONTROL":
                user = str(accounts.get(str(account))).split(",")[1]
                password = str(accounts.get(str(account))).split(",")[2]                    
                functions.open_winscp(user, password, server_standalone.get(), sudo_value.get())
                functions.update_server(w_server, server_standalone.get())
            elif account != "" and account != None:
                if password_standalone.get() != "":
                    user = user_standalone.get()
                    password = password_standalone.get()
                    functions.open_winscp(user, password, server_standalone.get(), sudo_value.get())
                    functions.update_server(w_server, server_standalone.get())
                else:
                    messagebox.showerror("Error","Empty Password")
                    break
            elif account == None:
                messagebox.showerror("Error","Empty User")
                break
    else:
        ip = str(servers.get(str(servers_list.get(servers_list.curselection())))).split(",")[1]
        account = str(servers.get(str(servers_list.get(servers_list.curselection())))).split(",")[2]
        user = str(accounts.get(str(account))).split(",")[1]
        password = str(accounts.get(str(account))).split(",")[2]
        functions.open_winscp(user, password, ip, sudo_value.get())
        functions.update_server(w_server, servers_list.get(servers_list.curselection()))    

def button_open_winscp():
    do_open_winscp(accounts_key0, accounts_key1, accounts_key2, accounts_key3, accounts_key4, accounts_other, sudo_value, accounts)

def do_open_wfreerdp(accounts_key0, accounts_key1, accounts_key2, accounts_key3, accounts_key4, accounts_other, full_screen_value, accounts):
    global servers, server_key, servers_list
    if server_standalone.get() != "":
        title = "Server: "+str(server_standalone.get())
        width = 1440
        height = 900
        for account in functions.create_accounts_used(accounts_key0, accounts_key1, accounts_key2, accounts_key3, accounts_key4, accounts_other, server_standalone, user_standalone):
            if account == "LTM" or account == "DUS" or account == "BRGER" or account == "ADMU" or account == "CONTROL":
                user_tmp = str(accounts.get(str(account))).split(",")[1]
                user_name = str(user_tmp).split("@")[0]
                user_domain = str(user_tmp).split("@")[1]
                user=user_domain+"\\"+user_name
                password = str(accounts.get(str(account))).split(",")[2]
                functions.open_wfreerdp(title, server_standalone.get(), user, password, width, height, full_screen_value.get())
                functions.update_server(w_server, server_standalone.get())
            elif account != "" and account != None:
                if password_standalone.get() != "":
                    user = user_standalone.get()
                    password = password_standalone.get()                    
                    functions.open_wfreerdp(title, server_standalone.get(), user, password, width, height, full_screen_value.get())
                    functions.update_server(w_server, server_standalone.get())
                else:
                    messagebox.showerror("Error","Empty Password")
                    break
            elif account == None:
                messagebox.showerror("Error","Empty User")
                break
    else:
        title = str(servers.get(str(servers_list.get(servers_list.curselection())))).split(",")[1]
        ip = str(servers.get(str(servers_list.get(servers_list.curselection())))).split(",")[1]
        account = str(servers.get(str(servers_list.get(servers_list.curselection())))).split(",")[2]
        user_tmp = str(accounts.get(str(account))).split(",")[1]
        user_name = str(user_tmp).split("@")[0]
        user_domain = str(user_tmp).split("@")[1]
        user=user_domain+"\\"+user_name
        password = str(accounts.get(str(account))).split(",")[2]
        width = str(servers.get(str(servers_list.get(servers_list.curselection())))).split(",")[3]
        height = str(servers.get(str(servers_list.get(servers_list.curselection())))).split(",")[4]
        functions.open_wfreerdp(title, ip, user, password, width, height, full_screen_value.get())
        functions.update_server(w_server, servers_list.get(servers_list.curselection()))

def button_open_wfreerdp():
    do_open_wfreerdp(accounts_key0, accounts_key1, accounts_key2, accounts_key3, accounts_key4, accounts_other, full_screen_value, accounts)

# Instancia os botoes que abrem o putty, winscp e wfreerdp e check buttoms

button = tkinter.Button(w_buttoms, text='Open Putty', command=button_open_putty)
button.place(x=8,y=30, width=100, height=30)

button = tkinter.Button(w_buttoms, text='Open WinSCP', command=button_open_winscp)
button.place(x=8,y=70, width=100, height=30)

sudo_value = IntVar()
sudo_value_check = Checkbutton(w_buttoms, text="With sudo?", variable=sudo_value)
sudo_value_check.place(x=8, y=100)

button = tkinter.Button(w_buttoms, text='Open WFreeRDP', command=button_open_wfreerdp)
button.place(x=8,y=130, width=100, height=30)

full_screen_value = IntVar()
full_screen_value_check = Checkbutton(w_buttoms, text="Full Screen?", variable=full_screen_value)
full_screen_value_check.place(x=8, y=160) 

# Função de refresh da janela    

def refresh(self):
    root.wm_attributes("-topmost", ontop_value.get())
    
def do_refresh():
    refresh(root)

# Variável para manter a janela acima das outras
ontop_value = IntVar()

def reload_servers():
    global servers, server_key, servers_list
    servers = load_servers(servers_file)        
    # Inicializa a variável que guarda a key de cada linha do arquivo de servidores
    #server_key = tkinter.StringVar()
    # Atribui a key da última linha dos arquivo de servidores
    server_key.set(str(list(servers.keys())[-1]))
    # Instancia a lista de servidores
    #servers_list = Listbox(w_server, yscrollcommand = Scrollbar.set)
    # Limpa a lista
    servers_list.delete(0, END)
    # Preenche a lista com as keys do arquivo de servers
    for server in servers.keys():
        servers_list.insert(END, str(server))
    show_server = Message(w_server, text=server_key.get(), aspect=2000, anchor=W, relief=SUNKEN)
    show_server.place(x=80, y=0, width=215, height=30)
    #messagebox.showerror("clickado")
    
def reload_accounts():
    global accounts
    accounts = functions.load_file(accounts_file,0,1)

def item_menu_accounts():
    onOpen(accounts_file)
def item_menu_servers():
    onOpen(servers_file)
        
menubar = tkinter.Menu(root)

filemenu = tkinter.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open Accounts file", command=item_menu_accounts)
filemenu.add_command(label="Open Servers file", command=item_menu_servers)
filemenu.add_command(label="Exit", command=root.quit)

configmenu = tkinter.Menu(menubar, tearoff=0)
configmenu.add_checkbutton(label="On top", variable=ontop_value, command=do_refresh)
configmenu.add_command(label="Reload Accounts", command=reload_accounts)
configmenu.add_command(label="Reload Servers", command=reload_servers)

menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Config", menu=configmenu)

root.config(menu=menubar)

# Desenha a janela toda e atribui a escolha do on top
w_server.pack(padx=1,pady=1, side=LEFT)
w_buttoms.pack(padx=1,pady=1, side=RIGHT)
root.wm_attributes("-topmost", ontop_value.get())
root.resizable(width=False, height=False)
root.mainloop()

