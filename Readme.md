# Con Controller

This is a python 3 script, with a graphical user interface all written with tkinter.

Tested/created with python 3.9.

## Preparing to run

Download the files con_controller.py and functions.py.

Create a folder named Con_controller inside your home directory.

You may create a shortcut at desktop if you like.

Inside the folder Con_controller you need 2 .txt files.

servers.txt and accounts.txt

They must follow the following parameters: (example)

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

The first 6 lines of accounts.txt will appear as check boxes at the gui for quick selection, you may change this editing the code.

### Con controller was written to control 3 different aplications:

>Download putty at <https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html>

>Download winscp at <https://winscp.net/eng/downloads.php#additional>

>Download WfreeRDP for windows at <https://cloudbase.it/freerdp-for-windows-nightly-builds/>

All should be downloaded/unzipped at Con_controller directory.

With this done, we´re good to go :-)

## Running the app

You may type on shell:

```shell
pythonw con_controller.py
```

## Developing

Feel free to download, use and modify it:

```shell
git clone https://github.com/FernandoRD/Con_controller.git
```
