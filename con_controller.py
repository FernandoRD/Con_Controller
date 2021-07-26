import tkinter
from tkinter import Listbox, Message, IntVar, Checkbutton, Scrollbar
from tkinter.constants import BOTTOM, DISABLED, GROOVE, LEFT, RIGHT, TOP, W, SUNKEN, END, NORMAL
import functions
import subprocess


def main():
    root = tkinter.Tk() 
    root.title("Con controller")

    servers_file="/Documents/servers.txt"
    accounts_file="/Documents/accounts.txt"

    def destroy_frame(frame):
        for widget in frame.winfo_children():
            widget.destroy()

    w_server = tkinter.Frame(root, width=320, height=310, borderwidth=1, relief=GROOVE)
    destroy_frame(w_server)
    
    w_buttoms = tkinter.Frame(root, width=120, height=310, borderwidth=1, relief=GROOVE)
    destroy_frame(w_buttoms)

    servers = functions.load_file(servers_file)
    server_key = tkinter.StringVar()
    server_key.set(str(list(servers.keys())[-1]))
    title_server = tkinter.Message(w_server, text="Server", width=100)
    title_server.place(x=1, y=67)
    

    
    servers_list = Listbox(w_server, yscrollcommand = Scrollbar.set)
    #servers_list.config(command = servers_list.yview)

    for server in servers.keys():
        servers_list.insert(END, str(server))
    servers_list.place(x=80, y=65, width=220, height=120)
    
    servers_scroll = tkinter.Scrollbar(w_server)
    servers_scroll.place(x=300, y=65, width=15, height=120)
    servers_scroll.config(command=servers_list.yview)

    title_show_server = tkinter.Message(w_server, text="Last Opened", width=100)
    title_show_server.place(x=1, y=32)
    show_server = Message(w_server, text=server_key.get(), aspect=2000, anchor=W, relief=SUNKEN)
    show_server.place(x=80, y=30, width=235, height=30)   

    title_server_standalone = tkinter.Message(w_server, text="Connect to: ", width=100)
    title_server_standalone.place(x=1, y=193)
    server_standalone = tkinter.Entry(w_server)
    server_standalone.place(x=80, y=195, width=235)

    title_user_standalone = tkinter.Message(w_server, text="User: ", width=100)
    title_user_standalone.place(x=1, y=263)
    user_standalone = tkinter.Entry(w_server, state=DISABLED)
    user_standalone.place(x=80, y=265, width=235)
    title_password_standalone = tkinter.Message(w_server, text="Password: ", width=100)
    title_password_standalone.place(x=1, y=283)
    password_standalone = tkinter.Entry(w_server, state=DISABLED)
    password_standalone.place(x=80, y=285, width=235)

    def clear_server_standalone(e):
        server_standalone.delete(0,END)

    servers_list.bind('<<ListboxSelect>>', clear_server_standalone)
    
    def enable_fields():
        if user_standalone['state'] == tkinter.NORMAL:
            user_standalone['state'] = tkinter.DISABLED
        else:
            user_standalone['state'] = tkinter.NORMAL
        if password_standalone['state'] == tkinter.NORMAL:
            password_standalone['state'] = tkinter.DISABLED
        else:
            password_standalone['state'] = tkinter.NORMAL  

    accounts = functions.load_file(accounts_file)
    accounts_key0 = tkinter.IntVar()
    accounts_key1 = tkinter.IntVar()
    accounts_key2 = tkinter.IntVar()
    accounts_key3 = tkinter.IntVar()
    accounts_key4 = tkinter.IntVar()
    accounts_other = tkinter.IntVar()
    
    title_accounts = tkinter.Message(w_server, text="Use account: ", width=100)
    title_accounts.place(x=1, y=220)
    
    account_check = Checkbutton(w_server, text="ACC1",variable=accounts_key0)
    account_check.place(x=75, y=220)
    account_check = Checkbutton(w_server, text="ACC2",variable=accounts_key1)
    account_check.place(x=135, y=220)
    account_check = Checkbutton(w_server, text="ACC3",variable=accounts_key2)
    account_check.place(x=190, y=220)

    account_check = Checkbutton(w_server, text="ACC4",variable=accounts_key3)
    account_check.place(x=75, y=240)
    account_check = Checkbutton(w_server, text="ACC5",variable=accounts_key4)
    account_check.place(x=135, y=240)

    account_check = Checkbutton(w_server, text="OTHER",variable=accounts_other, command=enable_fields)
    account_check.place(x=250, y=220)
    
    def do_open_putty(accounts_key0, accounts_key1, accounts_key2, accounts_key3, accounts_key4, accounts_other):
        if server_standalone.get() != "":
            accounts_used = list()
            if accounts_key0.get() != 0:
                accounts_key0 = "ACC1"
            else:
                accounts_key0 =""

            if accounts_key1.get() != 0:
                accounts_key1 = "ACC2"
            else:
                accounts_key1 = "" 

            if accounts_key2.get() != 0:
                accounts_key2 = "ACC3"
            else:
                accounts_key2 = ""

            if accounts_key3.get() != 0:
                accounts_key3 = "ACC4"
            else:
                accounts_key3 = ""

            if accounts_key4.get() != 0:
                accounts_key4 = "ACC5"
            else:
                accounts_key4 = ""

            if accounts_other.get() != 0:
                accounts_other = user_standalone.get()
            else:
                accounts_other = ""

            accounts_used.append(accounts_key0);accounts_used.append(accounts_key1);accounts_used.append(accounts_key2);accounts_used.append(accounts_key3);accounts_used.append(accounts_key4);accounts_used.append(accounts_other)

            for account in accounts_used:
                if account == "ACC1" or account == "ACC2" or account == "ACC3" or account == "ACC4" or account == "ACC5":
                    user = str(accounts.get(str(account))).split(",")[1]
                    password = str(accounts.get(str(account))).split(",")[2]
                    functions.open_putty(user, password, server_standalone.get())
                    functions.update_server(w_server, server_standalone.get())
                elif account != "":
                    user = user_standalone.get()
                    password = password_standalone.get()
                    functions.open_putty(user, password, server_standalone.get())
                    functions.update_server(w_server, server_standalone.get())
        else:
            ip = str(servers.get(str(servers_list.get(servers_list.curselection())))).split(",")[1]
            account = str(servers.get(str(servers_list.get(servers_list.curselection())))).split(",")[2]
            user = str(accounts.get(str(account))).split(",")[1]
            password = str(accounts.get(str(account))).split(",")[2]
            functions.open_putty(user, password, ip)
            functions.update_server(w_server, servers_list.get(servers_list.curselection()))

    def button_open_putty():
        do_open_putty(accounts_key0, accounts_key1, accounts_key2, accounts_key3, accounts_key4, accounts_other)

    def do_open_winscp(accounts_key0, accounts_key1, accounts_key2, accounts_key3, accounts_key4, accounts_other, sudo_value):
        if server_standalone.get() != "":
            accounts_used = list()
            if accounts_key0.get() != 0:
                accounts_key0 = "ACC1"
            else:
                accounts_key0 =""
            
            if accounts_key1.get() != 0:
                accounts_key1 = "ACC2"
            else:
                accounts_key1 = ""  
            
            if accounts_key2.get() != 0:
                accounts_key2 = "ACC3"      
            else:
                accounts_key2 = ""
            
            if accounts_key3.get() != 0:
                accounts_key3 = "ACC4"      
            else:
                accounts_key3 = ""
            
            if accounts_key4.get() != 0:
                accounts_key4 = "ACC5"      
            else:
                accounts_key4 = ""
            
            if accounts_other.get() != 0:
                accounts_other = user_standalone.get()
            else:
                accounts_other = ""

            accounts_used.append(accounts_key0);accounts_used.append(accounts_key1);accounts_used.append(accounts_key2);accounts_used.append(accounts_key3);accounts_used.append(accounts_key4);accounts_used.append(accounts_other)

            for account in accounts_used:
                if account == "ACC1" or account == "ACC2" or account == "ACC3" or account == "ACC4" or account == "ACC5":
                    user = str(accounts.get(str(account))).split(",")[1]
                    password = str(accounts.get(str(account))).split(",")[2]
                    functions.open_winscp(user, password, server_standalone.get(), sudo_value.get())
                    functions.update_server(w_server, server_standalone.get())
                elif account != "":
                    user = user_standalone.get()
                    password = password_standalone.get()
                    functions.open_winscp(user, password, server_standalone.get(), sudo_value.get())
                    functions.update_server(w_server, server_standalone.get())
        else:
            ip = str(servers.get(str(servers_list.get(servers_list.curselection())))).split(",")[1]
            account = str(servers.get(str(servers_list.get(servers_list.curselection())))).split(",")[2]
            user = str(accounts.get(str(account))).split(",")[1]
            password = str(accounts.get(str(account))).split(",")[2]
            functions.open_winscp(user, password, ip, sudo_value.get())
            functions.update_server(w_server, servers_list.get(servers_list.curselection()))    

    def button_open_winscp():
        do_open_winscp(accounts_key0, accounts_key1, accounts_key2, accounts_key3, accounts_key4, accounts_other, sudo_value)

    def do_open_wfreerdp(accounts_key0, accounts_key1, accounts_key2, accounts_key3, accounts_key4, accounts_other, full_screen_value):

        if server_standalone.get() != "":
            accounts_used = list()
            if accounts_key0.get() != 0:
                accounts_key0 = "ACC1"
            else:
                accounts_key0 =""
            
            if accounts_key1.get() != 0:
                accounts_key1 = "ACC2"
            else:
                accounts_key1 = ""  
            
            if accounts_key2.get() != 0:
                accounts_key2 = "ACC3"
            else:
                accounts_key2 = ""
            
            if accounts_key3.get() != 0:
                accounts_key3 = "ACC4"
            else:
                accounts_key3 = ""
            
            if accounts_key4.get() != 0:
                accounts_key4 = "ACC5"
            else:
                accounts_key4 = ""
            
            if accounts_other.get() != 0:
                accounts_other = user_standalone.get()
            else:
                accounts_other = ""
                
            accounts_used.append(accounts_key0);accounts_used.append(accounts_key1);accounts_used.append(accounts_key2);accounts_used.append(accounts_key3);accounts_used.append(accounts_key4);accounts_used.append(accounts_other)
            title = "Server: "+str(server_standalone.get())
            width = 1440
            height = 900
            for account in accounts_used:
                if account == "ACC1" or account == "ACC2" or account == "ACC3" or account == "ACC4" or account == "ACC5":
                    user_tmp = str(accounts.get(str(account))).split(",")[1]
                    user_name = str(user_tmp).split("@")[0]
                    user_domain = str(user_tmp).split("@")[1]
                    user=user_domain+"\\"+user_name
                    password = str(accounts.get(str(account))).split(",")[2]
                    functions.open_wfreerdp(title, server_standalone.get(), user, password, width, height, full_screen_value.get())
                    functions.update_server(w_server, server_standalone.get())
                elif account != "":
                    user = user_standalone.get()
                    password = password_standalone.get()                    
                    functions.open_wfreerdp(title, server_standalone.get(), user, password, width, height, full_screen_value.get())
                    functions.update_server(w_server, server_standalone.get())
        else:
            title = str(servers.get(str(servers_list.get(servers_list.curselection())))).split(",")[0]
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
        do_open_wfreerdp(accounts_key0, accounts_key1, accounts_key2, accounts_key3, accounts_key4, accounts_other, full_screen_value)
   
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

    def refresh(self):
        root.wm_attributes("-topmost", ontop_value.get())
        
    def do_refresh():
        refresh(root)

    ontop_value = IntVar()
    ontop_value_check = Checkbutton(w_server, text="On Top?", variable=ontop_value, command=do_refresh)
    ontop_value_check.place(x=1, y=1) 

    w_server.pack(padx=1,pady=1, side=LEFT)
    w_buttoms.pack(padx=1,pady=1, side=RIGHT)
    root.wm_attributes("-topmost", ontop_value.get())
    root.resizable(width=False, height=False)
    root.mainloop()

if __name__ == '__main__':
    main()