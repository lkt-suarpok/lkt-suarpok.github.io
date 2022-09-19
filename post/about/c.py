import asyncio #line:1
import aiohttp #line:2
from fake_useragent import UserAgent #line:3
from time import sleep #line:4
from random import randint ,choice #line:5
import requests #line:6
from datetime import datetime ,timedelta ,timezone #line:7
async def getheaders ():#line:10
    O0OOOO00000000OO0 =UserAgent ().random #line:11
    O00O00O0OO0OOO00O ={'User-Agent':O0OOOO00000000OO0 ,"Host":"www.maimemo.com","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language":"zh-CN,zh-Hans;q=0.9","Connection":"keep-alive","Accept-Encoding":"gzip, deflate, br"}#line:20
    return O00O00O0OO0OOO00O #line:21
async def create_aiohttp (O00000000000OOOO0 ):#line:23
    async with aiohttp .ClientSession ()as OO0000000O0O0OOO0 :#line:24
        O00O000OO000000OO =[asyncio .create_task (web_request (O00000000000OOOO0 ,OO0000000O0O0OOO0 ))]#line:26
        await asyncio .wait (O00O000OO000000OO )#line:27
async def web_request (OOOO0OO000000O0O0 ,O00O0OO0O0O00OOOO ):#line:30
    async with asyncio .Semaphore (5 ):#line:32
        try :#line:33
            async with await O00O0OO0O0O00OOOO .get (url =OOOO0OO000000O0O0 ,headers =await getheaders (),timeout =aiohttp .ClientTimeout (total =10 ))as OO000O0OOO00O000O :#line:35
                O00O00000O00OOO0O =await OO000O0OOO00O000O .text ()#line:37
                await page (O00O00000O00OOO0O )#line:38
        except Exception :#line:39
            pass #line:40
async def page (OO00O0OOOO000OOOO ):#line:43
    global n #line:44
    n =0 #line:45
    if "学习天数"in OO00O0OOOO000OOOO :#line:46
        n +=1 #line:47
def getip ():#line:50
    OO00O0OOO0O0O0OOO ='http://myip.ipip.net'#line:51
    OO00OOOOO00O0O0OO ={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}#line:54
    try :#line:55
        O000O00OO00000O0O =requests .get (OO00O0OOO0O0O0OOO ,headers =OO00OOOOO00O0O0OO ).text #line:56
        O00O0OO00000OOO0O =O000O00OO00000O0O #line:58
        print (O00O0OO00000OOO0O )#line:59
        return O00O0OO00000OOO0O #line:60
    except Exception as OOOOO0O0000OO0O0O :#line:61
        print (OOOOO0O0000OO0O0O )#line:62
def randomszxx ():#line:65
    OOOO0O0O0O0OOO00O ='qwertyuioplkjhgfdsazxcvbnm1234567890'#line:66
    O0O0OO0000OO0O00O =''#line:67
    for OOO00OOO0O00000OO in range (0 ,64 ):#line:68
        OO00OO0OO000O00OO =choice (OOOO0O0O0O0OOO00O )#line:69
        O0O0OO0000OO0O00O +=OO00OO0OO000O00OO #line:70
    return O0O0OO0000OO0O00O #line:72
def getlink (OO000O000O0OOOO0O ):#line:75
    OO0O0O0OOO00OO00O ="https://www.maimemo.com/share/title"#line:76
    OOOOOO00OOOOO0000 =randomszxx ()#line:77
    O000O0OOO0OO0000O ={"Host":"www.maimemo.com","Content-Type":"application/json","Accept-Encoding":"gzip, deflate, br","Connection":"keep-alive","Ignorable":"false","Accept":"*/*","User-Agent":"MaiMemo/4.4.30_7389 iOS/15.6 Device/iPad11,1 (ARM_64) Resolution/1536x2048 RAM/2.85 ROM/238.41 DId/4d1bc2f7f864b4afe57a4f30fa095932 InstallId/b1133f859c90e20bf392e1c4cfece593 DeviceName/C%20%20iPad Jbv/NIL AFNetworking/3.2.1 Timezone/Asia%2FShanghai+08:00 Theme/Day","Accept-Language":"zh-Hans-CN;q=1","Content-Length":"34","token":OOOOOO00OOOOO0000 }#line:89
    OO0O0O0O00OO0000O ={"uid":OO000O000O0OOOO0O ,"action":"share"}#line:93
    try :#line:94
        O000OO00O000O0O00 =requests .post (OO0O0O0OOO00OO00O ,headers =O000O0OOO0OO0000O ,data =json .dumps (OO0O0O0O00OO0000O ))#line:95
        OO00000OO0OO00O0O =json .loads (O000OO00O000O0O00 .text )#line:96
        if 'uid'in str (OO00000OO0OO00O0O ):#line:97
            OOO0OO0O00000O0O0 =OO00000OO0OO00O0O ['page']#line:98
            O0OOO0O0O0OO0OOOO =OOO0OO0O00000O0O0 .find ('page/?')#line:99
            OOO0OO0O00000O0O0 ='https://www.maimemo.com/share/page?'+OOO0OO0O00000O0O0 [O0OOO0O0O0OO0OOOO +6 :]#line:100
            print (f'link获取成功，为{OOO0OO0O00000O0O0}')#line:101
            return OOO0OO0O00000O0O0 #line:102
    except Exception as O0000OO000OOOO000 :#line:103
        print (O0000OO000OOOO000 )#line:104
def getlists (OO00O0O00OOOO00O0 ):#line:106
    OO00O0O00OOOO00O0 =OO00O0O00OOOO00O0 [OO00O0O00OOOO00O0 .find ('&pid=')+5 :OO00O0O00OOOO00O0 .find ('&tid=')]#line:107
    O0O00O0OOO0000OOO =f'https://api.maimemo.com/api/v1/sharecontents/{OO00O0O00OOOO00O0}/comments?token=null&offset=5&limit=100&hideUnreviewed=true'#line:108
    OO0OO0OOO0OO00OOO ={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}#line:111
    try :#line:112
        O0O000OO0O00O000O =requests .get (O0O00O0OOO0000OOO ,headers =OO0OO0OOO0OO00OOO )#line:113
        OO0OOO0OO0OOOOOO0 =json .loads (O0O000OO0O00O000O .text )#line:114
        OO0OOO0OO0OOOOOO0 =OO0OOO0OO0OOOOOO0 ['data']['comments']#line:115
        OO0O0O0O00OOOOO0O =len (OO0OOO0OO0OOOOOO0 )#line:116
        print (f'=======共找到{OO0O0O0O00OOOOO0O}条记录=======')#line:117
        O0OOO00000O00OOO0 =0 #line:118
        while O0OOO00000O00OOO0 <OO0O0O0O00OOOOO0O :#line:119
            OOOOO00O00O0OOOO0 =OO0OOO0OO0OOOOOO0 [O0OOO00000O00OOO0 ]['creator']['uid']#line:120
            OOO0OO0O0O000000O =getlink (OOOOO00O00O0OOOO0 )#line:121
            asyncio .run (create_aiohttp (OOO0OO0O0O000000O ))#line:122
            sleep (randint (1 ,2 ))#line:123
            print (f"{OOOOO00O00O0OOOO0}墨墨分享链接访问成功{n}次")#line:124
            O0OOO00000O00OOO0 +=1 #line:125
    except Exception as OOOO00000OOOOOOO0 :#line:126
        print (OOOO00000OOOOOOO0 )#line:127
uidarr =['10229269']#line:129
def main ():#line:131
    getip ()#line:132
    for OOOO0O00OOOO0OO00 in range (len (uidarr )):#line:133
        O0OO0OO00O00O000O =uidarr [OOOO0O00OOOO0OO00 ]#line:134
        O0O0OO0O0OOOOO000 =getlink (O0OO0OO00O00O000O )#line:135
        asyncio .run (create_aiohttp (O0O0OO0O0OOOOO000 ))#line:136
        print (f"{O0OO0OO00O00O000O}墨墨分享链接访问成功{n}次。")#line:137
        sleep (randint (1 ,2 ))#line:138
    getlists (O0O0OO0O0OOOOO000 )#line:139
    getip ()#line:140
if __name__ =='__main__':#line:143
    main ()
