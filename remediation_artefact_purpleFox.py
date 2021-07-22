import os
import re
import winreg
import subprocess

def rootkit_dll():
    rootkit_here = False
    folder = "C:\\Windows\\System32"

    for file in os.listdir(folder):
        if re.fullmatch(r"Ms[A-Z0-9]{8}App.dll",file):
            print(file)
            try:
                os.remove(os.path.join(folder,file))
                print("dll "+file+" removed !")
            except FileNotFoundError:
                print("fichier non trouvé: "+file)
                return False
            except: 
                print("erreur sur: "+file)
                return False
            rootkit_here = True
    return rootkit_here

def rootkit_sdb():
    rootkit_here = False
    folder = "C:\\Windows\\AppPatch"

    for file in os.listdir(folder):
        if re.fullmatch(r"Ac[A-Z0-9]{8}.sdb",file):
            print(file)
            try:
                os.remove(os.path.join(folder,file))
            except FileNotFoundError:
                print("fichier non trouvé: "+file)
                return False
            except: 
                print("erreur sur: "+file)
                return False
            rootkit_here = True
    return rootkit_here

def rootkit_tmp():
    rootkit_here = False
    folder = "C:\\Windows\\AppPatch\\Custom"

    for file in os.listdir(folder):
        if re.fullmatch(r".{7}.tmp",file):
            print(file)
            try:
                os.remove(os.path.join(folder,file))
            except FileNotFoundError:
                print("fichier non trouvé: "+file)
                return False
            except: 
                print("erreur sur: "+file)
                return False
            rootkit_here = True
    return rootkit_here

def rootkit_moe():
    rootkit_here = False
    folder = "C:\\Windows\\AppPatch\\Custom"

    for file in os.listdir(folder):
        if re.fullmatch(r"[0-9a-zA-Z]*.moe",file):
            print(file)
            try:
                os.remove(os.path.join(folder,file))
            except FileNotFoundError:
                print("fichier non trouvé: "+file)
                return False
            except: 
                print("erreur sur: "+file)
                return False
            rootkit_here = True
    return rootkit_here

def rootkit_xsl():
    rootkit_here = False
    folder = "C:\\Windows\\AppPatch\\"

    for file in os.listdir(folder):
        if re.fullmatch(r"Ke[0-9]{6}.xsl",file):
            print(file)
            try:
                os.remove(os.path.join(folder,file))
            except FileNotFoundError:
                print("fichier non trouvé: "+file)
                return False
            except: 
                print("erreur sur: "+file)
                return False
            rootkit_here = True
    return rootkit_here

def rootkit_driver():
    rootkit_here = False
    folder = "C:\\Windows\\System32\\drivers"

    for file in os.listdir(folder):
        if re.fullmatch(r"dump_[0-9a-zA-Z]*.sys",file):
            print(file)
            try:
                os.remove(os.path.join(folder,file))
            except FileNotFoundError:
                print("fichier non trouvé: "+file)
                return False
            except: 
                print("erreur sur: "+file)
                return False
            rootkit_here = True
    return rootkit_here

def rootkit_folder():
    rootkit_here = False
    folder = "C:\\Program Files"
    try:
        for file in os.listdir(folder):
            if file == "FONDQXIMSYHLISNDBCFPGGQDFFXNKBARIRJH":
                print(file)
                try:
                    os.remove(os.path.join(folder,file))
                except FileNotFoundError:
                    print("fichier non trouvé: "+file)
                    return False
                except: 
                    print("erreur sur: "+file)
                    return False
                rootkit_here = True
        return rootkit_here
    except FileNotFoundError:
        print("C:\\Program does not exist")
        return False

def rootkit_registry(key):
    try:
        registry = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
        rawKey = winreg.OpenKey(registry, key,0,winreg.KEY_ALL_ACCESS)
        for i in range (10000):
            try:
                key_name = winreg.EnumKey(rawKey,i)
                if re.fullmatch(r"Ms[A-Z0-9]{8}App",key_name):
                    winreg.DeleteKey(rawKey,key_name)
                    print("reg key: "+key_name)
                    return True
            except :
                break
        return False
    except WindowsError:
        print("Erreur clé registry")
    return False

def rootkit_registry_value(key):
    try:
        registry = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
        rawKey = winreg.OpenKey(registry, key,0,winreg.KEY_ALL_ACCESS)
        for i in range (10000):
            try:
                key_value = winreg.EnumValue(rawKey,i)
                if re.fullmatch(r"UpdaterLastTimeChecked[1-3]{1}",key_value):
                    winreg.DeleteValue(rawKey,key_value)
                    print("reg key: "+key_value)
                    return True
            except :
                break
        return False
    except FileNotFoundError:
        print("clé non trouvé updater")
        return False
    except WindowsError:
        print("Erreur clé value updater")
        return False

def rootkit_registry_value_2():
    try:
        registry = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
        rawKey = winreg.OpenKey(registry, "Software\\Microsoft\\DirectPlay8\\Direct3D",0,winreg.KEY_ALL_ACCESS)
        for i in range (10000):
            try:
                key_value = winreg.EnumValue(rawKey,i)
                winreg.DeleteValue(rawKey,key_value)
                print("reg key: "+key_value)
                return True
            except :
                break
        return False
    except FileNotFoundError:
        print("clé non trouvé direct3d")
        return False
    except WindowsError:
        print("Erreur clé value direct3d")
        return False

def rootkit_registry_driver(key):
    try:
        registry = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
        rawKey = winreg.OpenKey(registry, key,0,winreg.KEY_ALL_ACCESS)
        for i in range (10000):
            try:
                key_name = winreg.EnumKey(rawKey,i)
                if re.fullmatch(r"dump_[a-zA-Z0-9]*",key_name):
                    winreg.DeleteKey(rawKey,key_name)
                    print("reg key: "+key_name)
                    return True
            except :
                break
        return False
    except WindowsError:
        print("Erreur clé driver")
        return False

def rootkit_reg_svchost():
    try:
        registry = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
        rawKey = winreg.OpenKey(registry, "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Svchost",0,winreg.KEY_ALL_ACCESS)
        for i in range (10000):
            try:
                key_value = winreg.EnumValue(rawKey,i)
                if key_value[0]=="netsvcs":
                    data = key_value[1]
                    for d in data:
                        if re.fullmatch(r"Ms[A-Z0-9]{8}App",d):
                            cmd="$pipes=(Get-ItemProperty \"HKLM:\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Svchost\" -Name netsvcs).netsvcs;$newpipes=$pipes|?{$_ -ne '"+d+"'};Set-ItemProperty \"HKLM:\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Svchost\" -Name netsvcs -Value $newpipes;"
                            subprocess.run(["powershell", "-Command", cmd], capture_output=True)
                            print("reg svchost: "+d)
                            return True
            except :
                break
        return False
    except :
        print ("error reg svchost")
        return False

def main():
    
    a=rootkit_registry("SYSTEM\\ControlSet001\\services")
    b=rootkit_registry("SYSTEM\\CurrentControlSet\\services")
    c=rootkit_registry("SYSTEM\\ControlSet001\\Control\\SafeBoot\\Minimal")
    d=rootkit_registry("SYSTEM\\CurrentControlSet\\Control\\SafeBoot\\Minimal")
    e=rootkit_registry("SYSTEM\\ControlSet001\\Control\\SafeBoot\\Network")
    f=rootkit_registry("SYSTEM\\CurrentControlSet\\Control\\SafeBoot\\Network")
    g=rootkit_registry_driver("SYSTEM\\ControlSet001\\Control\\SafeBoot\\Minimal")
    h=rootkit_registry_driver("SYSTEM\\CurrentControlSet\\Control\\SafeBoot\\Minimal")
    i=rootkit_dll()
    j=rootkit_driver()
    k=rootkit_folder()
    l=rootkit_moe()
    m=rootkit_sdb()
    n=rootkit_tmp()
    o=rootkit_xsl()
    p=rootkit_reg_svchost()
    q=rootkit_registry_value("Software\\SoundResearch")
    r=rootkit_registry_value_2()
    return {'reg_services':a,'reg_services2':b,'reg_minimal':c,'reg_minimal2':d,'reg_network':e,'reg_network2':f,'reg_driver':g,'reg_driver2':h,'dll':i,'driver':j,'folder':k,'moe':l,'sdb':m,'tmp':n,'xsl':o,'reg_svchost':p,'reg_sound':q,'reg_direct3d':r}
