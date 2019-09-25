#decompiled by MRLINKERRORSYSTEM
import os, sys
print '''
            SELAMAT DATANG
                 DI
      TOOLS MRLINKERRORSYSTEM
           CODE: BY MRLINKERRORSYSTEM
     FACEBOOK HACKING SYSTEM FAST CRACK 
 _____              _                 _
|  ___|_ _  ___ ___| |__   ___   ___ | | __
| |_ / _` |/ __/ _ \ '_ \ / _ \ / _ \| |/ /
|  _| (_| | (_|  __/ |_) | (_) | (_) |   <
|_|  \__,_|\___\___|_.__/ \___/ \___/|_|\_\                                '''

print '\x1b[1;33mSudah punya ID dan Password nya?'
print '\x1b[1;32mSilahkan Login '
import os, sys

def wa():
    os.system('xdg-open https://api.whatsapp.com/send?phone=6281249281196&text=Assalamualaikum')


def restart():
    ngulang = sys.executable
    os.execl(ngulang, ngulang, *sys.argv)


user = raw_input('ID: ')
import getpass
sandi = raw_input('Password: ')
if sandi == 'ganteng' and user == 'Mrlink':
    print 'Kamu Telah Login System Saya'
    sys.exit
else:
    print 'Login GAGAL, Silahkan hubungi Saya'
    wa()
    restart()
