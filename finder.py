import os
import re
import json
import logging
## log
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
# handler = logging.FileHandler("log.txt")
# handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#handler.setFormatter(formatter)

console = logging.StreamHandler()
console.setLevel(logging.INFO)

# logger.addHandler(handler)
logger.addHandler(console)

print("******By HongdaChen******")



def extract():
    #pyinstaller -i love.ico -c -F finder.py
    directory=input("=============please input your html's directory=================\n")
    # directory='D:\\恒生聚源\\AUT-2916\\600018798-信用浉河-首页-双公示'
    file_list=os.listdir(directory)
    html_list=[i for i in file_list if i[-5:]=='.html']
    result1=[]
    result2=[]
    res=[]
    file_num=0
    for html in html_list:
        f = open( directory+'\\'+html, 'r',encoding='utf-8')
        file = f.read()
        li = re.findall(r'<table ?.*?>(.*?)</table>',file)
        if len(li)>0:
            findList=re.findall(r'<td ?.*?>(.*?)</td>',li[0])
            result1.extend([findList[i] for i in range(len(findList)) if i%2==0])
            file_num+=1
        else:
            findList2=re.findall(r'<th ?.*?>(.*?)</th>',file)
            result2.extend([_.replace('<br>','') for _ in findList2])
            file_num+=1
        f.close()
        result1.extend(result2)
        res=list(set(result1))
    if file_num==len(html_list):
        print("all html files have been extracted!\n")
    # 拼接
    left='.*('
    right=').*'
    start=left+res[0]
    for i in range(1,len(res)):
        start+='|'+res[i]
    end=start+right
    print("the end format which you want is:\n")
    print(end)


    while True:
        temp_end = end
        temp_res = res
        start=left+res[0]
        exclude=input("\n\n\ninput which you want to exclude:(press <q> to quit this func)\n")
        if exclude=='q':
            break
        elif exclude==temp_res[0]:
            temp_end=temp_end.replace(temp_res[0]+"|","")
        else:
            for i in range(1,len(temp_res)):
                if temp_res[i]!=exclude:
                    start+='|'+temp_res[i]
            temp_end=start+right

        print("the end format which has rejected {} is:\n".format(exclude))
        print(temp_end)

        

def store():
    
    while True:
        dr=input("\nplease input the file of WGLX or WGJG or CFLX:(press <q> to quit this func)\n")
        
        if dr=='q':
            break
        else:
            fe = open(dr, 'r',encoding='utf-8')
            f = fe.read()
            WGLX_rule_list=f.split("\n")
            WGLX_condict={}
            for i in WGLX_rule_list:
                WGLX_code=re.findall(r'([A-Z0-9]*) *-',i)
                WGLX_cont=re.findall(r'“(.*?)”',i)
                if len(WGLX_code)*len(WGLX_cont)!=0:
                    WGLX_condict[WGLX_code[0]]=WGLX_cont

            js=json.dumps(WGLX_condict,sort_keys=True,ensure_ascii=False)
            print("\n\njson:\n"+js)
            

while True:
    func=input("=============please choose fun: 1:extract 2:store q:quit=============\n")
    if func=='q':
        break
    elif func=='1':
        try:
            extract()
        except (SystemExit, KeyboardInterrupt):
            raise
        except Exception:
            logger.error("Faild to extract", exc_info=True)
    elif func=='2':
        try:
            store()
        except (SystemExit, KeyboardInterrupt):
            raise
        except Exception:
            logger.error("Faild to store", exc_info=True)
