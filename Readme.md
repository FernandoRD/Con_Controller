# Putty Controller

> Use this app to control Putty, Winscp and WFreeRDP <http://www.freerdp.com> sessions.

This is a python 3 script, with a graphical user interface all written with tkinter.

Tested/created with python 3.9.

## Running the app

Download the files putty_controller.py and functions.py anywhere, then run:

```shell
pythonw putty_controller.py
```
You may create a shortcut if you like.

Before running you need to fill the two text files, servers.txt and accounts.txt in the following way:

```shell
servers.txt
Server1_name,192.168.0.1,account1_name,
Server2_name,192.168.0.2,account2_name,
Server3_RDP_name,192.168.0.3,account3_name,width,height,

accounts.txt 
account1_name,user,password,
account2_name,user,password,
account3_name,user,password,
```

Those files should be placed at your Documents folder.

Download putty at <https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html>

Download winscp at <https://winscp.net/eng/downloads.php#additional>

Download WfreeRDP for windows at <https://cloudbase.it/freerdp-for-windows-nightly-builds/>

All should be downloaded/unzipped at your home directory.

Those locations can be changed in the code, in fact winscp version is hardcoded, please change it accordingly.

With this done, we´re good to go :-)

## Developing

Feel free to download, use and modify it:

```shell
git clone https://github.com/FernandoRD/putty_controller.git
```
