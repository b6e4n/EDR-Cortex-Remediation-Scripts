import sys
import winreg
import os
import traceback
import subprocess

worms_persitance = ["SysinfY2X","SysinfYhX","Vlce","Vlc","cste","Video","7","MerciJacquieMichel","iTunesHelper","urctjdizmf.","flashmemory","t61yDQ6g","221","SURVIVAL","BronCoder","Facebook","smougen","igfxnself","8","updat","223","Desktop","mhH5Vwcp","Microsoft","4bfQdD4h","A7KGEquN","httpwww.xnxx.comvideo6836063super_cumshot","mH5Vwcp"]
worms_files = ["%Appdata%\\Temp\\SysinfY2X.db","%Appdata%\\Temp\\SysinfYhX.db","C:\\g-avc-ssiap\\Vlce.rar","D:\\$RECYCLEBIN\\Vlc.rar","%Appdata%\\Microsoft\\SYSTEM\\cste ","%Appdata%\\Video.3gp","%Appdata%\\Temp\\7.vbe","%Appdata%\\Temp\\MerciJacquieMichel.vbe","%Appdata%\\Temp\\iTunesHelper.vbe","%Appdata%\\Temp\\urctjdizmf..vbe","%Appdata%\\Temp\\flasmemory.vbe","%Appdata%\\Temp\\t61yDQ6g.vbs","%Appdata%\\Temp\\221.vbe","%Appdata%\\Temp\\SURVIVAL.vbe","%Appdata%\\Temp\\BronCoder.wsf","%Appdata%\\Temp\\Facebook.vbs","%Appdata%\\Temp\\smougen.vbs","%Appdata%\\Temp\\igfxnself.vbs","%Appdata%\\Temp\\8.vbs","%Appdata%\\Temp\\updat.vbs","%Appdata%\\Temp\\223.vbe","%Appdata%\\Temp\\Desktop.vbs","%Appdata%\\Temp\\mhH5Vwcp.vbs","%Appdata%\\Temp\\Microsoft.vbe","%Appdata%\\Temp\\4bfQdD4h.vbs","%Appdata%\\Temp\A7KGEquN.vbs","%Appdata%\\Temp\httpwww.xnxx.comvideo6836063super_cumshot.vbs","%Appdata%\\Temp\\mH5Vwcp.vbs"]


def enumerate_user_key():
    a=[]
    for i in range(0,100):
        try:
            key = winreg.EnumKey(winreg.HKEY_USERS,i)
            a.append(key)
        except WindowsError:
            break
    return a

def delete_file(file_path):
    path = os.path.expanduser(file_path)
    path = os.path.expandvars(path)
    if os.path.isabs(path):
        try:
            if(os.path.exists(file_path)):
                os.remove(path)
                print("deleted "+path)
        except IOError:
            sys.stderr.write(f"File not accessible: {path}\n")
            return False
        except Exception:
            sys.stderr.write(f"Exception occured: {traceback.format_exc()}")
            return False
    return True
    
def delete_registry_key_v3(key, worm):
    try:
        registry = winreg.ConnectRegistry(None, winreg.HKEY_USERS)
        rawKey = winreg.OpenKey(registry, key+"\\Software\\Microsoft\\Windows\\CurrentVersion\\Run",0,winreg.KEY_ALL_ACCESS)
        rawValue = winreg.QueryValueEx(rawKey,worm)
        winreg.DeleteValue(rawKey,worm)
        print(rawValue)
        return True
    except:
        return False


def main():
    result_script = False
    keys = enumerate_user_key()
    try:
        for key in keys:
            for worm in worms_persitance:
                action = delete_registry_key_v3(key,worm)
                if(action):
                    print("deleted !")
                    result_script = True
        
        for vbfile in worms_files:
            delete_file(vbfile)

        return result_script
            
            
    except PermissionError as e:
        sys.stderr.write(f"Access is denied to registry key: \n")
        raise e
    except OSError as e:
        sys.stderr.write(f"Registry key  not found\n")
        raise e
    except IOError:
        sys.stderr.write(f"File not accessible:")
    except Exception as e:
        sys.stderr.write(f"Exception occured: {traceback.format_exc()}")
        raise e
    except :
        print("failed")
        raise
