from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5 import QtCore
import psutil
from PyQt5.QtGui import QFont
import ctypes
import os
import sys
import wmi
import platform
from PyQt5.QtCore import Qt
import screen_brightness_control as sbc
import subprocess
import socket
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import winreg
pr=''
REG_PATH = r'Software\Microsoft\Windows\CurrentVersion\Internet Settings'
def get_reg(ad):
    global pr
    try:
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0,
                                       winreg.KEY_READ)
        value, regtype = winreg.QueryValueEx(registry_key, ad)
        winreg.CloseKey(registry_key)
        return value
    except WindowsError:
        return None
liste7=[]
try:
    liste7.append((f"Memory :{psutil.virtual_memory()}"))
    liste8=[]
    liste8.append(liste7[0].split(" "))
    liste9=[]
    liste9.append(int(liste8[0][1][13:][:-1]))
    liste9.append(int(liste8[0][2][10:][:-1]))
    liste9.append(float(liste8[0][3][8:][:-1]))
    liste9.append(int(liste8[0][4][5:][:-1]))
except:
    liste8=[]
    liste8.append("---")

    liste9=[]
    liste9.append("---")
    liste9.append("---")
    liste9.append("---")
    liste9.append("---")


pr=get_reg('ProxyServer')
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
   IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
my_system1 = platform.uname()
c = wmi.WMI()   
my_system = c.Win32_ComputerSystem()[0]
userhome = os.path.expanduser('~')

liste=[]
liste.append("İstehsalçı : "+ my_system.Manufacturer)
liste.append("Model : "+ my_system.Model)
liste.append("Kompyuter adı : "+ my_system.Name)
liste.append("Prosessor sayı : "+ str(my_system.NumberOfProcessors))
liste.append("Sistem tipi : "+ my_system.SystemType)
liste.append("Sistem ailesi : "+ my_system.SystemFamily)
liste.append("Emeliyyat sistem : "+ my_system1.system+my_system1.release)
liste.append("Versiyası : "+ my_system1.version)
liste.append("Prosessor : "+ my_system1.processor)
liste.append("İstifadeçi : " + os.path.split(userhome)[-1])
try:
    liste.append("IP ünvanı : "+ [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1][0])
except:
    liste.append("IP ünvanı :      ")
    
liste.append("Proxy : "+pr)
try:
    liste.append("RAM : "+str(round(liste9[0]/1024/1024/1024,2))+" GB"+"      Boş: "+str(round(liste9[1]/1024/1024/1024,2))+" GB"+"     İstifadede : "+str(round(liste9[3]/1024/1024/1024,2))+" GB"+"     Faiz : "+str(float(liste8[0][3][8:][:-1]))+"%")
except:
    liste.append("RAM : "+liste9[0]+" GB"+"      Boş: "+liste9[1]+" GB"+"     İstifadede : "+liste9[3]+" GB"+"     Faiz : "+liste8[0]+"%")

text="\n"+"   "+liste[0]+"\n"+"   "+liste[1]+"\n"+"   "+liste[2]+"\n"+"   "+liste[3]+"\n"+"   "+liste[4]+"\n"+"   "+liste[5]+"\n"+"   "+liste[6]+"\n"+"   "+liste[7]+"\n"+"   "+liste[8]+"\n"+"   "+liste[9]+"\n"+"   "+liste[10]+"\n"+"   "+"Proxy : "+get_reg('ProxyServer')+"\n"+"   "+liste[12]+"\n\n\n\n"+"    İşıq    Proxy  Ses"
    

class Pencere(QWidget,Qt):
    def __init__(self):
        super().__init__()
        yazi = QLabel( self)
        yazi.setText(text)
        yazi.setFont(QFont('Arial', 9))
        yazi.setStyleSheet('color:#ffffff;font:bold')
        self.setWindowTitle("HelpCom v1.0")
        self.setWindowIcon(QtGui.QIcon('el.png')) 
        self.setFixedSize(548,277)
        self.move(200,200)
        self.setStyleSheet("background-color:#1b70ff")
        

############################### DIAL DUYMELER ######################################

        self.dial=QDial(self)
        self.dial.setMinimum(0)
        self.dial.setMaximum(100)
        self.dial.setGeometry(3,215,40,40)
        self.dial.setValue(sbc.get_brightness()[0])
        self.dial.valueChanged.connect(self.isiq)
        self.dial.setStyleSheet("background-color : brown ;")

        self.dial2=QDial(self)
        self.dial2.setMinimum(1)
        self.dial2.setMaximum(65)
        self.dial2.setGeometry(80,215,40,40)
        self.dial2.valueChanged.connect(self.isiq)
        print(65+int(volume.GetMasterVolumeLevel()))
        self.dial2.setValue(65+int(volume.GetMasterVolumeLevel()))
        self.dial2.valueChanged.connect(self.ses)
        self.dial2.setStyleSheet("background-color : brown ;")
      
############################### SEKILLI DUYMELER ######################################
        
        self.duyme=QPushButton(self)
        self.duyme.clicked.connect(self.enerji)
        self.duyme.setGeometry(443,5,50,50)
        self.duyme.setStyleSheet("background-image : url(enerji.png);")

        self.duyme=QPushButton(self)
        self.duyme.clicked.connect(self.internet)
        self.duyme.setGeometry(443,60,50,50)
        self.duyme.setStyleSheet("background-image : url(internet_parametrleri.png);")


        self.duyme=QPushButton(self)
        self.duyme.clicked.connect(self.tapsiriq)
        self.duyme.setGeometry(443,115,50,50)
        self.duyme.setStyleSheet("background-image : url(tapsiriq.png);")

        self.duyme=QPushButton(self)
        self.duyme.clicked.connect(self.sistem)
        self.duyme.setGeometry(443,170,50,50)
        self.duyme.setStyleSheet("background-image : url(sistem.png);")

        self.duyme=QPushButton(self)
        self.duyme.clicked.connect(self.qurgular)
        self.duyme.setGeometry(495,5,50,50)
        self.duyme.setStyleSheet("background-image : url(hardware.png);")

        self.duyme=QPushButton(self)
        self.duyme.clicked.connect(self.directx)
        self.duyme.setGeometry(495,60,50,50)
        self.duyme.setStyleSheet("background-image : url(directX.png);")

        self.duyme=QPushButton(self)
        self.duyme.clicked.connect(self.comp)
        self.duyme.setGeometry(495,115,50,50)
        self.duyme.setStyleSheet("background-image : url(comp.png);")

        self.duyme=QPushButton(self)
        self.duyme.clicked.connect(self.add)
        self.duyme.setGeometry(495,170,50,50)
        self.duyme.setStyleSheet("background-image : url(add.png);")

        self.duyme=QPushButton(self)
        self.duyme.clicked.connect(self.qurgu)
        self.duyme.setGeometry(495,225,50,50)
        self.duyme.setStyleSheet("background-image : url(qurgu.png);")

        self.duyme=QPushButton(self)
        self.duyme.clicked.connect(self.temizle)
        self.duyme.setGeometry(443,225,50,50)
        self.duyme.setStyleSheet("background-image : url(disksil.png);")

        self.duyme=QPushButton(self)
        self.duyme.clicked.connect(self.restart)
        self.duyme.setGeometry(391,60,50,50)
        self.duyme.setStyleSheet("background-image : url(restart.png);")

        self.duyme=QPushButton(self)
        self.duyme.clicked.connect(self.kilit)
        self.duyme.setGeometry(391,115,50,50)
        self.duyme.setStyleSheet("background-image : url(kilit.png);")

        self.duyme=QPushButton(self)
        self.duyme.clicked.connect(self.ekran)
        self.duyme.setGeometry(391,170,50,50)
        self.duyme.setStyleSheet("background-image : url(ekran.png);")

        self.duyme=QPushButton(self)
        self.duyme.clicked.connect(self.bolge)
        self.duyme.setGeometry(391,225,50,50)
        self.duyme.setStyleSheet("background-image : url(bolge.png);")
        

        self.duyme=QPushButton(self)
        self.duyme.clicked.connect(self.shutdown)
        self.duyme.setGeometry(391,5,50,50)
        self.duyme.setStyleSheet("background-image : url(shutdown.png);")

############################### YAZILI DUYMELER ######################################

        self.duyme=QPushButton(self)
        self.duyme.clicked.connect(self.powershell)
        self.duyme.setGeometry(122,225,85,23)
        self.duyme.setStyleSheet("background-color : white;")
        self.duyme.setText("Power Shell")

        self.duyme=QPushButton(self)
        self.duyme.setGeometry(41,222,42,25)
        self.duyme.setStyleSheet("background-image : url(ox.png);")
        self.duyme.clicked.connect(self.proxydeyis)
        #self.duyme.setText("Deyiş")

        self.duyme=QPushButton(self)
        self.duyme.clicked.connect(self.idare)
        self.duyme.setGeometry(122,250,85,23)
        self.duyme.setStyleSheet("background-color : white;")
        self.duyme.setText("İdareetme paneli")

        self.duyme=QPushButton(self)
        self.duyme.clicked.connect(self.fealiyyetler)
        self.duyme.setGeometry(212,250,85,23)
        self.duyme.setStyleSheet("background-color : white;")
        self.duyme.setText("Fealiyyetler")

        self.duyme=QPushButton(self)
        self.duyme.clicked.connect(self.performans)
        self.duyme.setGeometry(301,250,85,23)
        self.duyme.setStyleSheet("background-color : white;")
        self.duyme.setText("Performans")

        self.duyme=QPushButton(self)
        self.duyme.clicked.connect(self.regedit)
        self.duyme.setGeometry(212,225,85,23)
        self.duyme.setStyleSheet("background-color : white;")
        self.duyme.setText("Regedit")

        self.duyme=QPushButton(self)
        self.duyme.clicked.connect(self.cmd)
        self.duyme.setGeometry(301,225,85,23)
        self.duyme.setStyleSheet("background-color : white;")
        self.duyme.setText("Command")
        

############################### DUYME FUNKSIYALARI ######################################

    def proxydeyis(self):
        global text
        global pr
        import winreg
        print (pr)
        if pr== "http://nmrjusproxy01:8080" or pr=="nmrjusproxy01:8080":
            def proxy():
                def set_key(name, value):
                    _, reg_type = winreg.QueryValueEx(INTERNET_SETTINGS, name)
                    winreg.SetValueEx(INTERNET_SETTINGS, name, 0, reg_type, value)
                INTERNET_SETTINGS = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Internet Settings',0, winreg.KEY_ALL_ACCESS)
                a=winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Internet Settings',0, winreg.KEY_ALL_ACCESS)
                winreg.SetValueEx(INTERNET_SETTINGS, "ProxyServer", 0, winreg.REG_SZ, "172.16.1.141:3128")
            proxy()
            pr="172.16.1.141:3128"
            text="\n"+"   "+liste[0]+"\n"+"   "+liste[1]+"\n"+"   "+liste[2]+"\n"+"   "+liste[3]+"\n"+"   "+liste[4]+"\n"+"   "+liste[5]+"\n"+"   "+liste[6]+"\n"+"   "+liste[7]+"\n"+"   "+liste[8]+"\n"+"   "+liste[9]+"\n"+"   "+liste[10]+"\n"+"   "+"Proxy : "+get_reg('ProxyServer')+"\n"+"   "+liste[12]+"\n\n\n\n"+"    İşıq    Proxy  Ses"
            print (pr)
        elif pr=="172.16.1.141:3128":
            def proxyqaytar():
                def set_key(name, value):
                    _, reg_type = winreg.QueryValueEx(INTERNET_SETTINGS, name)
                    winreg.SetValueEx(INTERNET_SETTINGS, name, 0, reg_type, value)
                INTERNET_SETTINGS = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Internet Settings',0, winreg.KEY_ALL_ACCESS)
                a=winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Internet Settings',0, winreg.KEY_ALL_ACCESS)
                winreg.SetValueEx(INTERNET_SETTINGS, "ProxyServer", 0, winreg.REG_SZ, "http://nmrjusproxy01:8080")
                winreg.SetValueEx(INTERNET_SETTINGS, "ProxyOverride", 0, winreg.REG_SZ, "*ehm.e-imza.az;*hom.e-imza.az;*e-imza.az;10.1.3.6;http://pdcis-test.justice.loc;172.16.1.*;172.16.2.*;10.16.1.*;10.17.1.*;10.102.40.*;10.101.1.*;10.40.2.*;10.90.1.*;85.132.58.12;bprorec*;cms*;dms*;emf*;tasks.cms;bprorec.justice.loc;*.justice.loc;e-mehkeme.gov.az;localhost*;10.168.170.*;172.16.7.30;meet.e-mehkeme.gov.az;hr.justice.loc;<local>")
            proxyqaytar()
            pr="http://nmrjusproxy01:8080"
            text="\n"+"   "+liste[0]+"\n"+"   "+liste[1]+"\n"+"   "+liste[2]+"\n"+"   "+liste[3]+"\n"+"   "+liste[4]+"\n"+"   "+liste[5]+"\n"+"   "+liste[6]+"\n"+"   "+liste[7]+"\n"+"   "+liste[8]+"\n"+"   "+liste[9]+"\n"+"   "+liste[10]+"\n"+"   "+"Proxy : "+get_reg('ProxyServer')+"\n"+"   "+liste[12]+"\n\n\n\n"+"    İşıq    Proxy  Ses"
            print(pr)
        else:
            print (pr)

    def comp(self):
        try:
            subprocess.call('compmgmt.msc',shell=True)
        except:
            a=QMessageBox()
            a.setWindowTitle("Diqqət")
            a.setText("Verilən əmri yerinə yetirmək mümkün olmadı...")
            a.setIcon(QMessageBox.Warning)
            a.exec()


    def bolge(self):
        try:
            subprocess.call('intl.cpl',shell=True)
        except:
            a=QMessageBox()
            a.setWindowTitle("Diqqət")
            a.setText("Verilən əmri yerinə yetirmək mümkün olmadı...")
            a.setIcon(QMessageBox.Warning)
            a.exec()


    def ekran(self):
        try:
            subprocess.call('desk.cpl',shell=True)
        except:
            a=QMessageBox()
            a.setWindowTitle("Diqqət")
            a.setText("Verilən əmri yerinə yetirmək mümkün olmadı...")
            a.setIcon(QMessageBox.Warning)
            a.exec()


    def kilit(self):
        try:
            ctypes.windll.user32.LockWorkStation ()
        except:
            a=QMessageBox()
            a.setWindowTitle("Diqqət")
            a.setText("Verilən əmri yerinə yetirmək mümkün olmadı...")
            a.setIcon(QMessageBox.Warning)
            a.exec()


    def directx(self):
        try:
            subprocess.call('dxdiag.exe',shell=True)
        except:
            a=QMessageBox()
            a.setWindowTitle("Diqqət")
            a.setText("Verilən əmri yerinə yetirmək mümkün olmadı...")
            a.setIcon(QMessageBox.Warning)
            a.exec()

    def qurgular(self):
        try:
            os.system('hdwwiz.cpl')
        except:
            a=QMessageBox()
            a.setWindowTitle("Diqqət")
            a.setText("Verilən əmri yerinə yetirmək mümkün olmadı...")
            a.setIcon(QMessageBox.Warning)
            a.exec()

    def tapsiriq(self):
        try:
            subprocess.call('taskmgr.exe',shell=True)
        except:
            a=QMessageBox()
            a.setWindowTitle("Diqqət")
            a.setText("Verilən əmri yerinə yetirmək mümkün olmadı...")
            a.setIcon(QMessageBox.Warning)
            a.exec()

    def internet(self):
        try:
            subprocess.call('inetcpl.cpl',shell=True)       
        except:
            a=QMessageBox()
            a.setWindowTitle("Diqqət")
            a.setText("Verilən əmri yerinə yetirmək mümkün olmadı...")
            a.setIcon(QMessageBox.Warning)
            a.exec()

    def enerji(self):
        try:
            subprocess.call('powercfg.cpl',shell=True)
        except:
            a=QMessageBox()
            a.setWindowTitle("Diqqət")
            a.setText("Verilən əmri yerinə yetirmək mümkün olmadı...")
            a.setIcon(QMessageBox.Warning)
            a.exec()

    def add(self):
        try:
            subprocess.call('appwiz.cpl',shell=True)
        except:
            a=QMessageBox()
            a.setWindowTitle("Diqqət")
            a.setText("Verilən əmri yerinə yetirmək mümkün olmadı...")
            a.setIcon(QMessageBox.Warning)
            a.exec()

    def sistem(self):
        try:
            subprocess.call('sysdm.cpl',shell=True)
        except:
            a=QMessageBox()
            a.setWindowTitle("Diqqət")
            a.setText("Verilən əmri yerinə yetirmək mümkün olmadı...")
            a.setIcon(QMessageBox.Warning)
            a.exec()
 
    def cmd(self):
        try:
            subprocess.run(["start", "/wait", "cmd", "/K",  "arg /?\^"], shell=True)
            #os.system("start /wait cmd ")
        except:
            a=QMessageBox()
            a.setWindowTitle("Diqqət")
            a.setText("Verilən əmri yerinə yetirmək mümkün olmadı...")
            a.setIcon(QMessageBox.Warning)
            a.exec()
           

    def isiq (self):
        try:
            sbc.set_brightness(self.dial.value(), display=0)
        except:
            a=QMessageBox()
            a.setWindowTitle("Diqqət")
            a.setText("Verilən əmri yerinə yetirmək mümkün olmadı...")
            a.setIcon(QMessageBox.Warning)
            a.exec()

    def ses(self):
        try:
            volume.SetMasterVolumeLevel(0-(66-(self.dial2.value())),None)
        except:
            a=QMessageBox()
            a.setWindowTitle("Diqqət")
            a.setText("Verilən əmri yerinə yetirmək mümkün olmadı...")
            a.setIcon(QMessageBox.Warning)
            a.exec()

    def qurgu(self):
        try:
            subprocess.call('%windir%\explorer.exe shell:::{A8A91A66-3A7D-4424-8D24-04E180695C7A}', shell=True);
        except:
            a=QMessageBox()
            a.setWindowTitle("Diqqət")
            a.setText("Verilən əmri yerinə yetirmək mümkün olmadı...")
            a.setIcon(QMessageBox.Warning)
            a.exec()

    def temizle(self):
        try:
            subprocess.call('c:\windows\SYSTEM32\cleanmgr.exe');
        except:
            a=QMessageBox()
            a.setWindowTitle("Diqqət")
            a.setText("Verilən əmri yerinə yetirmək mümkün olmadı...")
            a.setIcon(QMessageBox.Warning)
            a.exec()

    def powershell(self):
        try:
            #subprocess.call('powershell.exe')
            os.system("powershell.exe")
        except:
            a=QMessageBox()
            a.setWindowTitle("Diqqət")
            a.setText("Verilən əmri yerinə yetirmək mümkün olmadı...")
            a.setIcon(QMessageBox.Warning)
            a.exec()

    def idare(self):
        try:
            subprocess.call('control.exe', shell=True);
        except:
            a=QMessageBox()
            a.setWindowTitle("Diqqət")
            a.setText("Verilən əmri yerinə yetirmək mümkün olmadı...")
            a.setIcon(QMessageBox.Warning)
            a.exec()

    def fealiyyetler(self):
        try:
            subprocess.call('eventvwr.msc', shell=True);
        except:
            a=QMessageBox()
            a.setWindowTitle("Diqqət")
            a.setText("Verilən əmri yerinə yetirmək mümkün olmadı...")
            a.setIcon(QMessageBox.Warning)
            a.exec()

    def performans(self):
        try:
            subprocess.call('resmon.exe',shell=True)
        except:
            a=QMessageBox()
            a.setWindowTitle("Diqqət")
            a.setText("Verilən əmri yerinə yetirmək mümkün olmadı...")
            a.setIcon(QMessageBox.Warning)
            a.exec()

    def regedit(self):
        try:
            subprocess.call('regedit.exe',shell=True)
        except:
            a=QMessageBox()
            a.setWindowTitle("Diqqət")
            a.setText("Verilən əmri yerinə yetirmək mümkün olmadı...")
            a.setIcon(QMessageBox.Warning)
            a.exec()

    def shutdown(self):
        try:
            os.system('shutdown /p /f')
        except:
            a=QMessageBox()
            a.setWindowTitle("Diqqət")
            a.setText("Verilən əmri yerinə yetirmək mümkün olmadı...")
            a.setIcon(QMessageBox.Warning)
            a.exec()

    def restart(self):
        try:
            os.popen("shutdown -r -t 01")
        except:
            a=QMessageBox()
            a.setWindowTitle("Diqqət")
            a.setText("Verilən əmri yerinə yetirmək mümkün olmadı...")
            a.setIcon(QMessageBox.Warning)
            a.exec()

app = QApplication(sys.argv)
pencere = Pencere()
pencere.show()
app.exec_()
