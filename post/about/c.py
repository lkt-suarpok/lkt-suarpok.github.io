import asyncio #line:1
import aiohttp #line:2
from fake_useragent import UserAgent #line:3
from time import sleep #line:4
from random import randint ,choice #line:5
import requests #line:6
import json #line:7
async def getheaders ():#line:9
    OO0OO0OO0O0O00OOO =UserAgent ().random #line:10
    OO0000OOO0OO00O00 ={'User-Agent':OO0OO0OO0O0O00OOO ,"Host":"www.maimemo.com","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language":"zh-CN,zh-Hans;q=0.9","Connection":"keep-alive","Accept-Encoding":"gzip, deflate, br"}#line:19
    return OO0000OOO0OO00O00 #line:20
async def create_aiohttp (OO000OO00OO0OO00O ):#line:22
    async with aiohttp .ClientSession ()as OOOO00OOO0O00O0O0 :#line:23
        OOO0OOO0O0OO00O0O =[asyncio .create_task (web_request (OO000OO00OO0OO00O ,OOOO00OOO0O00O0O0 ))]#line:25
        await asyncio .wait (OOO0OOO0O0OO00O0O )#line:26
async def web_request (O0O0000O0000O0O00 ,OOOO000000OO0OOOO ):#line:29
    async with asyncio .Semaphore (5 ):#line:31
        try :#line:32
            async with await OOOO000000OO0OOOO .get (url =O0O0000O0000O0O00 ,headers =await getheaders (),timeout =aiohttp .ClientTimeout (total =10 ))as OO00O00OOOO000000 :#line:34
                OO0000OO00OOO0OOO =await OO00O00OOOO000000 .text ()#line:36
                await page (OO0000OO00OOO0OOO )#line:37
        except Exception :#line:38
            pass #line:39
async def page (OO00O0O0O000OO00O ):#line:42
    global n #line:43
    n =0 #line:44
    if "学习天数"in OO00O0O0O000OO00O :#line:45
        n +=1 #line:46
def getip ():#line:49
    OOOOO0OO0000O0O00 ='http://myip.ipip.net'#line:50
    O0O0OOOOOOOO0O000 ={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}#line:53
    try :#line:54
        O00OO00O0000000O0 =requests .get (OOOOO0OO0000O0O00 ,headers =O0O0OOOOOOOO0O000 ).text #line:55
        OOO0O0OO00OOOOOOO =O00OO00O0000000O0 #line:57
        print (OOO0O0OO00OOOOOOO )#line:58
        return OOO0O0OO00OOOOOOO #line:59
    except Exception as O0OO0O00OO00OO00O :#line:60
        print (O0OO0O00OO00OO00O )#line:61
def randomszxx ():#line:64
    OO00O0O00O0O0OO0O ='qwertyuioplkjhgfdsazxcvbnm1234567890'#line:65
    O00000O0OOOO00000 =''#line:66
    for O0OOOO0OO0OO000OO in range (0 ,64 ):#line:67
        O00000OOO00OO0OOO =choice (OO00O0O00O0O0OO0O )#line:68
        O00000O0OOOO00000 +=O00000OOO00OO0OOO #line:69
    return O00000O0OOOO00000 #line:71
def getlink (O00OO0OO0OOO000OO ):#line:74
    O0OO0O00OOOO00O00 ="https://www.maimemo.com/share/title"#line:75
    O0OOOOO0O0O0OOOO0 =randomszxx ()#line:76
    O000O0OOOO000OO0O ={"Host":"www.maimemo.com","Content-Type":"application/json","Accept-Encoding":"gzip, deflate, br","Connection":"keep-alive","Ignorable":"false","Accept":"*/*","User-Agent":"MaiMemo/4.4.30_7389 iOS/15.6 Device/iPad11,1 (ARM_64) Resolution/1536x2048 RAM/2.85 ROM/238.41 DId/4d1bc2f7f864b4afe57a4f30fa095932 InstallId/b1133f859c90e20bf392e1c4cfece593 DeviceName/C%20%20iPad Jbv/NIL AFNetworking/3.2.1 Timezone/Asia%2FShanghai+08:00 Theme/Day","Accept-Language":"zh-Hans-CN;q=1","Content-Length":"34","token":O0OOOOO0O0O0OOOO0 }#line:88
    O0O0OOOOO00000OO0 ={"uid":O00OO0OO0OOO000OO ,"action":"share"}#line:92
    try :#line:93
        O0OO0OOO0OO000OO0 =requests .post (O0OO0O00OOOO00O00 ,headers =O000O0OOOO000OO0O ,data =json .dumps (O0O0OOOOO00000OO0 ))#line:94
        OOOOOOO0OOO0OO00O =json .loads (O0OO0OOO0OO000OO0 .text )#line:95
        if 'uid'in str (OOOOOOO0OOO0OO00O ):#line:96
            O0000O00OOOO0O0OO =OOOOOOO0OOO0OO00O ['page']#line:97
            O00OOO0OOOO000000 =O0000O00OOOO0O0OO .find ('page/?')#line:98
            O0000O00OOOO0O0OO ='https://www.maimemo.com/share/page?'+O0000O00OOOO0O0OO [O00OOO0OOOO000000 +6 :]#line:99
            print (f'link获取成功，为{O0000O00OOOO0O0OO}')#line:100
            return O0000O00OOOO0O0OO #line:101
    except Exception as OOOOO0O0O0OO0O00O :#line:102
        print (OOOOO0O0O0OO0O00O )#line:103
def getlists (OO0O0OOOOOO0OOOO0 ):#line:105
    OO0O0OOOOOO0OOOO0 =OO0O0OOOOOO0OOOO0 [OO0O0OOOOOO0OOOO0 .find ('&pid=')+5 :OO0O0OOOOOO0OOOO0 .find ('&tid=')]#line:106
    O0OOOO000OO00000O =f'https://api.maimemo.com/api/v1/sharecontents/{OO0O0OOOOOO0OOOO0}/comments?token=null&offset=5&limit=100&hideUnreviewed=true'#line:107
    OO000OOO00O00O0O0 ={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}#line:110
    try :#line:111
        OO0O0O0O0O0O00O00 =requests .get (O0OOOO000OO00000O ,headers =OO000OOO00O00O0O0 )#line:112
        OO0OOOO000OO000O0 =json .loads (OO0O0O0O0O0O00O00 .text )#line:113
        OO0OOOO000OO000O0 =OO0OOOO000OO000O0 ['data']['comments']#line:114
        OOOOOO00OO0OO0O00 =len (OO0OOOO000OO000O0 )#line:115
        print (f'=======共找到{OOOOOO00OO0OO0O00}条记录=======')#line:116
        OOOOO00O00O0O000O =0 #line:117
        while OOOOO00O00O0O000O <OOOOOO00OO0OO0O00 :#line:118
            OO00O0OOO000O0OO0 =OO0OOOO000OO000O0 [OOOOO00O00O0O000O ]['creator']['uid']#line:119
            OO00O0OO000O0OO0O =getlink (OO00O0OOO000O0OO0 )#line:120
            asyncio .run (create_aiohttp (OO00O0OO000O0OO0O ))#line:121
            sleep (randint (1 ,2 ))#line:122
            print (f"{OO00O0OOO000O0OO0}墨墨分享链接访问成功{n}次")#line:123
            OOOOO00O00O0O000O +=1 #line:124
    except Exception as O0O0OO000OO0OOO00 :#line:125
        print (O0O0OO000OO0OOO00 )#line:126
uidarr =['10229269']#line:128
def main2 ():#line:130
    getip ()#line:131
    for O000OO0OO0OOOOOOO in range (len (uidarr )):#line:132
        OO000O0000000OOO0 =uidarr [O000OO0OO0OOOOOOO ]#line:133
        O0OOO0O0O0OO00O00 =getlink (OO000O0000000OOO0 )#line:134
        asyncio .run (create_aiohttp (O0OOO0O0O0OO00O00 ))#line:135
        print (f"{OO000O0000000OOO0}墨墨分享链接访问成功{n}次。")#line:136
        sleep (randint (1 ,2 ))#line:137
    getlists (O0OOO0O0O0OO00O00 )#line:138
if __name__ =='__main__':#line:140
    main2 ()
