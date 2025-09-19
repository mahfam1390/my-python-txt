from winreg import *
def disable_cdrom ():
    keyval = r"SYSTEM\CurrentControlSet\Services\USBSTOR"
    try :
        key = OpenKey(HKEY_LOCAL_MACHINE,keyval,0,KEY_ALL_ACCESS)
    except:
        key = CreateKey(HKEY_LOCAL_MACHINE,keyval)
    SetValueEx(key,"Start",0,REG_DWORD,4)
    CloseKey(key)
disable_cdrom()